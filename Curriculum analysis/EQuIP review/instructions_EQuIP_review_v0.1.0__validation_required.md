# Instructions — EQuIP Review of the Marty Robot Curriculum (v0.1.0)

> **Status:** DRAFT — validation required. Per project rules: do **not** execute this
> instructions file until the user provides a `run.md` file. Any output generated must
> carry the `__validation_required` suffix.

## 1. Purpose

Act as an expert reviewer applying the **EQuIP Rubric for Lessons & Units: Science v3.1**
(Achieve, Inc., 2021) to the curriculum *"A Build-and-Learn Approach to Responsible
Robotics Using Marty the Robot"* (grade 8 NwT, Baden-Württemberg; classroom ages 12–16;
2 h/week). The rubric is **adapted** from NGSS (US) to the **Baden-Württemberg
Bildungsplan** (German) standards — see §4. This adaptation must be kept in mind for
every judgement and documented in the output.

## 2. Object of review — enacted curriculum, not the plan

The program was **planned for 6 weeks but enacted over 7 weeks**. Rate the **enacted
7-week curriculum**.

- **Primary evidence = the enacted weekly slide decks** (§3, list B).
- The plan document (`Curriculum for Marty project.pdf`) describes the *intended* design
  and is the source of the standards excerpts; execution was narrower than the plan.
  Where slides diverge from the plan, **rate what was enacted** and note the divergence
  in the evidence field (e.g., "planned but not enacted: …").
- **Track:** review the **experimental (Marty build) track** as the primary curriculum.
  Weeks 2–4 have `_Control` slide variants; review the experimental version
  (`_Nikola`/`_presented`) and add a note only where the control variant diverges
  substantially.

## 3. Inputs (read all before rating)

