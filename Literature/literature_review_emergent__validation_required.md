# Literature Review — Bottom-Up: Emergent Elements

**Status:** `validation_required`. Companion to `literature_review__validation_required.md` (which is top-down: organized around our claims). This file works **inductively**: starting from the 85 per-paper summaries (`literature_summaries__validation_required.md`) and asking *what is in this corpus that our current argument does not yet use?* Each theme states what the corpus says, why it is easy to miss, and what it changes for our paper. ⏳ = verify against the primary source before citing.

---

## A. Emergent themes — what we might have missed

### A1. Calibrated trust — not debunking — is the learning target (anthropomorphism cluster)
**Corpus:** Baumann et al. (2023) show children by age ~5 decouple epistemic trust from animacy — a robot can be judged a "machine" yet remain a credible informant [batch 8]. Hitron et al. (2019) show unpredictability *causes* anthropomorphic attribution. Van Straten et al. (2023) show transparency about machine-likeness mediates trust dynamics (η² ≈ .43 ⏳) — and that transparency can be delivered *by the robot itself*. Huang et al. (2025, long-term) show interaction histories shift beliefs toward instrumentality.
**Why missed:** our top-down reading framed anthropomorphism as a misconception to correct (W6_08: "AI cannot feel"). The corpus instead suggests the harder, more useful target is **calibrated reliance** — knowing when to trust output — and that some anthropomorphic framing is developmentally normal and even functional.
**What it changes:** (i) v2 learning-point candidate: "trust is about reliability, not feelings"; (ii) didactic channel: Marty can *voice* its own machine-disclaimer (transparency through the artifact, not just the slide); (iii) interpretation of our anthropomorphism scale: movement toward "machine" labels is not necessarily the success signal — calibrated reliance is.

### A2. What we call "attachment" may be effort and engagement (measurement cluster)
**Corpus:** Rabb et al. (2022): children who *built* robots show affection driven by effort invested (IKEA-effect-like), distinct from attachment; Abdelghani et al. (2025, SCA work ⏳): self-report attachment instruments fail with children — behavioral observation needed.
**Why missed:** our attachment/robot-perception measures (SOAS, attachment items) were adopted as instruments, not interrogated as constructs.
**What it changes:** Build-group "attachment" differences may index effort, not bonding — a confound for the Build-vs-Control comparison; state as limitation; consider behavioral proxies in v2.

### A3. LLM-safety failure modes are teachable content — and the corpus enumerates them
**Corpus (batch 7):** self-consistent errors — an LLM repeating the same answer confidently can still be systematically wrong (Tan et al., 2025); over-correction — verification attempts degrade already-correct answers (Streaming-VR; CRITIC: 14.3% wrong corrections ⏳); role-play false positives — safeguards over-flag children's creative/role-play prompts (Youth AI Risk Taxonomy ⏳); prompt-time safeguards are bypassable (Duan et al.; Sapphire); sampling ≠ safety (BRET: paraphrase attacks); alignment tax — safer models sometimes rated less helpful (Sparrow).
**Why missed:** our top-down lens asked "do curricula cover safeguards?" — the corpus answers a different, richer question: "which *specific* failure modes are documented?"
**What it changes:** three are already in our curriculum as learning points (confidence ≠ correctness appears in our intro examples; W6_09 covers training-time vs. prompt-time safeguards; W7_03 implicitly acknowledges bypassability by moving instructions to background code). **Two are not taught and are v2 candidates:** (i) "verification can make correct things worse — don't fix what isn't wrong"; (ii) "safeguards also err in the safe direction (false positives) — a refused prompt is not proof of danger."

