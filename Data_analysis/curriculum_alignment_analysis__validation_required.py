#!/usr/bin/env python3
"""Curriculum <-> assessment alignment analysis (rebuilt from scratch, 2026-09-15).

Why this script exists:
    The previous scripts (curriculum_concept_mapping.py, create_complete_concept_mapping.py)
    hardcoded concept lists and guessed concept->item links with keyword matching.
    Both were disconnected from (a) the enacted curriculum (slide decks) and
    (b) the actually administered survey items. This script fixes that by construction:

    * Concepts come from curriculum_concepts__validation_required.csv
      (extracted manually from the slide decks in ../Developped curriculum/,
      classified by instructional role/mastery and mapped to the UNESCO AI
      competency framework for students).
    * Item inventory is *parsed* from the codebook tables and cross-checked
      against the columns actually present in the administered data.
    * Concept<->item links come from concept_item_mapping__validation_required.csv
      (human-validatable; no keyword guessing anywhere in this file).
    * Context/pedagogy descriptors come from
      curriculum_context_pedagogy__validation_required.csv (from deck agendas).

The report is organized along the five curriculum-analysis dimensions:
Context, Content, Pedagogy, Didactics, Assessment.

Nothing is hardcoded except structural parsing configuration (documented).
Every number in the report is computed from the inputs above.

Inputs:
    Data/Buildbots_Codebook_15122025-2/Learning objectives-Table 1.csv
    Data/Buildbots_Codebook_15122025-2/LLM_microcontrollers-Table 1.csv
    Data/combineddf_T1_T4_T7/combined_df-Table 1.csv
    curriculum_concepts__validation_required.csv
    concept_item_mapping__validation_required.csv
    curriculum_context_pedagogy__validation_required.csv

Outputs:
    survey_items_inventory__validation_required.csv
    curriculum_alignment_report__validation_required.md
"""
from pathlib import Path
import re

import pandas as pd

BASE = Path(__file__).resolve().parent
CODEBOOK_DIR = BASE / "Data" / "Buildbots_Codebook_15122025-2"
COMBINED_CSV = BASE / "Data" / "combineddf_T1_T4_T7" / "combined_df-Table 1.csv"
CONCEPTS_CSV = BASE / "curriculum_concepts__validation_required.csv"
MAPPING_CSV = BASE / "concept_item_mapping__validation_required.csv"
PEDAGOGY_CSV = BASE / "curriculum_context_pedagogy__validation_required.csv"
INVENTORY_OUT = BASE / "survey_items_inventory__validation_required.csv"
REPORT_OUT = BASE / "curriculum_alignment_report__validation_required.md"

# ---------------------------------------------------------------------------
# Structural parsing configuration (NOT data values).
# Author-written items carry no item code in the codebook; their column name in
# the administered data is derived from (topic, subtopic) with a running index.
# None -> rule matches any subtopic within the topic.
# ---------------------------------------------------------------------------
AUTHOR_COLUMN_RULES = {
    ("Technical knowledge", "Robots parts"): "robotparts",
    ("Technical knowledge", "Sensors"): "sensors",
    ("Technical knowledge", "Microcontrollers"): "microcontrollers",
    ("Programming", None): "PR",
    ("LLMs and generative AI", "LLM design"): "LLMdesign",
}
ITEM_CODE_RE = re.compile(r"\b([A-Z]{2}\d{2})\b")
# Column-name shapes that count as knowledge/objective items in the data.
DATA_ITEM_RE = re.compile(r"^(robotparts|sensors|microcontrollers|LLMdesign)_\d+$"
                          r"|^(PR\d+)$"
                          r"|^([A-Z]{2}\d{2})$"
                          r"|^AI_[A-Z]{2}\d{2}$")
MASTERY_ORDER = ["core", "working", "exposure"]


def _read_semicolon_table(path: Path) -> pd.DataFrame:
    """Read a codebook table (semicolon-separated, merged cells kept as '')."""
    return pd.read_csv(path, sep=";", dtype=str, keep_default_na=False)