**A. Rubric**
- `Developped curriculum/EQuIP review/equip_rubric_structure__validation_required.csv`
  — the 19 criteria / 31 sub-items to apply (this review's checklist).
- Source rubric (for context only):
  `Literature/Literature on Curriculum design/Achieve Inc - 2021 - EQuIP rubric for lessons and units Science v31.pdf`

**B. Enacted curriculum materials** (`Developped curriculum/`)
| Week | Experimental track (primary) | Control variant (note only) |
|---|---|---|
| 1 | `W1 Intro to Social Robots - Teaching material EN.pdf` | — |
| 2 | `Marty - Woche2_presented.pptx.pdf` | `Marty_Woche2_Control.pptx.pdf` |
| 3 | `Marty_Woche3_Nikola.pptx.pdf` | `Marty_Woche3_Control.pptx.pdf` |
| 4 | `Marty_Woche4_Nikola.pptx.pdf` | `Marty_Woche4_Control.pptx.pdf` |
| 5 | `Marty_Woche5_28112025.pptx.pdf` | — |
| 6 | `Marty_Week6.pptx.pdf` | — |
| 7 | `Marty_Week7.pptx.pdf` | — |

**C. Plan + standards excerpts**
- `Developped curriculum/my notes/Curriculum for Marty project.pdf`
  - p. 1: process-related vs content-related competencies; prior knowledge; Aufträge 2.1–2.16
  - pp. 1–2: Learning objectives NIT 8 (NwT)
  - pp. 2–4: **Bildungsplan competency items** (3.1.2, 3.1.4, 3.2.1, 3.2.2, 3.2.2.2,
    3.2.3.3, 3.2.3, 3.2.4.1, 3.2.4.2, 3.2.4.3, 3.1.3.1, 3.1.5.2) — the standards lens
  - pp. 5–13: intervention plan + week-by-week plan (Weeks 1–6 only; Week 7 exists
    only as slides)

**D. Assessment instruments** (`Data_analysis/`)
- `survey_items_with_questions_COMPLETE.csv` — full item text, options, correct answers,
  difficulty, week taught
- `survey_items_inventory__validation_required.csv` — item inventory with administration
  waves (T1/T4/T7)
- `Data_analysis/Data/Buildbots_Codebook_15122025-2/` — per-instrument codebook tables
  (Learning objectives, RoSAS, MAILS, IMI, LLM interaction, etc.)

## 4. Standards adaptation table (NGSS → Bildungsplan / this curriculum)

| Rubric term (NGSS) | Apply as (this review) |
|---|---|
| Performance expectations | The numbered Bildungsplan competency items quoted in the plan PDF pp. 2–4 (e.g., 3.2.2 (15) "detect physical quantities with sensors") |
| Science & engineering practices (SEPs) | **Process-related competencies** (prozessbezogene Kompetenzen, plan PDF p. 1): programming, wiring/control of microcontrollers, reading datasheets, technical drawing, constructing/manufacturing, testing & evaluating products |
| Disciplinary core ideas (DCIs) | **Content-related competencies** (inhaltbezogene Kompetenzen, plan PDF p. 1): motors, sensors, circuits, algorithms/ML/LLMs, energy, product development |
| Crosscutting concepts (CCCs) | Crosscutting themes: **systems & processes thinking** (system boundaries, subsystems, black-box, energy/material/information flows, feedback loops — Bildungsplan 3.2.1), **sustainability**, **social equity**, **ethics** |
| Phenomena / problems | The Marty build project itself; real-world AI/robotics scenarios (LLM safety & hallucinations, sustainability of electronics/batteries, AI ethics) |
| "Elements" (for criterion I.B) | The *specific* numbered competency items or specific concepts — never broad headings |
| I.E Multiple Science Domains | Adapted: links across physics (energy, sensors, electromagnetic), computer science (algorithms, ML), technology/engineering (product development), and ethics/society |
| I.F Math and ELA (Common Core) | Adapted: grade-appropriate connections to mathematics (e.g., dataframes, histograms, P=E/T) and language/literacy in the German classroom context |

## 5. Procedure

**Step 0 — Familiarization.** Read all inputs in §3. Record: Grade 8 (NwT), title
"Marty the Robot — Build-and-Learn program (enacted 7 weeks)", reviewer ID = model name + run number.

**Step 1 — Lesson-level reviews (7×).** For each week 1–7, apply the **lesson criteria**
(I.A–C, II.A–E, III.A–D = 12 criteria) to that week's materials. For each criterion:
record (a) specific evidence with citation, (b) reasoning, (c) evidence-of-quality
rating, (d) suggestions for improvement. Then rate each category 0–3 using the
**lesson** scales (§6).

**Step 2 — Unit-level review (1×).** Apply **all 19 criteria** (incl. unit-only I.D–F,
II.F–G, III.E–F) across the whole 7-week program, drawing on Step-1 findings plus
cross-week coherence. Then rate each category 0–3 using the **unit** scales (§6).

**Step 3 — Gateway check.** If unit Category I < 2, flag prominently: per the rubric,
a vetting review would stop here and return feedback to the developer.

**Step 4 — Overall rating (unit scope only).** Sum the three unit category ratings;
assign E / E-I / R / N per §6; write summary comments.

## 6. Rating scales (verbatim from rubric pp. 5, 7–14)

**Evidence of quality per criterion:** None / Inadequate / Adequate / Extensive.

**Category descriptors:** 3 = Exemplifies NGSS Quality; 2 = Approaching NGSS Quality;
1 = Developing toward NGSS Quality; 0 = Not representing NGSS Quality.

**Category I — lesson scale (A–C):**
- 3: Extensive evidence to meet at least two criteria (and at least adequate evidence for the third)
- 2: Adequate evidence to meet all three criteria in the category
- 1: Adequate evidence to meet at least one criterion, but insufficient evidence for at least one other
- 0: Inadequate (or no) evidence to meet any of the criteria

**Category I — unit scale (A–F):**
- 3: At least adequate evidence for all unit criteria; extensive evidence for criteria A–C
- 2: At least some evidence for all unit criteria (A–F); adequate evidence for criteria A–C
- 1: Adequate evidence for some criteria, but inadequate/no evidence for at least one criterion A–C
- 0: Inadequate (or no) evidence to meet any criteria (A–F)

**Category II — lesson scale (A–E):**
- 3: At least adequate evidence for all criteria; extensive evidence for at least one
- 2: Some evidence for all criteria and adequate evidence for at least four, including A
- 1: Adequate evidence of quality for at least two criteria
- 0: Adequate evidence of quality for no more than one criterion

**Category II — unit scale (A–G):**
- 3: At least adequate evidence for all criteria; extensive evidence for at least two
- 2: Some evidence for all criteria and adequate evidence for at least five, including A
- 1: Adequate evidence for at least three criteria
- 0: Adequate evidence for no more than two criteria

**Category III — lesson scale (A–D):**
- 3: At least adequate evidence for all criteria; extensive evidence for at least one
- 2: Some evidence for all criteria and adequate evidence for at least three, including A
- 1: Adequate evidence for at least two criteria
- 0: Adequate evidence for no more than one criterion

**Category III — unit scale (A–F):**
- 3: At least adequate evidence for all criteria; extensive evidence for at least one
- 2: Some evidence for all criteria and adequate evidence for at least five, including A
- 1: Adequate evidence for at least three criteria
- 0: Adequate evidence for no more than two criteria

**Gateway:** Category I (unit) is non-negotiable — if 0 or 1, a vetting review stops;
feedback goes to the developer.

**Overall (unit):** E = high quality NGSS design (total ~8–9); E/I = high quality if
improved (~6–7); R = revision needed (~3–5); N = not ready to review (0–2). The total
is an approximate guide; documented evidence may justify deviation.

## 7. Evidence rules (strict)

1. Every evidence statement cites `filename, p./slide N` plus a **short verbatim quote**.
   German quotes are kept in German with an English gloss in parentheses.
2. If no evidence is found, write **"None"** and state what was searched.
   **Never fabricate evidence, quotes, or slide numbers.**
3. Criterion I.B: evidence must name the **specific element** (numbered competency item
   or specific concept) for each dimension separately; rate i, ii, iii individually.
4. Enacted > planned: divergences between slides and the plan PDF are noted, and the
   enacted version is rated.
5. Mark any uncertain citation or borderline judgement with `[CHECK]` for human review.

## 8. Output

One CSV per run: `equip_review_output_run<N>__validation_required.csv`
(same folder as this file), columns:

```
scope,row_type,category,criterion_id,criterion_name,specific_evidence_and_reasoning,evidence_of_quality,suggestions_for_improvement,rating_0_3,rating_justification,overall_rating,summary_comments
```

- `scope`: `week_1` … `week_7` or `unit`
- `row_type`: `criterion` | `category_rating` | `overall_rating`
- Per week scope: 12 criterion rows + 3 category_rating rows (I, II, III)
- Unit scope: 19 criterion rows + 3 category_rating rows + 1 overall_rating row
- Expected total: 7 × 15 + 23 = **128 rows**
- `evidence_of_quality` ∈ {None, Inadequate, Adequate, Extensive} (criterion rows only)
- `rating_0_3` on category_rating rows; `overall_rating` ∈ {E, E/I, R, N} on the
  overall row; `summary_comments` on the overall row

## 9. Reliability

The EQuIP process is designed for multiple reviewers. Run this review **at least twice,
in independent sessions with no memory of prior runs** (run1, run2, …). Inter-rater
agreement (e.g., Cohen's κ on `evidence_of_quality` and on category ratings) is computed
afterwards in a separate step, consistent with the project's two-coder methodology
(Methods §2.2).

## 10. Known limitations of this review (state in output summary)

- Rubric designed for NGSS; applied here via the §4 adaptation to the Bildungsplan.
- Reviewer sees slides and instruments, not classroom enactment; teacher guidance that
  existed only orally is invisible to this review.
- Week 7 has slides but no corresponding section in the plan PDF.