### A4. Assessment engineering is the corpus's most actionable methodological cluster
**Corpus:** AI-CI (Zhang et al., 2025) builds items *from documented misconceptions* via cognitive interviews — 8–22 items per construct [batch 2/5]. Reichert et al. (UNESCO DLA ⏳): digital literacy is empirically near-**unidimensional** despite multidimensional theory. Multiple sources document weak/negative subjective–objective correspondence in children (MAILS-type self-report vs. knowledge).
**Why missed:** we treated our battery as an instrument to report, not as a design object.
**What it changes:** (i) v2 battery method: distractor-driven item generation from *our documented* misconceptions + cognitive interviews; (ii) testable prediction: our 23 items should load on ~one dominant factor (check in the notebook); (iii) the MAILS × knowledge analysis (notebook §6) now has a literature-grounded expected null/negative — a *finding*, not a failure.

### A5. PISA 2029 MAIL's difficulty drivers double as a difficulty metric for learning points
**Corpus:** the MAIL draft defines difficulty drivers (context complexity, scaffolding amount, number of operations…) for assessment items [batch 5].
**Why missed:** we read PISA as a benchmark to cite, not as a vocabulary to reuse.
**What it changes:** our Didactics dimension can adopt these drivers as per-learning-point difficulty ratings — making "too advanced for the age group" *computable* rather than asserted. Also: MAIL targets 15-year-olds → our 13–14 target sits just below the benchmark, strengthening the age-gap argument.

### A6. Engagement is not learning — and the corpus says platforms know it
**Corpus:** everyone.ai materials: gamified engagement metrics optimize for retention, not learning, and can undermine intrinsic motivation [batch 5].
**Why missed:** our weekly engagement pulses (teacher-rated + IMI) were collected as if they proxy learning.
**What it changes:** for the affective cross-analysis, *expect decoupling*: engagement can stay high while knowledge stays at chance. Reported jointly, this is a strength (multi-dimensional outcomes); conflated, it's the field's known bias (Wang et al., 2024: cognitive outcomes dominate evaluations).

