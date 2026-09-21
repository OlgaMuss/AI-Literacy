# Literature Review — Evidence Map for the Curriculum Paper

**Status:** `validation_required`. Synthesizes `literature_summaries__validation_required.md` (85 entries, all read in full) into the evidence structure for the paper. Entries are cited as (Author, Year) with the summary-file tag in brackets. Claims marked ⏳ must be re-verified against the primary source before submission (verification protocol in the summaries file header).

The paper's argument in one sentence: *AI/digital-literacy curricula for children are hard to build, hard to analyze, and hard to compare; existing competency frameworks are abstract and age-blind; we contribute (1) a case study with a five-dimension curriculum analysis, (2) evidence of curriculum–assessment misalignment, and (3) the case for concrete learning points + machine-analyzable curriculum representations.*

---

## 1. Frameworks exist — but they are competency-abstract, age-blind, and safeguard-thin

**This is the paper's central critical claim; the corpus supports it from six independent directions.**

| Framework | Structure | Age-specific? | Safeguards/behaviors? | Source |
|---|---|---|---|---|
| UNESCO AI CFS for students (2024) | 4 aspects × 3 levels = 12 competency blocks | **No** — explicitly delegates: "It is up to national or institutional curriculum agencies to define concrete learning objectives for specific student cohorts" (Ch. 4, p. 27) | "Safe and responsible use" block exists but at L2 Apply; no LLM-safeguard mechanics, no anthropomorphism/deception content | [UNESCO-AICFS] ✅ read directly |
| AILit Framework (EC/OECD/Code.org, 2025 draft) | 4 domains × 22 competences ✅ (verified l. 600 of source) | No — spans all of primary+secondary in one band | Thin; feeds PISA 2029 | [02] |
| Long & Magerko (2020) | 17 competencies + 15 design considerations | No — general/adult orientation | Pre-genAI; no interaction safeguards | [01] |
| Ng et al. (2021) | 4 aspects mapped to Bloom | Calls for age-appropriate artifacts but provides none | Ethics as one of four aspects | [08] |
| AI literacy heptagon (Hackl et al., 2026) | 7 dimensions × 4 proficiency levels | Higher-ed only | **Legal/regulatory knowledge in only 2/27 reviewed frameworks** — safeguard content is neglected field-wide | [Heptagon] |
| PISA 2029 MAIL (OECD, 2026 draft) | 5 competences, ethics transversal; difficulty drivers ⏳ | **15-year-olds** — above our cohort | Strong on evaluation; an assessment, not a curriculum | [pisa2029-mail] |
| UNESCO AI CFT (teachers, 2024) | 5 aspects × 3 levels, 16 competencies | Adult (teacher) target | Safeguard content assigned to *teachers*, not learners | batch 1 |

**Supporting evidence for age-blindness:**
- Laupichler et al. (2022, scoping review): little empirical evidence on whether/how AI literacy differs between adults and children; definitions inconsistent [07].
- Yang et al. (2025): the only empirically derived K–12 progression (5 components × grade bands K–3/4–6/7–8/9–12); our 11–12 cohort sits exactly at the 4–6/7–8 boundary; literature base ends March 2024 [Yang-Progression] ⏳ (grade-band table).
- Zhang, Perry & Lee (2025, AI-CI): expert panels judged neural networks and GANs **too complex for grades 6–7** — rare explicit age-appropriateness evidence, adjacent to our band [AI-CI] ⏳.
- Reichert et al. (2023, UNESCO): assessments valid for under-10s are "particularly rare"; AI skills absent from large-scale assessments [UNESCO-DLA].
- AI-CI is the nearest validated instrument (middle school); AICOS is adult-normed (18–74), knowledge-only [AICOS, AI-CI].