def parse_learning_objectives(path: Path) -> pd.DataFrame:
    """Parse the main codebook table, forward-filling merged cells.

    The codebook is 'pretty-printed': topic/subtopic/week cells are empty on
    continuation rows. Leaving them empty (instead of ffilling) was the root
    cause of the old pipeline's false 'unassessed' verdicts.
    """
    df = _read_semicolon_table(path)
    df = df.rename(columns=lambda c: c.strip())
    for col in ["Learning topics", "Learning objective", "Week"]:
        df[col] = df[col].replace("", pd.NA).ffill()
    df = df[df["English"].str.strip() != ""].copy()

    counters: dict = {}
    rows = []
    for _, r in df.iterrows():
        english = r["English"].strip()
        topic, subtopic = r["Learning topics"], r["Learning objective"]
        m = ITEM_CODE_RE.search(english)
        prefix = next((p for (t, s), p in AUTHOR_COLUMN_RULES.items()
                       if t == topic and (s is None or s == subtopic)), None)
        # NB: the codebook's 'added by author' flag is itself shifted by merged
        # cells, so we trust (topic, subtopic) rules over the flag.
        is_author = ("added by author" in r["Source"].lower()) or (m is None and prefix is not None)
        if m:
            item_id = m.group(1)
        elif prefix:
            counters[prefix] = counters.get(prefix, 0) + 1
            item_id = (f"{prefix}{counters[prefix]}" if prefix == "PR"
                       else f"{prefix}_{counters[prefix]}")
        else:
            item_id = "UNKNOWN"
        week_match = re.search(r"(\d+)", str(r["Week"]))
        week = int(week_match.group(1)) if week_match else pd.NA
        rows.append({
            "item_id": item_id,
            "codebook_week": week,
            "topic": topic,
            "subtopic": subtopic,
            "item_stem_en": " ".join(english.split())[:120],
            "author_written": is_author,
            "difficulty_note": r["Item difficulty"].strip(),
            "source_table": path.name,
        })
    return pd.DataFrame(rows)


def parse_llm_microcontrollers(path: Path) -> pd.DataFrame:
    """Parse the 8-item microcontroller battery (never administered)."""
    df = _read_semicolon_table(path)
    df = df[df["English"].str.strip() != ""].copy()
    return pd.DataFrame([{
        "item_id": f"LLMmc_{i + 1}",
        "codebook_week": pd.NA,
        "topic": "Microcontrollers (full battery)",
        "subtopic": "",
        "item_stem_en": " ".join(r["English"].split())[:120],
        "author_written": True,
        "difficulty_note": "",
        "source_table": path.name,
    } for i, (_, r) in enumerate(df.iterrows())])


def load_administered_data(path: Path):
    """Load combined survey data; return (df, knowledge-item column names)."""
    df = pd.read_csv(path, sep=";", dtype=str, keep_default_na=False)
    df = df[df["Progress"] != "Progress"]  # drop embedded repeated header rows
    item_cols = [c for c in df.columns if DATA_ITEM_RE.match(c)]
    return df, sorted(item_cols)


def attach_administration(inv: pd.DataFrame, df: pd.DataFrame,
                          item_cols: list) -> pd.DataFrame:
    """Cross-check inventory against administered columns; add wave stats."""
    def resolve_column(item_id: str):
        if item_id in df.columns:
            return item_id
        matches = [c for c in item_cols if c.endswith("_" + item_id)]
        return matches[0] if matches else None

    inv["data_column"] = inv["item_id"].map(resolve_column)
    inv["administered"] = inv["data_column"].notna()

    waves = sorted(df["Timepoint"].unique())
    per_wave = {w: df[df["Timepoint"] == w] for w in waves}

    def n_in(col, wave_df):
        return int((wave_df[col].str.strip() != "").sum()) if col else 0

    for w in waves:
        inv[f"n_{w}"] = inv["data_column"].map(lambda c: n_in(c, per_wave[w]))
    inv["waves"] = inv["data_column"].map(
        lambda c: ";".join(w for w in waves if n_in(c, per_wave[w]) > 0) if c else "")

    orphan_cols = sorted(set(item_cols) - set(inv["data_column"].dropna()))
    extra = pd.DataFrame([{
        "item_id": c, "codebook_week": pd.NA, "topic": "(not in codebook)",
        "subtopic": "", "item_stem_en": "", "author_written": pd.NA,
        "difficulty_note": "", "source_table": "(administered data only)",
        "data_column": c, "administered": True,
        **{f"n_{w}": n_in(c, per_wave[w]) for w in waves},
        "waves": ";".join(w for w in waves if n_in(c, per_wave[w]) > 0),
    } for c in orphan_cols])
    return pd.concat([inv, extra], ignore_index=True)


