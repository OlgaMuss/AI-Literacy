# Framework Map — organizing the literature by object × question

> **Status:** `validation_required`. Created 2026-09-22. Purpose: single reference for where every framework/instrument/theory in the project belongs, so sources are never compared across categories.
> **Core principle:** the mess comes from mixing *objects of analysis*. Sort every source by **which question it answers about which object** — one object, one question, one place in the paper.

## The map (Q0–Q7)

| # | Question it answers | Object of analysis | Our sources | Paper location |
|---|---|---|---|---|
| **Q0** | Why does this matter? | theory lenses (justification) | Schwab's commonplaces, Klafki's Didaktik, Chevallard's transposition, Carroll (time), Sweller (load), Biggs (alignment), UbD, CIPP, ICAP (Chi & Wylie), SAFE (CASEL), Bloom, Four Pillars (Meyer et al. 2021), Black & Wiliam | §3.1 dimension derivation |
| **Q1** | What *should* learners become able to do? | learner — desired state | **Competency frameworks & standards:** UNESCO AI CFS 2024, AILit (OECD/EC 2026), PISA 2029 MAIL, DigComp, Bildungsplan BW (NwT), NGSS | §3.3 mapping + reverse coverage; §3.4 generation inputs |
| **Q2** | What is there to learn, and how does it connect? | knowledge domain | AI4K12 Five Big Ideas, concept maps, Atlas of Science Literacy strand maps, learning progressions / grade bands (Yang 2025) | Content + Didactics dimensions; Concepts Atlas |
| **Q3** | What was actually built/taught? | the artifact | 15 reviewed curricula + our Marty curriculum, described at learning-point granularity | §2.2, §2.3, §3.3 |
| **Q4** | Is the artifact good? | artifact quality | **Curriculum-evaluation instruments:** EQuIP v3.1, Project 2061 procedure (Kesidou & Roseman 2002; Stern & Roseman 2004), IQOer, IPN Kriterienkatalog, KMK strategy, SBZVO §5 → synthesized into our 5 dimensions + transversal Reusability layer | §3.1–3.3 |
| **Q5** | Did learners learn / feel? | learner — actual state | 23-item MC battery (+IDK), weekly IMI, MAILS, project evaluation, teacher pulse | §2.1, §2.4 |
| **Q6** | Is the measurement good? | instruments | our 9 Sense-B checks; Haladyna et al. 2002; Marsh 1986; Blueprints Ch. 8 standards (validity/reliability/feasibility/equity) | §3.2 Sense B |
| **Q7** | What does the field's evidence say? | evidence base (meta-level) | ISEE Assessment WG1–4 (Duraiappah & van Atteveldt 2022 — IPCC-style evidence review, *not* educational testing), EEF Toolkit | §1 / §4 anchors only |

## Where the stragglers live

- **Competencies, skills, attitudes** = the vocabulary of Q1 (and what Q5 measures).
- **Pedagogical strategies** (PRIMM, Four Pillars, project-based learning) = properties of the artifact (Q3), coded under Pedagogy (Q4), justified by theory (Q0).
- **Progression** = ordering inside the artifact (Q3), evaluated under Didactics (Q4), informed by domain maps (Q2).
- **Didactics** = our dimension name inside Q4.

## Three anti-mess rules

1. **One object, one question, one place.** Cross-cell "comparisons" are category errors: a target spec (Q1, e.g. UNESCO) and an artifact rubric (Q4, e.g. EQuIP) cannot be compared — only *mapped* (our §3.3 UNESCO block mapping + reverse coverage).
2. **Ban the bare word "assessment."** It does four jobs: artifact evaluation (Q4), learner measurement (Q5), instrument quality (Q6), field-evidence assessment (Q7). Always write "assessment *of what*." §3.2's Sense A/B split is the Q4/Q6 instance of this rule.
3. **Cite the role, not the document.** The same source can play two roles — PISA MAIL is a Q1 competence model (Content mapping) *and* a Q0 difficulty-driver source (Didactics, MAIL pp. 44–45). Name the role at each citation.

## Transversal Reusability layer (6th dimension — cuts across Q4's five dimensions)

**Status: facet names under review (user, 2026-09-22).** Working labels: **legibility** (≈ meaning: can an adopter understand what it *is*?) → **fit** (≈ usefulness: can they judge fit to *their* context?) → **adaptability** (reuse stricto sensu: can they modify and redeploy?). Ordered = the adoption pipeline.