**Competency abstraction problem (user's point for intro/skeleton):** all seven frameworks specify *competencies* ("Understand the working principles behind AI") without specifying the underlying knowledge units or depth. None enumerates concrete learning points. This is precisely what our enacted-concept inventory (52 concepts with slide-level evidence) provides — see §7.

---

## 2. Existing curricula/frameworks predate generative AI (user's limitations draft, point 1)

Traceable from the corpus:
- Long & Magerko (2020) — pre-LLM boom [01]; Ng et al. (2021) — pre-genAI [08]; Laupichler et al. (2022) — pre-ChatGPT [07].
- Yang et al. (2025) — review window ends March 2024; most included K–12 curricula predate classroom genAI [Yang-Progression].
- Only the newest frameworks (AILit 2025 [02], PISA MAIL 2026 draft [pisa2029-mail], Heptagon 2026 [Heptagon]) integrate genAI — and they remain non-age-specific (§1).
- User's causal claim ("that is normal since it takes so long to build a curriculum") is supported by curriculum-difficulty/development-time arguments in the curriculum-evaluation literature (CIPP/UbD sources in `curriculum_evaluation_frameworks__validation_required.md`) — pair with Finland's ~10-year national curriculum cycle [23] as the timescale anchor.
- ⏳ TODO for this section: for each major curriculum (DAILy/MIT, aiEDU, Day of AI, AI4GA), verify its publication date and genAI coverage before listing it as "too old" — use R9-1/R9-2 only as discovery maps (batch 9 audit).

---

## 3. Safeguards and interaction behaviors: the missing content, and why it matters

**Youth-specific harms are real and under-mitigated:**
- YouthSafe (Yu et al., 2025): mainstream moderation systems reach only F1 0.09–0.73 on youth risks, with 57–100% false-negative rates on developmental harm/undue influence/emotional overreliance; 12,449-snippet youth-risk benchmark [youthsafe] ⏳.
- Tandar et al. (2024): Snapchat's My AI gave harmful diet/mental-health advice to adolescents [snapchat-myai-misinformation].
- SAFE AI Companions pre-reading (Meta leak, Adam Raine case, companion-attachment studies) — orientation only; **verify against primaries before any citation** [note-safe-companions].
- UNICEF (2025): ten child-centred AI requirements incl. AI-companion and CSAM risks; AI literacy as a *rights* obligation [unicef-ai-children].

**Technical reality: safeguards are imperfect and layered — exactly what our W6–W7 teach:**
- Training-time: Constitutional AI (Bai et al., 2022) incl. an explicit child age-appropriateness principle (App. C.1) ⏳ [constitutional-ai]; Sparrow's 23 rules incl. "do not pretend to have a body/feelings" with the rationale "anthropomorphising systems can lead to overreliance" (Table 14) ⏳ [sparrow].
- Prompt/generation-time: Tamkin et al. (2023) — "do not discriminate" prompting collapses measured bias near zero [discrim-eval]; LMQL constrained decoding [lmql]; Streaming-VR layered verification [streaming-vr].
- Failure modes: output-constraint attacks bypass guardrails at 96.2% ASR (⏳ preprint) [output-constraints-attack]; self-consistent errors — consistency ≠ correctness [self-consistent-errors]; LLMs detect LLM errors at very low recall vs. humans [realmistake]; self-correction without external feedback ≈ worthless [critic].
- Gabriel (2020) provides the philosophical warrant (whose values? alignment as political) [gabriel-alignment].

**Why *taught* behaviors, not just built-in guards:** MaC13 intervention changed beliefs but not sharing behavior [MaC13-Disinformation]; PRAISE (HRI 2026 submission): 10–16yos' AI knowledge rises with age but safety ambivalence is **stable** — knowledge alone doesn't fix safety beliefs (misconception: emotional bond ⇒ data privacy) [PRAISE2026-safety] ⏳ preprint.

---

## 4. Assessment: self-report ≠ performance (justifies our objective battery — and our misalignment finding)

- Lintner (2024, npj Sci. Learn.): only 3 of 16 validated AI-literacy scales are performance-based — via R9-4 ⏳ verify in original.
- Abdelghani et al. (2025): middle-schoolers' self-reported AI expertise correlated *negatively* with performance — via R9-4 ⏳.
- Clerc et al. (2026, AIED): 2-hour workshop improved *behavioral* regulation of LLM use (51.5% vs 66.7% acceptance of underspecified prompts; follow-up questions 59.2% vs 27.9%) while GenAI self-reports (r = 0.01) and metacognition (r = 0.04) did not predict performance [aied26-intervention].
- MAILS ↔ objective test: r = .21 [MAILS-SV]; subjective–objective AI literacy r ≈ .04 [AICOS] ⏳.
- Reichert et al. (2023): self-reports systematically inaccurate (males over-report) [UNESCO-DLA].
- PISA 2029 MAIL: performance-based authentic tasks, difficulty drivers (context complexity, open-endedness, scaffolding, authenticity) — benchmark for our Assessment dimension [pisa2029-mail] ⏳.
- AIED26 supplement: validated LLM-as-judge protocol + honest reliability reporting (α as low as .26 for some self-report subscales) — methodological template [aied26-supplement].

---

## 5. Pedagogy & didactics: hands-on, experience-first, transparency — supported

- Hitron et al. (2019): 10–13yos understand ML only when **both** data labeling and evaluation are hands-on; partial uncovering = no learning; N = 30, M = 11.59y — our exact band [Hitron-BlackBoxes].
- van Straten et al. (2023): robot stating "I'm a machine, I don't feel" sharply reduces anthropomorphism in 8–10yos (η² = .43 ⏳) with only small drops in closeness/trust — transparency works *through the robot* [vanStraten2023-transparent]. Direct license for our "AI cannot feel" content (W6_08).
- Tarakli et al. (2025): learning-by-teaching a peer-like robot beats tablet practice for retention; low-prior-knowledge children benefit most [Tarakli2025-lbt] ⏳ preprint.
- Wang et al. (2024, TPCK review of 92 studies): robot-education evaluation is cognitive-biased (40% cognitive vs 22% affective outcomes); catalogs novelty effect, teacher workload — mirrors our misalignment finding [wang-2024-robots-tpck].
- Meyer et al. (2021): 58% of top "educational" apps score low on the Four Pillars; 87% fail social interaction — argument for a physical co-play robot over screen media [27].
- Heeg & Avraamidou (2025): Dutch 11–12yos conceptualize AI through personal experience and readily engage ethics — supports **experience-first ordering** (user's limitations draft, point 3) [03].
- Baumann et al. (2023): by age 5, children learn from a competent robot while knowing it's mechanical — "machine but useful" is developmentally available [Baumann2023-trust].
- Attachment measures interpretation: Rabb et al. (2022) — what builders feel is "weak attachment"; Huang et al. (2013) — affection for self-built robots is effort-driven, not psychological attachment [Rabb2022-framework, Huang2013-lego].
- van den Berghe et al. (2021): after 7 sessions children shift to "mechanical being with cognitive states" — beliefs evolve with exposure [vandenBerghe2021-toyfriend].
- HDR 2025 calculator analogy: chatbots help only *after* foundational skills exist; cognitive offloading reduces retention (pp. 72–74) ⏳ — supports sequencing fundamentals before tool use (nuance on user's point 3: experience-first for *what AI does*, but foundational judgment before *delegation*) [hdr-2025].
- GEM 2023: OLPC Peru (>1M laptops) → zero learning impact; edtech effects small and context-bound — didactics/context must lead design [24].

---

## 6. Curriculum evaluation & reporting standards (our framework contribution)

- EQuIP Rubric v3.1 (Achieve, 2021): criterion–evidence–reasoning forms, 0–3 category ratings, dedicated "Monitoring Student Progress" category, Category-I-non-negotiable gating — the closest operational template for our proposed reporting standard [equip-science].
- ISEE WG2 Ch. 9: measurement-driven regimes narrow curricula — external support for our misalignment thesis ⏳ [isee-wg2]; WG1 Ch. 4: six-domain curricular framework incl. technology domain [isee-wg1]; WG4: EBE³ evidence-grading + effect-size/uncertainty reporting standards [isee-wg4].
- Finland 2014: seven transversal competences incl. ICT; assessment "to promote learning", not ranking; ~10-year revision cycle [23].
- IBE/UNESCO-IBE curriculum-problem list (outdated content, weak curriculum–pedagogy–assessment alignment, insufficient design capacity) — from `New ideas.md`; ⏳ source: UNESCO-IBE "Curriculum Matters" PDF (not in Literature/ — acquire or cite from New ideas notes).

---

## 7. What the corpus does NOT contain (our novelty)

1. No framework or curriculum enumerates **concrete learning points with specified depth** for AI literacy — all operate at competency level (§1). Our 52-concept enacted inventory with mastery roles (core/working/exposure) is, to our knowledge, unique in this corpus.
2. **No performance-based AI-literacy instrument validated for ages 6–11** (R9-4, HIGH-reliability secondary source; ⏳ verify the COSMIN gap claims).
3. No curriculum–assessment alignment analysis at concept level for an enacted AI-literacy curriculum (AI-CI/DAILy co-development comes closest but was designed together, not audited).
4. Little on teaching **LLM safeguard mechanics** (training-time vs prompt-time) to children — YouthSafe/Sparrow/CAI are technical; curricula covering them are absent from the corpus.
5. User's misconception check (limitations draft, point 5): **prediction-as-oracle** — the closest corpus items are AI-CI's documented misconceptions (AI = automation/algorithms) [AI-CI] and PRAISE's safety misconceptions [PRAISE2026-safety]; *no curriculum in the corpus explicitly teaches "predictions are forecasts, not oracles"* — a genuine novelty claim, but ⏳ strengthen by checking DAILy/aiEDU/Day of AI directly before asserting it in print.
6. User's point 4 ("AI vs non-AI distinction is irrelevant; what matters is machines-you-can-talk-to and data") — partially supported: AI-CI documents children confusing AI with automation [AI-CI]; no corpus source makes the stronger claim that the distinction is *pedagogically counterproductive*. Frame as our design reflection, not as literature consensus.

---

## 8. Paper-section → citation map (for the skeleton)

| Paper section | Key citations |
|---|---|
| Intro: frameworks abstract & age-blind | UNESCO 2024 [AICFS]; EC/OECD 2025 [02]; Long & Magerko 2020 [01]; Laupichler 2022 [07]; Hackl 2026 [Heptagon] |
| Intro: why safeguards/behaviors | Yu 2025 [youthsafe]; UNICEF 2025 [unicef]; Tandar 2024 [snapchat]; UNDP 2025 [hdr] |
| Intro: learning points vs competencies | (our argument; contrast all §1 frameworks) |
| Case: curriculum description | (our data) + Kurian 2025 [11], CIFAR 2024 [13] for design principles |
| Findings: misalignment | our analysis + Clerc 2026 [aied26]; Lintner 2024 ⏳; Abdelghani 2025 ⏳; Wang 2024 (evaluation bias) |
| Findings: mastery/chance-level | our notebook analysis + AI-CI pre/post gains [AI-CI] as contrast |
| Framework: 5 dimensions | EQuIP [equip-science]; ISEE WG1/WG2/WG4; Finland [23]; GEM 2023 [24] |
| Framework: UNESCO mapping | [AICFS] + Yang 2025 [Yang-Progression] grade bands |
| Discussion: generation tool | Córdova-Esparza 2025 [educ-agents] (hybrid human-AI outperforms autonomous); Pan 2024 [self-correction-survey] |
| Discussion: robot pedagogy | Hitron 2019; van Straten 2023; Tarakli 2025; Baumann 2023; van den Berghe 2021 |

## 9. Verification queue before submission (all ⏳ above)

AICOS r = .04 · YouthSafe F1 ranges & 57–100% FNR · PISA MAIL five-competence model & difficulty drivers (pp. 25, 44–45) · van Straten η² = .43 · Constitutional AI child-age principle (App. C.1) · Sparrow anthropomorphism rules (Table 14) · CDA 96.2% ASR · HDR calculator analogy (pp. 72–74) · Yang grade-band table · AI-CI "too complex" panel judgment · Lintner 3/16 · Abdelghani negative correlation · ISEE chapter claims (WG1 Ch. 4, WG2 Ch. 9) · HDR PISA-2022 >3× trust figure (p. 180).