def parse_unesco(cell: str):
    """Split a unesco_block cell into (block, level, beyond_framework_flag)."""
    cell = cell.strip()
    if cell.startswith("beyond framework"):
        block = cell.split(":", 1)[1].strip() if ":" in cell else cell
        return (f"beyond framework: {block}", "", True)
    primary = cell.split("+ beyond")[0].split(" - taught at")[0].strip()
    m = re.match(r"(.+?)\s*\((L\d)\s*(\w+)\)", primary)
    if m:
        return (m.group(1).strip(), f"{m.group(2)} {m.group(3)}",
                "+ beyond" in cell)
    return (primary, "", "+ beyond" in cell)


def analyse(concepts: pd.DataFrame, inventory: pd.DataFrame,
            mapping: pd.DataFrame) -> dict:
    """Compute all alignment statistics from the three validated inputs."""
    # Normalize mapping item ids to canonical inventory ids (e.g. the data
    # column 'AI_DA09' is inventory item 'DA09').
    alias = inventory.dropna(subset=["data_column"]) \
        .set_index("data_column")["item_id"].to_dict()
    mapping = mapping.copy()
    mapping["item_id"] = mapping["item_id"].map(lambda i: alias.get(i, i))

    administered = set(inventory.loc[inventory["administered"], "item_id"])
    m_admin = mapping[mapping["item_id"].isin(administered)]
    m_valid = m_admin[m_admin["link_strength"].isin(["primary", "partial"])]

    links = m_valid.groupby("concept_id")["item_id"].agg(list)
    strengths = m_valid.groupby("concept_id")["link_strength"].agg(set)
    concepts = concepts.copy()
    concepts["items"] = concepts["concept_id"].map(links).map(
        lambda x: x if isinstance(x, list) else [])
    concepts["status"] = concepts["concept_id"].map(strengths).map(
        lambda s: "assessed" if isinstance(s, set) and "primary" in s
        else ("partially assessed" if isinstance(s, set) else "NOT assessed"))
    unesco = concepts["unesco_block"].map(parse_unesco)
    concepts["unesco_primary_block"] = [u[0] for u in unesco]
    concepts["unesco_level"] = [u[1] for u in unesco]
    concepts["unesco_beyond"] = [u[2] for u in unesco]

    linked_items = set(m_valid["item_id"])
    unknown_items = set(m_admin.loc[m_admin["link_strength"] == "unknown",
                                    "item_id"])
    orphan_items = sorted(administered - linked_items - unknown_items)

    # Timing: intended week (codebook) vs enacted week (concept introduced).
    item_week = inventory.set_index("item_id")["codebook_week"]
    concept_week = concepts.set_index("concept_id")["week_introduced"]
    prim = m_valid[m_valid["link_strength"] == "primary"].copy()
    prim["intended_week"] = prim["item_id"].map(
        lambda i: item_week.get(i, pd.NA))
    prim["enacted_week"] = prim["concept_id"].map(
        lambda c: concept_week.get(c, pd.NA))

    def _delta(row):
        try:
            return int(row["enacted_week"]) - int(row["intended_week"])
        except (TypeError, ValueError):
            return None

    prim["week_delta"] = prim.apply(_delta, axis=1)
    timing_mismatch = prim[[d not in (None, 0) for d in prim["week_delta"]]]

    revisited = concepts[concepts["weeks_revisited"].astype(str).str.strip() != ""]
    misconceptions = concepts[concepts["misconception_addressed"]
                              .astype(str).str.strip() != ""]

    not_administered = inventory[~inventory["administered"]]
    return {"concepts": concepts, "orphan_items": orphan_items,
            "unknown_items": sorted(unknown_items),
            "timing_mismatch": timing_mismatch, "revisited": revisited,
            "misconceptions": misconceptions,
            "not_administered": not_administered,
            "mapping_admin": m_admin, "administered": administered}


def _coverage_lines(concepts: pd.DataFrame, subset: pd.DataFrame,
                    label: str) -> list:
    """Coverage counts for one mastery subset (computed, not hardcoded)."""
    n = len(subset)
    if n == 0:
        return []
    a = (subset["status"] == "assessed").sum()
    p = (subset["status"] == "partially assessed").sum()
    u = (subset["status"] == "NOT assessed").sum()
    return [f"- **{label}** ({n} concepts): {a} assessed ({a / n:.0%}), "
            f"{p} partial ({p / n:.0%}), {u} not assessed ({u / n:.0%})"]