Per-dimension probes:
- **Context:** setting/constraints documented enough to judge fit (our §2.2 constraint-intersection method *is* a fit procedure).
- **Content:** learning points self-contained and clearly delimited (IQOer S3, items 3.1–3.5).
- **Pedagogy:** activity re-enactable without the author (our teacher-preparation-gap finding).
- **Didactics:** dose/sequence rationale explicit → re-timeable (our 2–3× pacing overruns = undocumented dose).
- **Assessment:** items + answer keys + scoring guidance shipped (our §2.2 gap: only ENARIS).
- **Artifact-wide technical/legal:** machine-readability, metadata standards, licence (IQOer S16/S13; KMK Veränderbarkeit/Teilbarkeit).

**Framing:** the five dimensions are theory-derived ("is it good teaching?"); this layer is problem-derived ("can anyone else use it?") — the framework's bridge to the title *Curricula as Data*. Our learning-point schema satisfies IQOer S3/S16 by construction.

### Temporal axis — curriculum ecology (reuse across *time*)

**Wiley's 5R — verified 2026-09-22** against the primary source: Wiley, D. (2016, July 1). *Defining the "Open" in Open Content and Open Educational Resources*. [opencontent.org/definition/](https://opencontent.org/definition/). The 5R activities permitted by open licences: **Retain** (make, own, control a copy) · **Revise** (edit, adapt, modify) · **Remix** (combine with other material) · **Reuse** (use publicly) · **Redistribute** (share copies). Peer-reviewed citation option: Wiley & Hilton (2018), *Defining OER-Enabled Pedagogy*, IRRODL 19(4) [VERIFY DOI before citing].

Same source, bonus framework — **ALMS** (technical enablers of 5R): Access to editing tools · Level of expertise required · Meaningfully editable · Self-sourced. 5R = the *legal* layer; ALMS = the *technical* layer.

**Curriculum ecology** adds the third layer: the *engineering discipline* that makes exercising Revise/Remix safe over time — sustainability/longevity, not just short-term use:
1. **Locality of edits** — learning-point granularity → updates touch points, not "the curriculum".
2. **Coherence = graph property** — prerequisite concept map (Concepts Atlas; Project 2061 strand-map logic): updating a point triggers downstream-dependent, upstream-prerequisite, and age-placement checks. Gradual progression is a network property, not a list property.
3. **Consistency = schema contract + regression tests** — every update fills the same schema fields; the 9 Sense-B checks + alignment pipeline rerun on each version (CI-for-curricula).
4. **Stability tiering** — mastery tiers (core/working/exposure) double as change-rate tiers: core changes slowly and is carefully versioned; exposure rotates fast to track the field. Decouples "keeping up with AI" from "redesigning the course"; operationalizes the §4 "fixed core + adaptive layer" idea.
5. **Versioning + changelog** — the §3.4 v1→v2 diff, made computable.
6. **Teacher-delta coupling** — every curriculum update is a teacher update (§1): diffs must be legible as *delta training*, not re-learning. Teacher workload is an ecology constraint.

## Instrument inventory (machine-readable, bilingual DE/EN)

| Instrument | File | Grain |
|---|---|---|
| EQuIP v3.1 | `Curriculum analysis/EQuIP review/equip_rubric_structure__validation_required.csv` | 19 criteria, sub-item long format |
| IQOer v17 | `Curriculum analysis/IQOer/iqoer_instrument__validation_required.csv` | 16 scales, 79 items |
| IPN Kriterienkatalog | `Curriculum analysis/IQOer/ipn_kriterienkatalog__validation_required.csv` | 16 criteria, 2 supercategories |
| German standards (Marty) | `Curriculum analysis/German standards/german_standards_marty_curriculum__validation_required.csv` | Bildungsplan items ↔ weeks |
| UNESCO AI CFS blocks | `Curriculum analysis/UNESCO_2024_AI_CFS_competency_blocks__validation_required.csv` | 12 blocks |
| PISA MAIL model | `Curriculum analysis/PISA 2019 MAIL/mail_competence_model__validation_required.csv` | 5 competences |
| AILit framework | `Literature/Literature on AI literacy/AILit_framework_2026__validation_required.csv` | 19 competences × 3 levels |