### A7. Motivation-by-jobs is empirically weak rhetoric
**Corpus:** GEM 2023 report: AI-complementary skills appear in <1% of job ads ⏳ [batch 1].
**Why missed:** "future workforce" is the default policy framing (and partly our intro's framing).
**What it changes:** citizenship/safety framing has better evidentiary footing than labor-market framing; one clause in the intro should be enough.

### A8. Governance findings support the continuous-update argument
**Corpus:** Finland's ~10-year reform cycle + assessment "to promote learning, not rank" (Vahtivuori-Hänninen et al., 2014); CPS guidebook on *quarterly* revision with an age-access table (Chicago Public Schools, 2025); Colorado AI Act classifies education as a high-risk AI domain ⏳ [batch 1/5].
**Why missed:** read as context, not as evidence.
**What it changes:** the intro's temporal-pressure paragraph gains: (i) a governance counter-model (quarterly cycles exist!), (ii) a regulatory hook (education = legally high-risk), (iii) the assessment-philosophy contrast (Finland) that aligns with our formative-alignment argument.

### A9. The teacher dimension is where policy already moved
**Corpus:** UNESCO AI CFT (2024b) assigns safeguard content to *teachers*, not learners [batch 1]; Wang et al. (2024) document teacher workload as a binding constraint in hands-on AI education; CPS institutionalizes teacher-facing guidance with versioned updates.
**Why missed:** our framework treated teacher variables as background context.
**What it changes:** supports the skeleton's new teacher-in-Context move (readiness, workload, training) *and* the intro's "every curriculum update is a teacher update" claim — now with corpus backing, and our weekly teacher pulse becomes an instrument others lack.

### A10. Curriculum theory already has language for our position
**Corpus:** ISEE Working Group 2, Ch. 8: curriculum as "complicated conversation" (Pinar), Schwab's practical arts, warning against measurement narrowing the curriculum [batch 9].
**Why missed:** read as background theory, not as quotable anchors.
**What it changes:** gives the Discussion its intellectual home: learning points are a *reporting* unit (not a pedagogy), and the standard must describe rather than prescribe — pre-empting the "you reduce curriculum to a checklist" critique with the field's own words.

---

## B. Does any paper discuss "reinventing the wheel" or analyze how curricula are developed?

**No.** A targeted search of the full corpus (85 sources; terms: reinvent / wheel / from scratch / reuse / development process / how curricula are developed) found **no empirical study of the AI-literacy curriculum *development process*** — who builds them, how long it takes, what gets reused, why reuse fails. Closest neighbors, none of which analyze the process:
- Overdeck et al. (2024): *observes* fragmentation ("no coherent K–12 pathway") without studying its production [batch 3].
- aiEDU blueprint / GEM reports: policy advocacy, not process analysis [batch 1].
- Vahtivuori-Hänninen et al. (2014): describes Finland's *national* reform process (macro), not curriculum-team practice (micro).
- CPS guidebook: a governance artifact (district-level process), not a study of one.
- ISEE WG2 Ch. 8: curriculum *theory*, no empirical development-process work.

**Implication for the paper (safe formulation):** *"In a corpus of 85 sources spanning AI-literacy frameworks, curricula, assessments, LLM safety, and social robotics, we found no empirical analysis of how AI-literacy curricula are actually developed or why reuse between teams fails. Curriculum development practice remains a black box; we call for research that studies it directly."* — frame as corpus-bounded ("to our knowledge"), and it doubles as the motivation for our Part 1 case study and a future-research call in the Discussion. ⏳ Before submission: run one systematic database query (Scopus/WoS) to harden the claim beyond our corpus.

---

## C. Priority re-read list (for the author)

Ranked by load-bearing weight for the current argument; "look for" = what to extract on re-read.

1. **Yang et al. (2025, K–12 AI learning progression, C&E)** — closest existing attempt at age-banded AI content; our age-specificity critique must engage it head-on. *Look for:* their band boundaries, evidence basis, whether depth is specified.
2. **Zhang et al. (2025, AI-CI)** — the assessment-engineering model for our v2 battery. *Look for:* item-generation procedure from misconceptions, cognitive-interview protocol, items-per-construct ratios.
3. **Clerc et al. (AIED26) + supplementary appendix** — our own intervention paper; consistency of instruments, constructs, framing. *Look for:* what was promised vs. what this paper must not contradict.
4. **Van Straten et al. (2023)** — transparency–trust mediation; the "robot voices its own disclaimer" didactic channel. *Look for:* exact mediation stats (η² pending), age of sample, manipulation.
5. **Long & Magerko (2020)** — the field-defining competency list we position against. *Look for:* exact wording of the 17 competencies + design considerations (they are more nuanced than secondary citations suggest).
6. **PISA 2029 MAIL draft (OECD, 2026)** — assessment benchmark + reusable difficulty drivers. *Look for:* the driver list, transversal-ethics operationalization.
7. **EQuIP rubric (NextGenScience, 2023)** — closest relative to our reporting standard. *Look for:* its rating categories — our delta (computability, longitudinal diffing) must be stated precisely against them.
8. **Hackl et al. (2026, heptagon)** — the 2/27 legal-content finding anchors our "safeguards beyond frameworks" claim. *Look for:* their 27-framework list (does it include UNESCO AI CFS?) and exact coding.
9. **Hitron et al. (2019) + Rabb et al. (2022) + Huang et al. (2025)** — the anthropomorphism/attachment/effort cluster behind A1–A2. *Look for:* measures used, age ranges, what "attachment" operationally was.
10. **Youth AI Risk Taxonomy (YouthSafe)** — child-specific failure modes incl. role-play false positives. *Look for:* the taxonomy levels; whether any map to content we teach (W6_09–10) or miss.

*Also valuable but lower priority:* Baumann et al. (2023, calibrated trust), ISEE WG2 Ch. 8 (theory anchors), UNESCO AI CFT 2024b (teacher dimension), Wang et al. (2024, workload + cognitive-over-affective bias).