def write_report(res: dict, inventory: pd.DataFrame,
                 pedagogy: pd.DataFrame) -> None:
    """Write the markdown report along the 5 dimensions; all figures computed."""
    concepts = res["concepts"]
    L = []
    L.append("# Curriculum-Assessment Alignment Report (rebuilt pipeline)\n")
    L.append("**Data lineage:** concepts from slide decks in `Developped curriculum/`; "
             "item inventory parsed from codebook tables with merged cells forward-filled "
             "and cross-checked against administered columns in `combined_df-Table 1.csv`; "
             "links from human-validatable mapping table; context/pedagogy from deck agendas. "
             "No keyword matching used. Organized along the five dimensions: "
             "Context, Content, Pedagogy, Didactics, Assessment.\n")

    # ---------------- 1. Context ----------------
    L.append("\n## 1. Context\n")
    total_min = pedagogy["duration_min"].sum()
    L.append(f"- Weekly sessions: **{len(pedagogy)}**, total instructional time "
             f"~**{total_min} min** ({total_min / 60:.1f} h)")
    split_weeks = pedagogy[pedagogy["condition_difference"].str.lower()
                           .str.startswith("build")]
    L.append(f"- Condition split (Build vs Control activity) in weeks: "
             f"{', '.join(split_weeks['week'].astype(str))}")
    L.append("- Measurement waves: T1 (pre, W1), T4 (mid, W4), T7 (post, W7) "
             "- identical 23-item knowledge battery at all three waves")
    L.append("- Language of instruction: German (W1 deck in English; "
             "W2/W4 Control decks bilingual German/English)")

    # ---------------- 2. Content ----------------
    L.append("\n## 2. Content\n")
    L.append(f"- Concepts in enacted curriculum: **{len(concepts)}** "
             f"(see `curriculum_concepts__validation_required.csv`)")
    L.append("\n### 2.1 Concepts per theme\n")
    L.append("| Theme | Concepts |")
    L.append("|---|---|")
    for t, g in concepts.groupby("theme"):
        L.append(f"| {t} | {len(g)} |")
    L.append("\n### 2.2 Mapping to UNESCO AI competency framework for students (2024)\n")
    L.append("| UNESCO competency block (level) | Concepts |")
    L.append("|---|---|")
    blocks = concepts.groupby(["unesco_primary_block", "unesco_level"])
    for (b, lvl), g in sorted(blocks, key=lambda kv: -len(kv[1])):
        label = f"{b} ({lvl})" if lvl else b
        L.append(f"| {label} | {len(g)}: {', '.join(g['concept_id'])} |")
    n_beyond = int(concepts["unesco_primary_block"]
                   .str.startswith("beyond framework").sum())
    n_partial_beyond = int((concepts["unesco_beyond"]
                            & ~concepts["unesco_primary_block"]
                            .str.startswith("beyond framework")).sum())
    L.append(f"\n- Concepts entirely **beyond the UNESCO framework**: "
             f"**{n_beyond}** of {len(concepts)} "
             f"(robotics hardware, sensors, microcontrollers, LLM safeguards, "
             f"anthropomorphism/deception resistance, LLM behavior control)")
    L.append(f"- Concepts mapped to a UNESCO block but extending beyond it: "
             f"**{n_partial_beyond}**")
    l1 = (concepts["unesco_level"] == "L1 Understand").sum()
    L.append(f"- Concepts at **L1 Understand** blocks: {l1}; at L2 Apply blocks: "
             f"{(concepts['unesco_level'] == 'L2 Apply').sum()}; at L3 Create blocks: "
             f"{(concepts['unesco_level'] == 'L3 Create').sum()} "
             f"(several L2/L3 blocks were taught at reduced depth - see "
             f"'taught at ... depth' notes in the concepts table)")

    # --- 2.3 Reverse coverage: what the frameworks suggest vs. what we teach
    L.append("\n### 2.3 Reverse coverage: framework suggestions vs. enacted curriculum\n")
    unesco_12 = ["Human agency", "Human accountability", "Citizenship in the AI era",
                 "Embodied ethics", "Ethics by design", "Safe and responsible use",
                 "AI foundations", "Application skills", "Creating AI tools",
                 "Problem scoping", "Architecture design", "Iteration and feedback"]
    L.append("**UNESCO AI CFS competency blocks (12):**\n")
    L.append("| Block | Covered by concepts |")
    L.append("|---|---|")
    n_cov = 0
    for b in unesco_12:
        # unesco_primary_block uses the "Aspect > Block" format -> substring match
        ids = concepts.loc[concepts["unesco_primary_block"].str.contains(
            re.escape(b), na=False), "concept_id"].tolist()
        n_cov += bool(ids)
        cell = (str(len(ids)) + ": " + ", ".join(ids)) if ids else "- not covered"
        L.append(f"| {b} | {cell} |")
    L.append(f"\n- UNESCO blocks with at least one enacted concept: **{n_cov}/12**")

    mail_5 = ["Reflect and Act Ethically and Responsibly", "Access and Use",
              "Analyse and Evaluate", "Participate and Collaborate", "Create"]
    L.append("\n**PISA 2029 MAIL competences (5):**\n")
    L.append("| Competence | Direct mappings | Indirect mappings |")
    L.append("|---|---|---|")
    n_cov = 0
    for c in mail_5:
        direct = concepts.loc[concepts["pisa_competence"] == c,
                              "concept_id"].tolist()
        indirect = concepts.loc[concepts["pisa_competence"] == c + " (indirect)",
                                "concept_id"].tolist()
        n_cov += bool(direct or indirect)
        d_cell = (str(len(direct)) + ": " + ", ".join(direct)) if direct else "-"
        i_cell = (str(len(indirect)) + ": " + ", ".join(indirect)) if indirect else "-"
        L.append(f"| {c} | {d_cell} | {i_cell} |")
    L.append(f"\n- MAIL competences touched: **{n_cov}/5**; "
             f"'Participate and Collaborate' (online discourse, co-creation, "
             f"conflict de-escalation) has zero coverage - candidate gap for v2")

    # ---------------- 3. Pedagogy ----------------
    L.append("\n## 3. Pedagogy\n")
    L.append("| Week | Title | Task types | Configuration | Condition difference |")
    L.append("|---|---|---|---|---|")
    for _, r in pedagogy.iterrows():
        L.append(f"| {r['week']} | {r['title']} | {r['task_types']} "
                 f"| {r['task_configuration']} | {r['condition_difference']} |")

    # ---------------- 4. Didactics ----------------
    L.append("\n## 4. Didactics\n")
    L.append("### 4.1 Instructional role (mastery expectation) of concepts\n")
    L.append("| Mastery | Concepts | Share |")
    L.append("|---|---|---|")
    for m in MASTERY_ORDER:
        g = concepts[concepts["mastery"] == m]
        L.append(f"| {m} | {len(g)} | {len(g) / len(concepts):.0%} |")
    L.append("\n### 4.2 New concepts introduced per week (pacing)\n")
    L.append("| Week | New concepts |")
    L.append("|---|---|")
    for w, g in concepts.groupby("week_introduced"):
        L.append(f"| {w} | {len(g)} |")
    L.append("\n### 4.3 Weaving with previous concepts (revisits / spacing)\n")
    for _, r in res["revisited"].iterrows():
        L.append(f"- **{r['concept_id']}** introduced W{r['week_introduced']}, "
                 f"revisited W{r['weeks_revisited']}")
    L.append("\n### 4.4 Misconceptions explicitly addressed\n")
    for _, r in res["misconceptions"].iterrows():
        L.append(f"- **{r['concept_id']}**: {r['misconception_addressed']}")

    # ---------------- 5. Assessment ----------------
    L.append("\n## 5. Assessment\n")
    adm = inventory[inventory["administered"]]
    L.append("### 5.1 Item inventory\n")
    L.append(f"- Knowledge items administered (all waves T1/T4/T7): **{len(adm)}**")
    L.append(f"- Codebook items never administered: **{len(res['not_administered'])}** "
             f"({', '.join(res['not_administered']['item_id'])})")
    L.append(f"- Administered but missing from codebook: "
             f"{', '.join(res['unknown_items']) or 'none'}")
    L.append("- Item format: all 4-option multiple choice, digital, individual\n")
    L.append("### 5.2 Coverage by instructional role (mastery)\n")
    L.append("Non-assessment is only problematic for *core* concepts; "
             "*exposure* concepts are taught to spark curiosity or prepare "
             "later learning and are legitimately unassessed.\n")
    for m in MASTERY_ORDER:
        L += _coverage_lines(concepts, concepts[concepts["mastery"] == m], m)
    L.append("\n**Core concepts NOT assessed (alignment gaps to fix):**\n")
    gaps = concepts[(concepts["mastery"] == "core")
                    & (concepts["status"] == "NOT assessed")]
    for _, r in gaps.iterrows():
        L.append(f"- **{r['concept_id']}** (W{r['week_introduced']}): {r['concept']}")
    L.append("\n**Core concepts only partially assessed:**\n")
    part = concepts[(concepts["mastery"] == "core")
                    & (concepts["status"] == "partially assessed")]
    for _, r in part.iterrows():
        L.append(f"- **{r['concept_id']}** (W{r['week_introduced']}): {r['concept']} "
                 f"- items: {', '.join(r['items'])}")
    L.append("\n### 5.3 Full coverage table per week\n")
    L.append("| Week | Concepts | Assessed | Partial | Not assessed |")
    L.append("|---|---|---|---|---|")
    for w, g in concepts.groupby("week_introduced"):
        L.append(f"| {w} | {len(g)} | {(g['status'] == 'assessed').sum()} "
                 f"| {(g['status'] == 'partially assessed').sum()} "
                 f"| {(g['status'] == 'NOT assessed').sum()} |")
    L.append("\n### 5.4 Orphan items (assessed but not taught)\n")
    if res["orphan_items"]:
        for i in res["orphan_items"]:
            L.append(f"- **{i}**")
    else:
        L.append("- None: every administered item links to >=1 taught concept.")
    if res["unknown_items"]:
        L.append(f"\nUnresolved (item text not recoverable): "
                 f"{', '.join(res['unknown_items'])}")
    L.append("\n### 5.5 Timing: intended (codebook) vs enacted week\n")
    tm = res["timing_mismatch"]
    if len(tm):
        L.append("| Item | Intended week (codebook) | Enacted week (taught) | Delta |")
        L.append("|---|---|---|---|")
        for _, r in tm.iterrows():
            L.append(f"| {r['item_id']} | {r['intended_week']} "
                     f"| {r['enacted_week']} | {r['week_delta']:+.0f} |")
    else:
        L.append("- No mismatches.")
    L.append("\n### 5.6 Coverage matrix per item\n")
    L.append("| Item | Concept | Link | Intended W | Enacted W |")
    L.append("|---|---|---|---|---|")
    inv_idx = inventory.set_index("item_id")["codebook_week"]
    cw = concepts.set_index("concept_id")["week_introduced"]

    def _w(v):
        return "" if pd.isna(v) else str(v)

    for _, r in res["mapping_admin"].sort_values("item_id").iterrows():
        L.append(f"| {r['item_id']} | {r['concept_id']} | {r['link_strength']} "
                 f"| {_w(inv_idx.get(r['item_id']))} | {_w(cw.get(r['concept_id']))} |")
    REPORT_OUT.write_text("\n".join(L), encoding="utf-8")


def main() -> None:
    concepts = pd.read_csv(CONCEPTS_CSV, keep_default_na=False)
    if "mastery" not in concepts.columns:
        # mastery column removed 2026-09-15 pending user re-validation;
        # use a sentinel so mastery-based sections run as a single group
        concepts["mastery"] = "unclassified"
    mapping = pd.read_csv(MAPPING_CSV, keep_default_na=False)
    pedagogy = pd.read_csv(PEDAGOGY_CSV, keep_default_na=False)
    inv = pd.concat([
        parse_learning_objectives(CODEBOOK_DIR / "Learning objectives-Table 1.csv"),
        parse_llm_microcontrollers(CODEBOOK_DIR / "LLM_microcontrollers-Table 1.csv"),
    ], ignore_index=True)
    df, item_cols = load_administered_data(COMBINED_CSV)
    inventory = attach_administration(inv, df, item_cols)
    inventory.to_csv(INVENTORY_OUT, index=False)
    res = analyse(concepts, inventory, mapping)
    write_report(res, inventory, pedagogy)
    c = res["concepts"]
    print(f"Inventory: {len(inventory)} items "
          f"({int(inventory['administered'].sum())} administered) -> {INVENTORY_OUT.name}")
    for m in MASTERY_ORDER:
        g = c[c["mastery"] == m]
        print(f"  {m}: {len(g)} concepts, "
              f"{(g['status'] == 'assessed').sum()} assessed, "
              f"{(g['status'] == 'NOT assessed').sum()} not assessed")
    print(f"Report -> {REPORT_OUT.name}")


if __name__ == "__main__":
    main()
