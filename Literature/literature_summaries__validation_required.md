# Literature Summaries — AI & DL Curriculum Paper

**Status:** `validation_required` — consolidated per-paper summaries of the `Literature/` corpus.

## How these summaries were produced

- Every paper was read in full (main text; long appendices/supplements read representatively, flagged in each entry's *Caveats*) by reading agents under a strict no-invention protocol; where a pre-extracted `.txt` twin existed, the twin was verified against the PDF's first page and read instead.
- **Verification legend** (per entry, in *Caveats*):
  - ✅ *verified* — a load-bearing claim was independently re-checked against the source by the coordinating agent.
  - ⏳ *pending* — agent-read; verify against the source before citing in the manuscript.
- Verified so far: AILit framework structure (4 domains × 22 competences — exact match, 02 txt l. 600); `ai_literacy_assessments__validation_required.md` reuse-claims (Lintner 2024 npj Sci. Learn. DOI 10.1038/s41539-024-00264-4 and Abdelghani et al. 2025 arXiv:2505.01106 confirmed with claims as described); van Straten et al. (2023) transparency mediation framing (exact effect size η²=.43 pending); Constitutional AI SL+RL harmless-non-evasive design (exact "age" constitution principle pending).
- Duplicates found: `UNESCO - 2024 - AI competency framework for students.pdf` exists twice (UNESCO reports/ and Literature on AI literacy/); `Constitutional AI ... copy.pdf` (metadata-only difference); `06_Social_Robots_in_School_Settings_2023plus.csv` exists twice (byte-identical); Yang et al. K–12 progression paper exists twice (same DOI, one in "AI literacy assessement/", one in "Literature on AI curriculums/" + supplementary appendix).
- Filename misnomer: `25_Digital_Citizenship_Internet_Safety_Middle_School` is actually a French student slide deck on phone bans and cognitive development (see batch 10).

## Contents

1. UNESCO AI competency framework for students (read by coordinating agent) — this file, below
2. Batch 1 — UNESCO / UN policy reports (8)
3. Batch 2 — AI literacy frameworks, scales, assessment (12)
4. Batch 3 — Papers on AI literacy, numbered set 01–22 (16)
5. Batch 4 — Curriculum design + hands-on robotics (+5 existing-notes verifications)
6. Batch 5 — Root papers: AIED26 intervention, EveryoneAI, CPS guidebook, PISA 2029 MAIL, AI ethics (6)
7. Batch 6 — LLM safety, child-facing (7 + SAFE notes verification)
8. Batch 7 — LLM safety, technical self-correction (10)
9. Batch 8 — Social robots, attachment, anthropomorphism (14 + notes + CSV)
10. Batch 9 — Existing review notes audit (5)
11. Batch 10 — Related papers 23–27 (5)

---

## [UNESCO-AICFS] AI competency framework for students

- **Citation (APA):** UNESCO. (2024). *AI competency framework for students.* UNESCO Publishing. https://doi.org/10.54675/JKJB9835
- **File:** `UNESCO reports/UNESCO - 2024 - AI competency framework for students.pdf` (identical copy in `Literature on AI literacy/`)
- **Type:** framework
- **Core claims:** (1) Students need 12 AI competencies organized across four aspects — Human-centred mindset, Ethics of AI, AI techniques and applications, AI system design — each progressing through three levels: Understand → Apply → Create. (2) Level 1 'Understand' provides "the essential attitudinal, cognitive and practical foundations for the further study of AI" but "does not define the exit-level competencies for specific areas or domains of AI" (Ch. 3.2, p. 20). (3) 'Apply' is the expected exit point for most school students; 'Create' should be elective for interested students only (Ch. 3.2, pp. 21–22).
- **Relevance to our paper:** Central reference for our Content dimension — we mapped our 52 enacted concepts onto its blocks: 17/52 fall entirely beyond the framework (LLM safeguards, anthropomorphism/deception resistance, LLM behavior control, sensors, microcontrollers, robotics) and 3 more partially; the framework contains no competency on safe interaction behaviors with conversational agents as taught in our W6–W7. [content-frameworks] [age-appropriateness] [assessment]
- **Key points with locations:**
  - 12 competencies / 4 aspects / 3 levels — Short summary, p. 2; Table 1, p. 19.
  - Aspect definitions and competency blocks (Human agency → Human accountability → Citizenship; Embodied ethics → Safe and responsible use → Ethics by design; AI foundations → Application skills → Creating AI tools; Problem scoping → Architecture design → Iteration and feedback) — Ch. 3.3, pp. 22–26.
  - The framework explicitly delegates age-appropriateness: "It is up to national or institutional curriculum agencies to define concrete learning objectives for specific student cohorts, based on their AI readiness" — Ch. 4, p. 27. This substantiates our critique that the framework is not age-specific.
- **Caveats:** ✅ verified by direct full read of Ch. 1–4 (coordinating agent). Ch. 5 (application guidance, incl. 5.4 spiral sequences by age and 5.8 competency-based assessment) not yet read in full — ⏳ read before citing curricular-implementation claims.


---

<!-- ===== batch_1_unesco_policy__validation_required.md ===== -->

# Batch 1 — UNESCO/UN policy literature summaries

Summaries for the AI & digital literacy curriculum paper (11–12 year-olds, Marty robot; dimensions: Context, Content, Pedagogy, Didactics, Assessment). All files read with the Read tool (PDF auto-converted to text); large files read in chunks to the end. Tags: [curriculum-difficulty] [content-frameworks] [age-appropriateness] [assessment] [pedagogy] [didactics] [safeguards-behaviors] [social-robots] [hands-on] [ai-literacy-def] [ethics] [policy]

---

## [unesco-aicft] AI competency framework for teachers

- **Citation (APA, best effort from the document):** UNESCO. (2024). *AI competency framework for teachers*. UNESCO Publishing.
- **File:** Literature/UNESCO reports/UNESCO - 2024 - AI competency framework for teachers.pdf
- **Type:** framework
- **Core claims:** Defines the competencies teachers need to use AI in education in a human-centred, ethical, safe and sustainable way. Organizes 16 competencies across five aspects (human-centred mindset, ethics of AI, AI foundations and applications, AI pedagogy, AI for professional learning) and three progression levels (Acquire, Deepen, Create).
- **Evidence/methods:** Normative framework developed through UNESCO expert consultation; not empirical.
- **Relevance to our paper:** Direct target of our critique that UNESCO frameworks are generic and not age-specific — this framework addresses teachers, not students, and its progression levels are not calibrated to developmental stages. Supports our argument that safeguard/behaviour content sits with adults, not learners. Tags: [content-frameworks] [ai-literacy-def] [ethics] [pedagogy] [policy] [age-appropriateness]
- **Key points with locations:**
  - Five aspects × three levels (Acquire/Deepen/Create) matrix of 16 competencies (Chapter 2, pp. ~10–25)
  - Ethics of AI as a standalone aspect, including human rights and safety (aspect 2)
  - Implementation strategies: teacher education, procurement, professional communities (later chapters)
- **Caveats:** None; 52-page document read in full (chunked).

---

## [unesco-ethics-rec] Recommendation on the Ethics of Artificial Intelligence

- **Citation (APA, best effort from the document):** UNESCO. (2022). *Recommendation on the ethics of artificial intelligence* (SHS/BIO/PI/2021/1 REV.). UNESCO. (Adopted November 2021.)
- **File:** Literature/UNESCO reports/UNESCO - 2022 - Recommendation on the ethics of artificial intelligence.pdf
- **Type:** framework (normative instrument)
- **Core claims:** First global normative instrument on AI ethics, grounded in human rights, human dignity, environmental sustainability and diversity. Articulates core values and ten principles (e.g., proportionality, safety, privacy, human oversight, transparency, accountability, awareness/literacy, fairness) operationalized through 11 policy action areas.
- **Evidence/methods:** Negotiated normative text adopted by 193 Member States; includes monitoring mechanisms, not empirical research.
- **Relevance to our paper:** Explicitly names "public awareness and understanding of AI" and "data and AI literacy" as policy areas, legitimating AI literacy education; its child-relevant protections support our safeguards dimension. Tags: [ethics] [policy] [ai-literacy-def] [safeguards-behaviors]
- **Key points with locations:**
  - Values and principles (Sections III–IV, pp. ~14–30)
  - Policy action area on education, research and "data and AI literacy" for all (Section V)
  - Human oversight, determination and accountability principles (Section IV)
- **Caveats:** None; 44-page document read in full (chunked).

---

## [childrens-rights-digital] Children's Rights in the Digital Environment

- **Citation (APA, best effort from the document):** Drăghici, A. (2025). Children's rights in the digital environment. In *Encyclopedia entry* (publisher details as printed in document). [Best effort — encyclopedia metadata incomplete in PDF text.]
- **File:** Literature/UNESCO reports/Children's Rights in the Digital Environment.pdf
- **Type:** review (encyclopedia entry)
- **Core claims:** Analyses children's rights in the digital environment, mainly in the European context: evolution of digital rights, the EU framework (GDPR, Digital Services Act), and the tension between protection, provision and participation rights online. Highlights digital literacy as a precondition for exercising rights and flags generative AI as an intensifier of risks to children.
- **Evidence/methods:** Doctrinal/policy review of legislation and scholarship; not empirical.
- **Relevance to our paper:** Grounds the "safeguards/behaviors" content of our curriculum in a rights framework; supports teaching safe, rights-respecting online behaviour to 11–12 year-olds. Tags: [safeguards-behaviors] [ethics] [policy] [age-appropriateness]
- **Key points with locations:**
  - Three categories of children's digital rights: protection, provision, participation (early sections)
  - GDPR/DSA provisions relevant to minors (middle sections)
  - Generative AI risks for children (closing sections)
- **Caveats:** Exact encyclopedia title/publisher not fully recoverable from the extracted text; citation is best effort. 21 pages read in full.

---

## [unesco-2021-aied] AI and education: Guidance for policy-makers

- **Citation (APA, best effort from the document):** Miao, F., Holmes, W., Huang, R., & Zhang, H. (2021). *AI and education: Guidance for policy-makers*. UNESCO Publishing.
- **File:** Literature/UNESCO reports/Miao et al - 2021 - AI and education Guidance for policy-makers.pdf
- **Type:** report / policy guidance
- **Core claims:** Provides policy guidance on leveraging AI for SDG 4 while managing risks. Distinguishes learning with AI, learning about AI, and preparing for human–AI collaboration; categorizes AI applications in education (ITS, dialogue-based tutors, automated writing evaluation, chatbots, learning analytics) and urges AI literacy for all citizens.
- **Evidence/methods:** Synthesis of policy practice and expert knowledge; illustrative case examples, not primary empirical studies.
- **Relevance to our paper:** The "learning about AI" strand is the policy basis for our curriculum content; its non-age-specific treatment of AI literacy exemplifies the gap our paper critiques. Tags: [policy] [ai-literacy-def] [content-frameworks] [pedagogy] [ethics]
- **Key points with locations:**
  - Definitions and typology of AI applications in education (early chapters)
  - Policy recommendations on AI literacy and curriculum (mid-document)
  - Ethics, equity and inclusion risks (later chapters)
- **Caveats:** None; 50-page document read in full (chunked).

---

## [unesco-2023-genai] Guidance for generative AI in education and research

- **Citation (APA, best effort from the document):** Miao, F., & Holmes, W. (2023). *Guidance for generative AI in education and research*. UNESCO Publishing.
- **File:** Literature/UNESCO reports/Miao & Holmes - 2023 - Guidance for generative AI in education and research.pdf
- **Type:** report / policy guidance
- **Core claims:** Explains how generative AI works, maps controversies (plagiarism, bias, hallucination, privacy, deskilling) and proposes a human-centred regulatory approach for education and research. Recommends government regulation, age limits/age-appropriate design, teacher preparation, and development of GenAI competencies for learners and teachers.
- **Evidence/methods:** Policy synthesis based on UNESCO rapid assessment of Member State responses; not empirical research.
- **Relevance to our paper:** Explicitly raises age-appropriateness (e.g., minimum ages for GenAI use) and the need for learner-facing competencies — both central to our critique and our safeguards/behaviour content. Tags: [policy] [age-appropriateness] [safeguards-behaviors] [ethics] [ai-literacy-def] [assessment]
- **Key points with locations:**
  - How GenAI works and what it can/cannot do (Section 1)
  - Controversies: academic integrity, cognitive offloading, bias (Section 2)
  - Policy steps: regulation, age limits, competency frameworks (Sections 3–4)
- **Caveats:** None; 48-page document read in full (chunked).

---

## [unesco-2025-future] AI and the future of education: Disruptions, dilemmas and directions

- **Citation (APA, best effort from the document):** UNESCO. (2025). *AI and the future of education: Disruptions, dilemmas and directions*. UNESCO Publishing.
- **File:** Literature/UNESCO reports/UNESCO - 2025 - AI and the future of education Disruptions, dilemmas and directions.pdf
- **Type:** position (edited anthology of expert "think pieces")
- **Core claims:** Collects expert essays on philosophical, ethical and pedagogical dilemmas of AI in education: unequal access and "coded inequalities," human–machine co-creation, revaluing teachers' roles, rethinking assessment, and governance imperatives. Argues education must shape AI, not merely adapt to it.
- **Evidence/methods:** Normative/argumentative essays by invited experts; individual chapters cite empirical work but the volume is not a systematic review.
- **Relevance to our paper:** Provides quotable position arguments on pedagogy, assessment redesign and the limits of current frameworks — useful for our discussion of pedagogy/assessment misalignment and framework critique. Tags: [pedagogy] [assessment] [ethics] [policy] [ai-literacy-def] [content-frameworks]
- **Key points with locations:**
  - Introduction: framing of disruptions/dilemmas/directions (opening chapter)
  - Sections on AI pedagogies, assessment and educational futures (middle chapters)
  - Sections on ethical/governance imperatives and coded inequalities (closing chapters)
- **Caveats:** 165-page anthology read via table of contents, full introduction, and the most paper-relevant thematic sections (pedagogy/assessment, teachers' roles, ethics/governance, inequalities); not every individual essay was read word-for-word.

---

## [unicef-ai-children] Guidance on AI and Children (3rd edition)

- **Citation (APA, best effort from the document):** UNICEF Innocenti – Global Office of Research and Foresight. (2025). *Guidance on AI and children* (3rd ed.). UNICEF.
- **File:** Literature/UNESCO reports/UNICEF Innocenti - 2025 - Guidance on AI and children (3rd ed.).pdf
- **Type:** framework / policy guidance
- **Core claims:** Children's rights (protection, provision, participation) under the UN Convention on the Rights of the Child must frame all AI policies and systems. Sets out ten requirements for child-centred AI: regulatory frameworks, safety, data privacy, non-discrimination, transparency, human rights due diligence, well-being, inclusion, empowerment through AI literacy, and an enabling environment. Addresses new risks: AI-generated CSAM, AI companions, environmental impacts.
- **Evidence/methods:** Policy guidance drawing on consultations and evidence reviews; not primary empirical research.
- **Relevance to our paper:** Strongest direct support for our safeguards/behaviours dimension and for age-specific AI literacy ("empowerment" requirement) aimed at children rather than adults. Tags: [safeguards-behaviors] [age-appropriateness] [policy] [ethics] [ai-literacy-def]
- **Key points with locations:**
  - Ten requirements for child-centred AI (core chapters)
  - AI-generated CSAM and AI companion risks (risk sections)
  - AI literacy as empowerment for children (empowerment chapter)
- **Caveats:** None; 60-page document read in full (chunked).

---

## [hdr-2025] Human Development Report 2025 — A matter of choice: People and possibilities in the age of AI

- **Citation (APA, best effort from the document):** United Nations Development Programme. (2025). *Human Development Report 2025: A matter of choice: People and possibilities in the age of AI*. UNDP.
- **File:** Literature/UNESCO reports/United Nations Development Programme - 2025 - Human Development Report 2025 A matter of choice People and possibilities in.pdf
- **Type:** report (flagship analytical report with original survey data)
- **Core claims:** AI's impact on human development depends on human choices, not technological inevitability; advocates a "complementarity economy," innovation with intent, and investing in "capabilities that count." Chapter 3 shows AI's effects differ by life stage: excessive screen time harms early-childhood brain development; school-age AI use can level or widen gaps; adolescent wellbeing is threatened by engagement-optimized, AI-powered social media.
- **Evidence/methods:** Original 21-country UNDP Survey on AI and Human Development; synthesis of empirical studies (PISA 2022, neuroscience, field experiments); conceptual human-development framework.
- **Relevance to our paper:** Empirical backing for age-specific curriculum design: cognitive offloading risks, the calculator analogy (introduce tools only after foundational skills), critical/creative/relational thinking as learning goals, and teaching responsible AI/social-media use in curricula. Tags: [age-appropriateness] [safeguards-behaviors] [pedagogy] [assessment] [curriculum-difficulty] [policy] [ethics]
- **Key points with locations:**
  - Calculator analogy: chatbots help only after basic writing/analysis skills are acquired; cognitive offloading reduces retention (Ch. 3, pp. 72–74)
  - PISA 2022: low critical thinking → >3× extreme trust/distrust of online content; benefits of digital resources diminish with excessive use (Ch. 6, pp. 180–181, figs. 6.9–6.10)
  - "Including AI, algorithms and social media use in school curricula is key"; curricula need constant updating, teachers training (Ch. 3, pp. 78–79)
- **Caveats:** 324-page report. Read in full: table of contents; Overview (pp. 2–11); Terms and concepts (pp. 12–13); Chapter 1 opening/key messages (pp. 16–19); Chapter 2 closing recommendations (pp. 60–63); Chapter 3 in full incl. Spotlights 3.1–3.3 (pp. 66–99); Chapter 4 benchmark section (pp. 122–125); Chapter 6 education section "Investing in capabilities that count" (pp. 179–187) + Spotlight 6.1. Not read in full: Chapters 1–2 (middle), 4 (rest), 5, statistical annex — judged less relevant to children/education.


---

<!-- ===== batch_2_ai_literacy__validation_required.md ===== -->

# Literature Summaries — Batch 2: AI Literacy

Base path: `Literature/Literature on AI literacy/`. All files read in full via the Read tool (PDFs auto-converted; PNG read as image). Summaries are based solely on the read content.

---

## [AICOS] Objective measurement of AI literacy: Development and validation of the AI competency objective scale (AICOS)
- **Citation (APA, best effort from the document):** Markus, A., Carolus, A., & Wienrich, C. (2025). Objective measurement of AI literacy: Development and validation of the AI competency objective scale (AICOS). *Computers and Education: Artificial Intelligence, 9*, 100485. https://doi.org/10.1016/j.caeai.2025.100485
- **File:** `Markus et al - 2025 - Objective measurement of AI literacy Development and validation of the AI.pdf`
- **Type:** empirical (scale development/validation)
- **Core claims:** AICOS is an objective, MCQ-based measure of AI literacy built from content-validated items of prior instruments, covering six sub-competencies: Apply AI, Create AI, Detect AI, AI Ethics, Generative AI, Understand AI. It addresses weaknesses of self-report measures (subjective–objective AI literacy correlate only ~r = .04) and explicitly adds Generative AI literacy.
- **Evidence/methods:** German sample N = 514 (ages 18–74) via Prolific; 282 → 107 → 51 items via expert rating and 3PL IRT. Final scale: α = .83, CR = .90; unidimensional CFA acceptable; six-factor structure fits slightly better but parsimony favors one factor. Convergent validity r = .58 (H&P items), predictive r = .42 (CS quiz). An 18-item short version (AICOS-SV) is proposed.
- **Relevance to our paper:** Source instrument for our assessment items; its sub-competency structure (incl. AI Ethics, Detect AI) frames our content analysis, but it is adult-normed and knowledge-only — supports our critique that frameworks/instruments are not age-specific and omit behavior/safeguards. Tags: [assessment] [content-frameworks] [ai-literacy-def] [age-appropriateness]
- **Key points with locations:**
  - Six sub-competencies mapped to Bloom's taxonomy (Table 1, p. 2)
  - Final 51-item pool with IRT parameters and item sources (Table 10, pp. 7–8)
  - Limitation: measures knowledge only; knowledge weakly correlated with behavior (Sec. 4.2, p. 12)
- **Caveats:** Adult German sample; authors note behavioral measures are needed and items may age quickly.

## [MAILS-SV] Meta AI literacy scale: Further validation and development of a short version
- **Citation (APA):** Koch, M. J., Carolus, A., Wienrich, C., & Latoschik, M. E. (2024). Meta AI literacy scale: Further validation and development of a short version. *Heliyon, 10*(21), e39686. https://doi.org/10.1016/j.heliyon.2024.e39686
- **File:** `Koch et al - 2024 - Meta AI literacy scale Further validation and development of a short version.pdf`
- **Type:** empirical (scale validation)
- **Core claims:** Validates the 34-item MAILS self-assessment (AI literacy + AI self-efficacy + AI self-competency) against a nomological network of axioms, and derives a 10-item short version. MAILS total AI literacy correlates only weakly with an objective AI knowledge test (r = .21), confirming subjective and objective AI literacy are distinct.
- **Evidence/methods:** Four studies: N = 300 (German), N = 149 (English), N = 120 (German, with Hornberger objective test), N = 653 pooled for short-version CFA. Short version fits well (CFI = .958, RMSEA = .090). AI self-competency subscale showed deviating correlation patterns.
- **Relevance to our paper:** Theoretical parent of AICOS (Carolus et al., 2023 model: Use/Understand/Detect/Evaluate&Create/Ethics); documents the subjective–objective measurement gap that justifies our use of objective AICOS items. Tags: [assessment] [ai-literacy-def] [content-frameworks]
- **Key points with locations:**
  - MAILS factor structure and 11-point response format (Sec. 2.1, pp. 2–3)
  - Weak MAILS–objective test correlation, only Know & Understand AI relates (Table 4, p. 8)
  - 10-item short version selection via CFA (Sec. 3.4, pp. 8–9)
- **Caveats:** Self-report only; axioms 1e and 2c untested; translation between German/English not systematically validated.

## [Heptagon] The AI literacy heptagon: A structured approach to AI literacy in higher education
- **Citation (APA):** Hackl, V., Müller, A. E., & Sailer, M. (2026). The AI literacy heptagon: A structured approach to AI literacy in higher education. *Computers and Education: Artificial Intelligence, 10*, 100540. https://doi.org/10.1016/j.caeai.2026.100540
- **File:** `Hackl et al - 2026 - The AI literacy heptagon A structured approach to AI literacy in higher.pdf`
- **Type:** framework (integrative literature review + expert curriculum mapping)
- **Core claims:** Synthesizes 27 AIL conceptualizations (2021–2024) into seven dimensions — Technical Knowledge & Skills, Application Proficiency, Critical Thinking, Ethical Awareness & Reasoning, Social Impact Understanding, Integration Skills, Legal & Regulatory Knowledge — with four Bloom-linked proficiency levels (Unaware→Expert). Legal/regulatory knowledge appeared in only 2/27 sources, marking it as neglected.
- **Evidence/methods:** PRISMA-guided integrative review (WoS/Scopus, to Dec 2024); initial validation via expert-led mapping of two curricula (AI Engineering BSc; Media Pedagogy teacher education).
- **Relevance to our paper:** A curriculum-analysis instrument with dimensions × proficiency levels — methodologically analogous to our 5-dimension curriculum analysis; its finding that legal/safeguard content is underrepresented supports our critique. Tags: [content-frameworks] [ai-literacy-def] [curriculum-difficulty] [safeguards-behaviors] [ethics]
- **Key points with locations:**
  - Dimension frequency counts across 27 frameworks (Table 1, p. 3)
  - Working definition of AIL (Sec. 4.2, p. 6)
  - Levels × dimensions grid based on Bloom (Table 3, p. 7)
- **Caveats:** HE-focused, not K-12; validation is qualitative/illustrative with only two experts; no student outcome measurement.

## [MaC13-Disinformation] The Effectiveness of an Educational Intervention on Countering Disinformation Moderated by Intellectual Humility
- **Citation (APA):** Gross, E.-C., & Balaban, D. C. (2025). The effectiveness of an educational intervention on countering disinformation moderated by intellectual humility. *Media and Communication, 13*, 9109. https://doi.org/10.17645/mac.9109
- **File:** `Gross & Balaban - 2025 - The effectiveness of an educational intervention on countering disinformation.pdf`
- **Type:** empirical (within-subject +1 experiment)
- **Core claims:** A 15-minute educational intervention based on the European Commission (2022) disinformation guidelines increased perceived social media literacy and reduced general conspiracy beliefs, but did not reduce intention to share fake news. Intellectual humility moderates effects: the intervention raised algorithmic awareness only at low/medium intellectual humility.
- **Evidence/methods:** N = 127 young adults (18–23, 86% female), pre/post +1 week design, fictitious Instagram outlet with 2 fake + 1 true post; PROCESS moderated-mediation.
- **Relevance to our paper:** Evidence that literacy interventions change beliefs/perceptions more readily than sharing behavior — supports our argument that curricula need explicit safeguards/behavior content, not just knowledge. Tags: [safeguards-behaviors] [pedagogy] [assessment] [ethics]
- **Key points with locations:**
  - Hypotheses H1–H5 on PSML, sharing intention, conspiracy beliefs (Sec. 2, pp. 5–6)
  - Intervention raised PSML and lowered conspiracy beliefs; no effect on sharing intention (Sec. 4.2, pp. 10–11)
  - Self-efficacy caveat: confidence ≠ skills (Sec. 5, p. 12)
- **Caveats:** Convenience sample, self-assessed outcomes, young adults not children; no long-term follow-up.

## [Overdeck] Designing Learning FOR the Age of AI: A Better Path (Overdeck/Transcend resource)
- **Citation (APA, best effort):** Transcend Inc. (2026). *Designing learning FOR the age of AI: A better path* (V1). Transcend Inc. (supported by Overdeck Family Foundation).
- **File:** `Transcend Inc - 2026 - Designing learning FOR the age of AI A better path (V1). Transcend Inc..pdf`
- **Type:** report / position
- **Core claims:** Contrasts a "probable path" (AI optimizes industrial-era schooling) with a "preferable path" (AI enables holistic outcomes: human core, adaptive bridge, technical edge). AI literacy is named the newest, least-developed outcome area — currently sparse, fragmented, with no coherent vertically aligned K-12 pathway. Five ecosystem priorities include shared AI literacy frameworks/curricula/assessments and new assessment systems.
- **Evidence/methods:** Non-empirical; analysis of 14 outcomes frameworks (Appendix, p. 60); three vignettes (K–2, middle-school math, 11th-grade career learning) with "spicier/milder/rotten" variants; school spotlights.
- **Relevance to our paper:** Policy-level corroboration that AI literacy lacks age-aligned frameworks and assessments; its framework analysis shows most frameworks miss at least one of the three outcome categories. Tags: [policy] [content-frameworks] [assessment] [age-appropriateness]
- **Key points with locations:**
  - AI literacy as new focus area; fragmented instruction warning (pp. 12–13)
  - Five ecosystem priorities incl. shared AI literacy frameworks (p. 6, pp. 42–43)
  - Framework comparison table incl. UNESCO AI CFS, AILit, Five Big Ideas (Appendix, p. 60)
- **Caveats:** Advocacy document, not peer-reviewed; ChatGPT/Claude acknowledged as writing assistants; US-centric.

## [Eden-DL-Equity] Promoting Digital Literacy and Social Equity in Education: Lessons from Successful Initiatives
- **Citation (APA):** Eden, C. A., Chisom, O. N., & Adeniyi, I. S. (2024). Promoting digital literacy and social equity in education: Lessons from successful initiatives. *International Journal of Management & Entrepreneurship Research, 6*(3), 687–696. https://doi.org/10.51594/ijmer.v6i3.880
- **File:** `Eden et al - 2024 - Promoting digital literacy and social equity in education Lessons from.pdf`
- **Type:** review (narrative)
- **Core claims:** Successful digital-literacy-and-equity initiatives share four principles: equitable access to technology/connectivity, culturally relevant and inclusive curricula, development of critical thinking and digital citizenship skills, and multi-stakeholder collaboration. The digital divide disproportionately affects marginalized communities and perpetuates achievement gaps.
- **Evidence/methods:** Narrative review; cites initiatives (E-rate, One Laptop per Child, Google's Be Internet Awesome, Common Sense Education, Digital Promise League).
- **Relevance to our paper:** Context/equity framing for our Context dimension; culturally relevant curriculum argument supports age- and context-appropriate design. Tags: [policy] [pedagogy] [ai-literacy-def]
- **Key points with locations:**
  - Four key principles of successful initiatives (Abstract, p. 687)
  - Digital divide effects on underserved communities (pp. 688–689)
  - Case studies of critical thinking/digital citizenship integration (p. 691)
- **Caveats:** Low-rigor outlet; largely US examples; no systematic methodology; some references appear mismatched to claims.

## [Hitron-BlackBoxes] Can Children Understand Machine Learning Concepts? The Effect of Uncovering Black Boxes
- **Citation (APA):** Hitron, T., Orlev, Y., Wald, I., Shamir, A., Erel, H., & Zuckerman, O. (2019). Can children understand machine learning concepts? The effect of uncovering black boxes. In *Proceedings of CHI 2019* (Paper 415). ACM. https://doi.org/10.1145/3290605.3300645
- **File:** `Hitron et al - 2019 - Can children understand machine learning concepts The effect of uncovering.pdf`
- **Type:** empirical (mixed pre/post + between-subjects experiment)
- **Core claims:** Children aged 10–13 can understand basic supervised-ML concepts (sample size, sample versatility, negative examples) — but only when both Data Labeling and Evaluation building blocks are uncovered; uncovering only one yields no learning. Children transferred understanding to real-life ML applications and generated accurate, personally meaningful ML application ideas; 50% spontaneously identified contexts where ML should not be used (safety, privacy).
- **Evidence/methods:** N = 30 children (M = 11.59 years), three conditions (full system / labeling-only / evaluation-only) with the "Gest" gesture-recognition platform; two-way ANOVA (same-context F(2,27)=16.19; different-context F(2,27)=8.46); video coding, κ = .92.
- **Relevance to our paper:** Direct evidence for our age group that hands-on, iterative, embodied ML activities build accurate mental models — supports our hands-on didactics with Marty; shows children can reason about ML risks (safeguards). Tags: [hands-on] [age-appropriateness] [didactics] [pedagogy] [safeguards-behaviors]
- **Key points with locations:**
  - Four design principles: low floor, uncovering black boxes, iterations, self-generated knowledge (Sec. 2, pp. 3–4)
  - Only full system improved understanding; partial conditions = no learning (Sec. 5, pp. 7–8)
  - Children's ML risk reasoning: "Computers will always make mistakes" (Sec. 5, p. 9)
- **Caveats:** Small N, gender-imbalanced (20 boys/10 girls); classification tasks only; no non-hands-on comparison.

## [UNESCO-DLA] Digital Literacy Assessment (background paper for 2023 GEM Report)
- **Citation (APA):** Reichert, F., Pan, Q., & Chen, L. L. (2023). *Digital literacy assessment* [Background paper for the 2023 Global Education Monitoring Report: Technology in education]. UNESCO.
- **File:** `Reichert et al - 2023 - Digital literacy assessment.pdf`
- **Type:** report (systematic reviews + policy analysis)
- **Core claims:** Reviews digital skills frameworks (DigComp/DLGF dominant) and 15 large-scale assessments (ICILS, PISA-DRA, NAP-ICTL, NEPS-CL etc.). Key findings: digital literacy is empirically near-unidimensional despite multidimensional theorizing; self-reports are inaccurate (people overestimate; males over-report despite female performance advantage); assessments valid for children under 10 are particularly rare; AI-related skills are not yet implemented in large-scale assessments but will be needed.
- **Evidence/methods:** Systematic review of frameworks (2019–2022; 174 definitions of digital literacy found), 3 international + 12 regional performance assessments, and curriculum/policy documents from 35 education systems.
- **Relevance to our paper:** Authoritative support for performance-based over self-report assessment (aligns with AICOS choice); documents the assessment gap for young learners and absent AI-skill measurement — core to our critique. Tags: [assessment] [policy] [ai-literacy-def] [age-appropriateness]
- **Key points with locations:**
  - Self-report vs. performance discrepancy (Sec. 1, p. 5)
  - Unidimensionality and tool-dependency/testlet effects (Sec. 5.1, pp. 16–18)
  - Rarity of assessments for under-10s; AI skills not yet assessed (Sec. 7.1, p. 26; Sec. 7.2, p. 30)
- **Caveats:** Not edited by UNESCO GEM team; covers digital literacy broadly, AI only peripherally; search ended April 2022.

## [AI-CI] Developing and Validating the Artificial Intelligence Literacy Concept Inventory (AI-CI) for Middle School Students
- **Citation (APA):** Zhang, H., Perry, A., & Lee, I. (2025). Developing and validating the Artificial Intelligence Literacy Concept Inventory: An instrument to assess artificial intelligence literacy among middle school students. *International Journal of Artificial Intelligence in Education, 35*, 398–438. https://doi.org/10.1007/s40593-024-00398-x
- **File:** `AI literacy assessement/Zhang et al - 2025 - Developing and validating the Artificial Intelligence Literacy Concept.pdf`
- **Type:** empirical (instrument development/validation)
- **Core claims:** The AI-CI is a 20-item distractor-driven multiple-choice concept inventory measuring middle schoolers' AI literacy across four topics: AI general concepts, logic systems, ML general concepts, supervised learning (incl. bias/ethics). Expert panels judged neural networks and GANs too complex for early middle school — direct evidence on age-appropriateness boundaries.
- **Evidence/methods:** Six-step CI procedure (expert panels, student observations/interviews, cognitive interviews); validation N = 981 middle schoolers (2PL-IRT, unidimensional); pre/post reliability with N = 108 DAILy curriculum students (α = .73; significant gains t(85)=4.80, p<.0001; no gender/race differences).
- **Relevance to our paper:** The closest existing instrument to our target age (10–13); documents misconceptions (AI = automation/algorithms) and age-appropriateness judgments; its unidimensional outcome and DAILy co-development illustrate curriculum–assessment alignment issues we analyze. Tags: [assessment] [age-appropriateness] [curriculum-difficulty] [content-frameworks]
- **Key points with locations:**
  - Expert panels: NNs/GANs "too complex" for 6th–7th grade; add ethics/bias (Sec. Step 1, pp. 10–12)
  - Student misconceptions: AI confused with automation, sensing, algorithms (Sec. Step 2, pp. 12–14)
  - 30→20 item reduction via 2PL-IRT; pre/post sensitivity (pp. 19–24)
- **Caveats:** Developed alongside DAILy (not fully curriculum-independent); US sample; item content shown only as images in appendices (not text-extractable).

## [Yang-Progression] A Systematic Review Mapping of AI Literacy Progression in K–12
- **Citation (APA):** Yang, H., Rachmatullah, A., Alozie, N., Capan, S., & Cao, Q. (2025). A systematic review mapping of AI literacy progression in K–12. *Journal for STEM Education Research*. https://doi.org/10.1007/s41979-025-00166-z
- **Files:** `AI literacy assessement/Yang et al - 2025 - A systematic review mapping of AI literacy progression in K–12.pdf` AND `Literature on AI curriculums/Yang et al - 2025 - A systematic review mapping of AI literacy progression in K–12.pdf` (identical paper, same DOI — duplicate); supplementary: `Literature on AI curriculums/Yang et al - 2025 - A systematic review mapping of AI literacy progression in K–12 supmat.pdf`
- **Type:** review (systematic, PRISMA)
- **Core claims:** Across 36 empirical K–12 studies, five AI literacy components emerge: Understanding Foundational AI Concepts, Creating AI Artifacts, Interacting With AI Agents, Developing Awareness of AI Ethics, Understanding Human-AI Relationships. Competencies progress by grade band: elementary = awareness/interest via play; middle school (7–8) = defining AI, creating artifacts for community issues, ethical principles; high school = professional, project-based depth. "Understanding Human-AI Relationships" integrates the other four.
- **Evidence/methods:** PRISMA review (ProQuest + WoS, 2018–Mar 2024), 36 studies, constant-comparative open/axial coding by two researchers; grade bands K–3, 4–6, 7–8, 9–12. Supplement = Appendix A mapping each study to grade bands and components.
- **Relevance to our paper:** The key age-progression synthesis: our 11–12-year-olds sit at the 4–6/7–8 boundary; provides the empirical grade-band competency map against which our curriculum content difficulty can be benchmarked. Tags: [age-appropriateness] [curriculum-difficulty] [content-frameworks] [ai-literacy-def] [ethics]
- **Key points with locations:**
  - Five components and counts by grade band (Fig. 2, p. 12)
  - Full progression table of competencies by band (Table 2, pp. 14–17)
  - Middle schoolers' naive conceptions: AI = automation/robotics, all-powerful (Sec. RQ2, p. 18)
- **Caveats:** Only 36 studies; two databases; no inter-rater reliability statistic (consensus process only); literature ends March 2024.

## [Yang-Fig3] AI literacy Framework_Yang et al 2025.png (Figure: Relationships among the five AI literacy components)
- **Citation (APA):** Yang, H., Rachmatullah, A., Alozie, N., Capan, S., & Cao, Q. (2025). A systematic review mapping of AI literacy progression in K–12 [Figure 3]. *Journal for STEM Education Research*. https://doi.org/10.1007/s41979-025-00166-z
- **File:** `AI literacy Framework_Yang et al 2025.png` (image, read visually)
- **Type:** framework (figure)
- **Core claims / structure:** The diagram shows a central red circle, "Understanding Human-AI Relationships," connected by a double-headed arrow labeled "inform each other" to a blue rounded rectangle containing the other four components: "Understanding Foundational AI Concepts," "Creating AI Artifacts," "Interacting With AI Agents," and "Developing Awareness of AI Ethics." Inside the rectangle, a circular arrow labeled "iterative process" links the four components.
- **Evidence/methods:** n/a (conceptual figure from the systematic review above).
- **Relevance to our paper:** Compact visual model: human–AI relationship understanding is the integrative hub; the four content components develop iteratively — a structure we can contrast with our 5-dimension curriculum analysis and use to argue that safeguards/behavior content cuts across components. Tags: [content-frameworks] [ai-literacy-def] [safeguards-behaviors]
- **Key points with locations:**
  - Central hub: Understanding Human-AI Relationships (figure center)
  - "inform each other" bidirectional link between hub and the four-component block
  - "iterative process" cycle among the four components (inside blue block)
- **Caveats:** Image only; interpretive detail limited to what is visible; same evidentiary base as [Yang-Progression].


---

<!-- ===== batch_3_papers_ai_literacy__validation_required.md ===== -->

# Batch 3 Literature Summaries — Papers on AI Literacy

Summaries of 16 sources for the AI & digital literacy curriculum paper (Marty robot, ages 11–12; Context / Content / Pedagogy / Didactics / Assessment). All files were read in full. Where a `.txt` twin existed, the PDF first page was checked for title match and the `.txt` was read; this is stated per summary.

---

## [01] What is AI Literacy? Competencies and Design Considerations
- **Citation (APA):** Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations. *Proceedings of CHI 2020*. ACM.
- **File:** Literature on AI literacy/Papers on AI literacy/Long & Magerko - 2020 - What is AI literacy Competencies and design considerations (.txt twin used; PDF title verified)
- **Type:** position/framework
- **Core claims:** Provides the seminal definition of AI literacy: "a set of competencies that enables individuals to critically evaluate AI technologies; communicate and collaborate effectively with AI; and use AI as a tool." Synthesizes interdisciplinary literature into 17 competencies and 15 design considerations.
- **Evidence/methods:** Literature synthesis across HCI, AI, and education; expert workshop input.
- **Relevance:** Foundational [ai-literacy-def] source and [content-frameworks] baseline our curriculum content is mapped against; its design considerations inform [didactics] and [hands-on] robot activities.
- **Key points with locations:**
  - Competency list incl. "recognize AI," "understand intelligence," "ethics" competencies (Table 2, pp. 3–5).
  - Design considerations: explainability, embodied interaction, promoting identity exploration (Table 3, pp. 6–9).
  - Explicit call to design for low-AI-exposure learners and broad audiences (Discussion).
- **Caveats:** Pre-dates generative AI boom; not age-specific (adult/general-user oriented).

## [02] Empowering Learners for the Age of AI: An AI Literacy Framework for Primary and Secondary Education (AILit Framework, Review Draft)
- **Citation (APA):** European Commission, OECD, & Code.org. (2025). *Empowering learners for the age of AI: An AI literacy framework for primary and secondary education* (Review draft, May 2025).
- **File:** Literature on AI literacy/Papers on AI literacy/European Commission et al - 2025 - Empowering learners for the age of AI An AI literacy framework for primary and review draft (.txt twin used; PDF title verified)
- **Type:** framework
- **Core claims:** Joint EC/OECD framework defining AI literacy for schools via 4 domains (Engaging with, Creating with, Managing AI's Actions, Designing AI) and 22 competences with knowledge, skills, and attitudes; feeds PISA 2029 Media & AI Literacy assessment.
- **Evidence/methods:** Expert co-construction; review draft open for stakeholder feedback.
- **Relevance:** The central contemporary [content-frameworks] reference for school-age AI literacy; directly relevant to our critique that such frameworks are not [age-appropriateness]-differentiated (11–12 vs. teens) and under-specify [safeguards-behaviors].
- **Key points with locations:**
  - 4 domains × 22 competences structure (main framework tables).
  - Explicit linkage to PISA 2029 and DigComp 2.2 / EU AI Act Article 4 (Welcome section, p. 1).
  - Practical "competence descriptions + scenarios" format usable for [assessment] alignment.
- **Caveats:** Review draft (May 2025), not final; spans whole primary+secondary range, so age granularity is limited.

## [03] Young Children's Understanding of AI
- **Citation (APA):** Heeg, D. M., & Avraamidou, L. (2025). Young children's understanding of AI. *Education and Information Technologies, 30*, 10207–10230. https://doi.org/10.1007/s10639-024-13169-x
- **File:** Literature on AI literacy/Papers on AI literacy/Heeg & Avraamidou - 2025 - Young children's understanding of AI.pdf (PDF only, read in full)
- **Type:** empirical (qualitative case study)
- **Core claims:** Dutch 11–12-year-olds conceptualize AI through personal experience; take a socio-cultural view of AI as a supportive tool; and engage readily with AI ethics (privacy, data ownership, racial/gender bias). They also project future AI roles (chores, health, transport) while noting environmental harms.
- **Evidence/methods:** Classroom discussion with 18 children (age 11–12) after use of a drawing/recognition app; thematic analysis of transcripts.
- **Relevance:** Exact target age group; direct evidence for [age-appropriateness], [content-frameworks] (child-elicited AI concepts), [ethics], and discussion-based [pedagogy]/[didactics] with an everyday AI artifact.
- **Key points with locations:**
  - Socio-cultural conceptualizations of AI (Sec. 4.2–4.3, pp. 10215–10218).
  - Children's engagement with ethical issues: privacy, data ownership, stereotypes (Sec. 4.3, pp. 10218–10220).
  - Recommendations: software applications, daily-life experiences, collective classroom experience, critical AI literacy with justice focus (Sec. 6, pp. 10221–10225).
- **Caveats:** Single small sample (n=18), one school context; not about robots.

## [07] Artificial Intelligence Literacy in Higher and Adult Education: A Scoping Literature Review
- **Citation (APA):** Laupichler, M. C., Aster, A., Schirch, J., & Raupach, T. (2022). Artificial intelligence literacy in higher and adult education: A scoping literature review. *Computers and Education: Artificial Intelligence, 3*, 100101.
- **File:** Literature on AI literacy/Papers on AI literacy/Laupichler et al - 2022 - Artificial intelligence literacy in higher and adult education A scoping (.txt twin used; PDF title verified)
- **Type:** review (scoping)
- **Core claims:** Research on AI literacy for non-expert adults is in its infancy; definitions and taught content are inconsistent. There is little empirical evidence on whether/how AI literacy differs between adults and children.
- **Evidence/methods:** 10 databases searched; 30 of 902 records included and content-analyzed.
- **Relevance:** Supports our argument that [content-frameworks] and [ai-literacy-def] lack [age-appropriateness] differentiation; documents absence of age-comparative evidence.
- **Key points with locations:**
  - Field "still in its infancy"; definitional inconsistency (Abstract; Results).
  - 30 included studies' thematic foci (Results/Tables).
  - Recommendations for defining AI literacy content for non-experts (Discussion).
- **Caveats:** Adult/HE focus only; pre-ChatGPT (2022).

## [08] Conceptualizing AI Literacy: An Exploratory Review
- **Citation (APA):** Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021). Conceptualizing AI literacy: An exploratory review. *Computers and Education: Artificial Intelligence, 2*, 100041.
- **File:** Literature on AI literacy/Papers on AI literacy/Ng et al - 2021 - Conceptualizing AI literacy An exploratory review (.txt twin used; PDF title verified)
- **Type:** review
- **Core claims:** Proposes four AI literacy aspects — know & understand, use & apply, evaluate & create, ethical issues — mapped to Bloom's Taxonomy; ethics is integral, not peripheral. Calls for age-appropriate learning artifacts and notes AI literacy assessment is nascent.
- **Evidence/methods:** Exploratory review of 30 peer-reviewed articles.
- **Relevance:** Widely used [content-frameworks] and [ai-literacy-def] anchor; the Bloom mapping supports our [curriculum-difficulty] progression and [assessment] design; ethics pillar aligns with [ethics]/[safeguards-behaviors].
- **Key points with locations:**
  - Four-aspect framework with Bloom mapping (Sec. 3–4).
  - Ethics as a distinct AI literacy aspect (Sec. 4, ethical issues).
  - Need for age-appropriate artifacts and validated assessment instruments (Discussion).
- **Caveats:** 2021, pre-GenAI; conceptual rather than empirical validation.

## [09] The Blueprint for Action: Comprehensive AI Literacy for All
- **Citation (APA):** EDSAFE AI Alliance. (n.d.). *The blueprint for action: Comprehensive AI literacy for all*. www.edsafeai.org
- **File:** Literature on AI literacy/Papers on AI literacy/EDSAFE AI Alliance - n.d. - The blueprint for action Comprehensive AI literacy for all (.txt twin used; PDF title verified)
- **Type:** report
- **Core claims:** Advocates "comprehensive AI literacy" across learning-experience, social-ethical, and economic-civic considerations; calls for developmentally appropriate K-12 instruction grounded in the Science of Learning and Development.
- **Evidence/methods:** Policy/advocacy synthesis by the EDSAFE AI Alliance; no primary data.
- **Relevance:** [policy] and [content-frameworks] support for school AI literacy; explicit developmental-appropriateness stance relevant to [age-appropriateness] and our critique.
- **Key points with locations:**
  - Three consideration categories structuring AI literacy (Sections: Learning Experience p. 7; Social/Ethical p. 11; Economic/Civic p. 14).
  - Developmentally appropriate K-12 instruction call (Learning Experience section).
  - Action agenda for states/districts (Executive Summary, p. 1).
- **Caveats:** Advocacy document; no empirical evidence; publication year not stated in text.

## [10] AI, Brain, and Child: Navigating the Intersection of Artificial Intelligence, Neuroscience, and Child Development
- **Citation (APA):** Li, P. H., & Lee, J. C.-K. (2025). AI, Brain, and Child: Navigating the intersection of artificial intelligence, neuroscience, and child development. *AI, Brain and Child, 1*, Article 3. https://doi.org/10.1007/s44436-025-00004-4
- **File:** Literature on AI literacy/Papers on AI literacy/Li & Lee - 2025 - AI, Brain, and Child Navigating the intersection of artificial intelligence, (.txt twin used; PDF title verified)
- **Type:** position (launch editorial)
- **Core claims:** Introduces an interdisciplinary journal on AI × neuroscience × child development; argues AI's effects on children's cognitive, social, and emotional growth require rigorous, ethically conscious study, including neuroplasticity, cognitive overload, data privacy, and algorithmic bias.
- **Evidence/methods:** Editorial; argument from literature and field positioning.
- **Relevance:** Frames why child-specific AI research is needed — supports [age-appropriateness] and [safeguards-behaviors] rationale in our introduction.
- **Key points with locations:**
  - Journal scope: interplay of AI, neuroscience, child education (Abstract/Introduction).
  - Risks: cognitive overload, privacy, algorithmic bias (Introduction).
  - Call for evidence-based educational practice with AI (throughout).
- **Caveats:** Editorial, not empirical; broad scope, little curriculum-level detail.

## [11] Developmentally Aligned AI: A Framework for Translating the Science of Child Development into AI Design
- **Citation (APA):** Kurian, N. (2025). Developmentally aligned AI: A framework for translating the science of child development into AI design. *AI, Brain and Child, 1*, Article 9. https://doi.org/10.1007/s44436-025-00009-z
- **File:** Literature on AI literacy/Papers on AI literacy/Kurian - 2025 - Developmentally aligned AI A framework for translating the science of child (.txt twin used; PDF title verified)
- **Type:** framework
- **Core claims:** Proposes Developmentally Aligned Design (DAD): four principles — perceptual fit, cognitive scaffolding (ZPD), interface simplicity, relational integrity — translating child-development science into AI design; shifts "proof of safety" burden from parents/practitioners to developers.
- **Evidence/methods:** Conceptual framework with illustrative examples (reading apps, tutoring agents, conversational agents).
- **Relevance:** Direct theoretical backing for our [age-appropriateness] critique and for [safeguards-behaviors] (relational integrity = anti-anthropomorphism disclaimers); informs [pedagogy] and robot-interaction [didactics].
- **Key points with locations:**
  - Four DAD principles with examples (Abstract; main framework section).
  - ZPD-based cognitive scaffolding for tutoring agents (principle 2).
  - Relational integrity: "I'm a computer helper, not a real friend" disclaimers (principle 4).
- **Caveats:** Focused on young children (early childhood, up to ~8); conceptual, not validated with 11–12-year-olds.

## [12] The Future of Child Development in the AI Era: Cross-Disciplinary Perspectives Between AI and Child Development Experts
- **Citation (APA):** Neugnot-Cerioli, M., & Muss Laurenty, O. (n.d.). *The future of child development in the AI era: Cross-disciplinary perspectives between AI and child development experts*. everyone.ai.
- **File:** Literature on AI literacy/Papers on AI literacy/Neugnot-Cerioli & Laurenty - n.d. - The future of child development in the AI era Cross-disciplinary perspectives (.txt twin used; PDF title verified)
- **Type:** report
- **Core claims:** Integrating AI into children's environments will transform leisure, education, and human–machine interaction; benefits (interactive engagement) are balanced by serious risks during sensitive developmental periods (first ~25 years of brain development): screen-time harms, myopia, sleep, sedentary behavior, attention-capturing algorithms, privacy, emotional attachment to AI.
- **Evidence/methods:** Consultations with 15 experts (AI, product development, child development, neuroscience) plus literature review.
- **Relevance:** Strong [safeguards-behaviors] evidence base; developmental-neuroscience grounding for [age-appropriateness]; recommendations to educate regulators, developers, parents, educators, and children support our [pedagogy]/[policy] framing.
- **Key points with locations:**
  - Expert anticipation of AI transforming leisure/education (Abstract; Sec. 1–2).
  - Risk analysis: screen time, attention algorithms, emotional bonds with conversational agents (middle sections).
  - Recommendations for governments, developers, parents/educators (final section; expert appendix).
- **Caveats:** Publication year not stated in document; NGO report, not peer-reviewed.

## [13] Responsible AI and Children: Insights, Implications, and Best Practices
- **Citation (APA):** Grimes, S. M., Antle, A. N., Steeves, V., & Coulter, N. (2024). *Responsible AI and children: Insights, implications, and best practices*. CIFAR.
- **File:** Literature on AI literacy/Papers on AI literacy/Grimes et al - 2024 - Responsible AI and children Insights, implications, and best practices (.txt twin used; PDF title verified)
- **Type:** report (policy brief)
- **Core claims:** Advocates a children's-rights-based approach to AI (UNCRC General Comment 25), defines distinct child age groups, and argues children must be involved in AI research/development, including through hands-on activities; recognizes diversity of childhood experiences.
- **Evidence/methods:** Expert-authored policy synthesis (Canadian HCI/law/media scholars).
- **Relevance:** Rights-based [policy] and [safeguards-behaviors] framing; child-participation and [hands-on] argument supports our Marty-robot participatory design; age-band definitions relate to [age-appropriateness].
- **Key points with locations:**
  - Rights-based regulatory framing via UNCRC GC25 (main body).
  - Age group definitions and diversity of childhoods (early sections).
  - Best practices incl. children's involvement via hands-on activities (best-practices section).
- **Caveats:** Policy brief, not empirical; Canadian-centric examples.

## [14] Policy Guidance on AI for Children 2.0
- **Citation (APA):** UNICEF. (2021). *Policy guidance on AI for children 2.0*. UNICEF.
- **File:** Literature on AI literacy/Papers on AI literacy/UNICEF - 2021 - Policy guidance on AI for children 2.0 (.txt twin used; PDF title verified)
- **Type:** report (policy guidance)
- **Core claims:** Sets out 9 requirements for child-centred AI grounded in the Convention on the Rights of the Child, including AI literacy for children (knowledge, skills, attitudes/values, knowing their rights as users) and age-appropriate language/design.
- **Evidence/methods:** Global consultation process with pilot case studies (incl. the Haru social robot).
- **Relevance:** Cornerstone [policy] and [safeguards-behaviors] source; UNICEF's AI-literacy component supports [ai-literacy-def]; developmental-stage footnote (mid childhood 5–10, younger adolescence 10–15) directly frames our 11–12 cohort's [age-appropriateness]; Haru case relevant to [social-robots].
- **Key points with locations:**
  - 9 child-centred AI requirements (core framework section).
  - AI literacy definition incl. rights-as-users (requirement on AI literacy).
  - Developmental stages footnote (early childhood <5; mid 5–10; younger adolescence 10–15; older 15–18).
- **Caveats:** Policy level, not classroom-level curriculum guidance.

## [15] A Comprehensive Survey of AI-Generated Content (AIGC): A History of Generative AI from GAN to ChatGPT
- **Citation (APA):** Cao, Y., Li, S., Liu, Y., Yan, Z., Dai, Y., Yu, P. S., & Sun, L. (2023). A comprehensive survey of AI-generated content (AIGC): A history of generative AI from GAN to ChatGPT. *arXiv*. https://arxiv.org/abs/2303.04226
- **File:** Literature on AI literacy/Papers on AI literacy/Cao et al - 2023 - A comprehensive survey of AI-generated content (AIGC) A history of generative (.txt twin used; PDF title verified)
- **Type:** review (technical survey)
- **Core claims:** Surveys generative AI history and techniques (GANs through ChatGPT); documents applications incl. education; catalogs trustworthiness problems — factuality failures (ChatGPT produced false narratives for 80/100 misinformation samples in one cited study), toxicity, privacy leakage via membership inference and data extraction — plus bias, deepfakes, and copyright issues.
- **Evidence/methods:** Technical literature survey.
- **Relevance:** Source for [safeguards-behaviors] and [ethics] content children must understand (misinformation, deepfakes, privacy); education applications (Sec. 5.5) contextualize GenAI in classrooms.
- **Key points with locations:**
  - Education applications (Sec. 5.5).
  - Trustworthy & responsible AIGC: factuality, toxicity, privacy attacks (Sec. 7).
  - Open problems: bias, deepfakes, copyright (Sec. 8).
- **Caveats:** Highly technical; arXiv preprint (2023); citation year discrepancy with an older ACM-style reference noted.

## [19] "Aladdin's Genie or Pandora's Box for Early Childhood Education?" Experts Chat with ChatGPT
- **Citation (APA):** Su, J., & Yang, W. (2023). "Aladdin's Genie or Pandora's Box for early childhood education?" Experts chat with ChatGPT. (Early childhood education journal article).
- **File:** Literature on AI literacy/Papers on AI literacy/Su & Yang - 2023 - Aladdin's Genie or Pandora's Box for early childhood education Experts chat (.txt twin used; PDF title verified)
- **Type:** empirical (expert interviews) / position
- **Core claims:** ChatGPT can serve ECE as a conversational agent for children and an on-call facilitator for educators, but poses challenges framed by the "3A2S" scheme (Accessibility, Affordability, Accountability, Sustainability, Social Justice): precise-input demands, bias, misinformation, academic integrity, digital divide. Future seen as Intelligence Augmentation, opening AI literacy and AI social interaction as ECE domains.
- **Evidence/methods:** Expert interview study with thematic analysis.
- **Relevance:** [safeguards-behaviors] and [ethics] catalog for child-facing GenAI; supports inclusion of AI literacy in early schooling ([age-appropriateness], [content-frameworks]).
- **Key points with locations:**
  - Roles of ChatGPT in ECE (roles section).
  - 3A2S challenge framework (challenges section).
  - IA future + AI literacy as new ECE domain (future directions).
- **Caveats:** Early childhood focus, younger than our cohort; 2023 ChatGPT-specific.

## [20] ChatGPT and Artificial Intelligence in Higher Education: Quick Start Guide
- **Citation (APA):** Sabzalieva, E., & Valentini, A. (2023). *ChatGPT and artificial intelligence in higher education: Quick start guide*. UNESCO IESALC.
- **File:** Literature on AI literacy/Papers on AI literacy/Sabzalieva & Valentini - 2023 - ChatGPT and artificial intelligence in higher education Quick start guide (.txt twin used; PDF title verified)
- **Type:** report (guidance)
- **Core claims:** Explains how ChatGPT works and its uses across teaching, learning, research, and administration; catalogs challenges — academic integrity, lack of regulation, privacy (e.g., Italy's ban), cognitive bias, gender/diversity, accessibility, commercialization — and proposes institutional adaptation strategies incl. capacity building and AI audits.
- **Evidence/methods:** UNESCO IESALC guidance document referencing the UNESCO Recommendation on the Ethics of AI.
- **Relevance:** [policy]/[ethics] framing and teacher-capacity arguments transferable to school context; supports our [safeguards-behaviors] dimension.
- **Key points with locations:**
  - How ChatGPT works; use cases (early sections).
  - Challenges and ethical implications (challenges section).
  - Institutional strategies: capacity building, AI audits (recommendations).
- **Caveats:** Higher-education focus, not children; rapid-evolution topic (2023).

## [21] ChatGPT: Potential, Prospects, and Limitations
- **Citation (APA):** (2023). ChatGPT: Potential, prospects, and limitations. (Comment paper).
- **File:** Literature on AI literacy/Papers on AI literacy/Unknown - 2023 - ChatGPT Potential, prospects, and limitations. (Comment paper) (.txt twin used; PDF title verified)
- **Type:** position (comment)
- **Core claims:** ChatGPT's strengths (generalization, correction, safety, creativity) derive from LLM scale plus instruction tuning and RLHF, but key limitations persist: weak logical/maths reasoning, unreliable or biased outputs, no real-time knowledge, and vulnerability to instruction attacks and cultural bias; notes societal harms (misconduct, misinformation) and authorship ethics.
- **Evidence/methods:** Analytical commentary with demonstrations.
- **Relevance:** Concrete limitation examples usable in classroom [didactics] (testing AI fallibility); feeds [safeguards-behaviors] and [ethics] content about over-trust.
- **Key points with locations:**
  - Advantages: instruction tuning, RLHF (early sections).
  - Limitations: reasoning errors, reliability, robustness, bias (limitations section).
  - Societal/ethical effects: academic misconduct, misinformation (discussion).
- **Caveats:** 2023 snapshot of a fast-moving model family; higher-ed/general audience.

## [22] Guidance for Generative AI in Education and Research
- **Citation (APA):** UNESCO. (2023). *Guidance for generative AI in education and research*. UNESCO. https://unesdoc.unesco.org/ark:/48223/pf0000385877
- **File:** Literature on AI literacy/Papers on AI literacy/Miao & Holmes - 2023 - Guidance for generative AI in education and research (.txt twin used; PDF title verified)
- **Type:** report (policy guidance)
- **Core claims:** Provides a human-centred regulatory and pedagogical framework for GenAI in education: mandate data privacy, set an age limit for independent conversations with GenAI platforms, validate tools ethically, and build AI competencies; tables co-design specific uses (coaching, Socratic dialogue, special-needs support) with requirements and risks.
- **Evidence/methods:** UNESCO policy guidance informed by member-state survey, OECD/Stanford data, and expert input.
- **Relevance:** Directly supports our critique pillars: explicit [age-appropriateness] mechanism (age limits, "human-agent and age-appropriate approach"), [safeguards-behaviors] (privacy, inappropriate-content exposure, creativity loss), [assessment] rethinking, and teacher-capacity [policy].
- **Key points with locations:**
  - Regulatory steps incl. age limit for independent GenAI conversations (Sec. 3–4; back cover summary).
  - Risk tables: exposure to inappropriate content, echo chambers, reduced peer interaction (Tables 5–7, pp. 32–35).
  - Rethinking learning outcomes: values, foundational, higher-order, vocational (Sec. 6.5, p. 37).
- **Caveats:** Guidance level; not a validated curriculum; focuses GenAI, not physical robots.


---

<!-- ===== batch_4_curriculum_handson__validation_required.md ===== -->

# Batch 4 — Curriculum design & hands-on learning summaries

Summaries for the AI & digital literacy curriculum paper (11–12 year-olds, Marty robot; dimensions: Context, Content, Pedagogy, Didactics, Assessment; curriculum–assessment misalignment; reporting-standard proposal). All files read with the Read tool (PDF auto-converted to text). Note on coverage: the four ISEE Assessment volumes are book-length reports (188–736 pp); they were read via the full front matter/synopsis plus systematic chapter-level sampling across the whole page range (chapter starts, key-messages sections, glossaries), not line-by-line. The EQuIP rubric (14 pp) and Wang et al. (24 pp) were read in full. Tags: [curriculum-difficulty] [content-frameworks] [age-appropriateness] [assessment] [pedagogy] [didactics] [safeguards-behaviors] [social-robots] [hands-on] [ai-literacy-def] [ethics] [policy]

---

## [equip-science] EQuIP Rubric for Lessons & Units: Science (Version 3.1)

- **Citation (APA, best effort from the document):** Achieve, Inc. (2021). *EQuIP rubric for lessons & units: Science (Version 3.1)*. Creative Commons Attribution 3.1 Unported License. (EQuIP = Educators Evaluating the Quality of Instructional Products; publisher not stated on document.)
- **File:** Literature/Literature on Curriculum design/Achieve Inc - 2021 - EQuIP rubric for lessons and units Science v31.pdf
- **Type:** rubric
- **Core claims:** Provides criterion-based measures of the alignment and overall quality of science lessons/units with the Next Generation Science Standards (NGSS), organized in three categories: (I) NGSS 3D Design, (II) NGSS Instructional Supports, (III) Monitoring NGSS Student Progress. Purposes: review existing materials, give constructive feedback to developers, identify exemplars, inform new development (p. 1).
- **Evidence/methods:** Structured 5-step review process; each criterion scored for evidence (None/Inadequate/Adequate/Extensive), categories rated 0–3, overall rating E/E/I/R/N; Category I is "non-negotiable" — a score <2 halts approval review (p. 5).
- **Relevance to our paper:** A concrete, operational model for the curriculum-evaluation/reporting standard our paper proposes: criterion–evidence–reasoning documentation, unit-level coherence criteria, and a dedicated assessment-alignment category directly mirror our Context/Content/Pedagogy/Didactics/Assessment analysis and misalignment findings. Tags: [assessment] [content-frameworks] [curriculum-difficulty] [pedagogy] [didactics]
- **Key points with locations:**
  - Three categories with criteria A–F each; units get extra criteria on coherence, differentiation over time, coherent assessment system (pp. 2–3)
  - Category III requires direct observable evidence of 3D learning, embedded formative assessment, aligned scoring guidance, unbiased items (p. 2, p. 12)
  - 0–3 category scales; overall E (~8–9), E/I (~6–7), R (3–5), N (0–2) (p. 5, p. 14)
- **Caveats:** NGSS-specific (US science standards); criteria need adaptation for AI/digital literacy. Read in full (14 pp).

---

## [isee-wg1] Reimagining Education: The International Science and Evidence based Education Assessment — Working Group 1 volume (Education and Human Flourishing)

- **Citation (APA, best effort from the document):** Duraiappah, A. K., van Atteveldt, N. M., Borst, G., Bugden, S., Ergas, O., Gilead, T., Gupta, L., Mercier, J., Pugh, K., Singh, N. C., & Vickers, E. A. (Eds.). (2022). *Reimagining education: The International Science and Evidence based Education Assessment*. UNESCO MGIEP. ISBN 978-93-91756-04-8.
- **File:** Literature/Literature on Curriculum design/Duraiappah et al - 2022 - Reimagining education The International Science and Evidence based Education WG01.pdf
- **Type:** report (international expert assessment, IPCC-style; blind peer-reviewed chapters)
- **Core claims:** Education should be reoriented from a dominant human-capital/economic purpose toward human flourishing — self-actualization and fulfilment within a community — using a "whole-brain", learner-centric approach integrating cognitive, social and emotional dimensions (Synopsis; Ch. 1–2). Flourishing-related skills can be cultivated through education like literacy and numeracy (Ch. 3).
- **Evidence/methods:** Transdisciplinary expert assessment of peer-reviewed and grey literature by 300+ experts; consensus-building process; not a student assessment like PISA (Synopsis, pp. 5–19).
- **Relevance to our paper:** Ch. 4 proposes a six-domain curricular framework (environment, culture, society, technology, interpersonal, self) and six learning trajectories — a direct content-framework reference for situating AI/digital literacy ("technology" domain incl. digital literacy and ethical engagement). Survey data: 82% of teachers see disproportionate exam focus — supports our assessment-misalignment argument. Tags: [content-frameworks] [assessment] [policy] [pedagogy]
- **Key points with locations:**
  - Six curricular domains + six learning trajectories ("learning to know and think", "to do and evaluate", "to learn", "to live together", "with nature", "to be and become") (Ch. 4, pp. 193–241)
  - Curriculum–teaching–assessment treated as an integrated dynamic system; warns against "learnification"/over-measurement citing Biesta (Ch. 4, pp. 192–195)
  - Technology domain: learners progress from familiarity → digital literacy → ethically shaping technology for flourishing (Ch. 4, p. 239)
- **Caveats:** 342 pp; read via full synopsis + chapter-level sampling (Ch. 1 p. 41ff, Ch. 2 pp. 79–82, Ch. 3 pp. 139–143, Ch. 4 pp. 192–241, Ch. 5 pp. 277–281, glossary pp. 338–339). Normative/philosophical orientation; few primary empirical analyses.

---

## [isee-wg2] Reimagining Education: ISEE Assessment — Working Group 2 volume (Education and Context)

- **Citation (APA, best effort from the document):** Duraiappah, A. K., van Atteveldt, N. M., et al. (Eds.). (2022). *Reimagining education: The International Science and Evidence based Education Assessment* (WG2 volume). UNESCO MGIEP. Chapter 8 citable as: Wals, A., Pinar, W., Macintyre, T., et al. (2022). Curriculum and pedagogy in a changing world. https://doi.org/10.56383/YUDJ7139
- **File:** Literature/Literature on Curriculum design/Duraiappah & van Atteveldt - 2022 - Reimagining education The International Science and Evidence based Education WG02.pdf
- **Type:** report (10 chapters on social, political, economic, environmental contexts of education)
- **Core claims:** Context conditions what education can achieve; uniform blueprints are "unwise and potentially dangerous" (Ch. 1, p. 45). Curriculum is not a clearly delineated, uniformly applicable concept but dynamic, evolving, contextual (Ch. 8, p. 520). Global assessment intensification (PISA/OECD, economistic agenda) narrows curricula and pressures teachers/learners (Ch. 9).
- **Evidence/methods:** Critical evidence reviews per chapter (political economy, sustainability, diversity/social justice, conflict, neuroscience, EdTech, curriculum/pedagogy, assessment, teaching profession).
- **Relevance to our paper:** Strongest external support for our Context dimension and curriculum–assessment misalignment thesis: Ch. 9 ("Assessment in context") explicitly describes how measurement-driven regimes distort curriculum; Ch. 8 covers curriculum theory traditions (Schwab, Dewey, Freire) and hybrid learning ecologies. Tags: [assessment] [policy] [pedagogy] [content-frameworks] [ethics]
- **Key points with locations:**
  - Ch. 9 key messages: excessive achievement measurement narrows curricular focus; recommends more assessment *for* and *as* learning; warns of EdTech assessment risks (pp. 643–645)
  - Ch. 8: curriculum as "complicated conversation"; place-based "living curricula" and hybrid learning ecologies; critique of EdTech fetish and textbook/test "tyranny" (pp. 520–569)
  - Ch. 3: meritocracy critique — "hereditary meritocracy", competitive intensity narrowing learning (pp. 180–181); Ch. 5: education can fuel or ameliorate conflict (p. 333)
- **Caveats:** 736 pp; read via full synopsis + chapter sampling (all 10 chapter titles verified; Ch. 8–9 read more deeply). Critical-social-science stance; few quantitative syntheses.

---

## [isee-wg3] Reimagining Education: ISEE Assessment — Working Group 3 volume (Education and the Learning Experience)

- **Citation (APA, best effort from the document):** Duraiappah, A. K., van Atteveldt, N. M., et al. (Eds.). (2022). *Reimagining education: The International Science and Evidence based Education Assessment* (WG3 volume). UNESCO MGIEP.
- **File:** Literature/Literature on Curriculum design/Duraiappah & van Atteveldt - 2022 - Reimagining education The International Science and Evidence based Education WG03.pdf
- **Type:** report (7 chapters on the science of learning: brain development, individual differences, SEL, academic foundations, learning disabilities, learning spaces)
- **Core claims:** The learning experience is intrinsically cognitive, emotional and social — no clear neural dissociation between cognition and emotion (Ch. 1, 4). Development is non-linear, individual and culture-dependent; sensitive periods in early childhood and adolescence (Ch. 2, 5). SEL improves learning outcomes by 7–11% yet constitutes only ~7%/4% of primary/secondary learning time (Synopsis, p. 13).
- **Evidence/methods:** Evidence reviews integrating neuroscience, developmental and educational psychology; SEL meta-analytic effects cited (e.g., Taylor et al., 2017).
- **Relevance to our paper:** Provides developmental/psychological grounding for age-appropriateness claims (11–12 year-olds = early adolescence, heightened emotional reactivity, still-developing regulation) and for including social-emotional and embodied/spatial aspects in curriculum evaluation; Ch. 7 on built/natural/digital learning spaces (incl. datafication/platform critique) informs our Context and safeguards dimensions. Tags: [age-appropriateness] [pedagogy] [safeguards-behaviors] [curriculum-difficulty]
- **Key points with locations:**
  - Adolescent emotional reactivity/regulation and social brain network development (Ch. 4, pp. 208–209)
  - Non-linear development; sensitive periods; nature–nurture interplay (Ch. 5, p. 287)
  - Ch. 7: datafication, platformization and learning analytics reshape learning spaces; more data ≠ better knowledge of outcomes (pp. 500–501)
- **Caveats:** 572 pp; read via synopsis + chapter sampling (Ch. 1 p. 43, Ch. 3 p. 126, Ch. 4 p. 208, Ch. 5 p. 287, Ch. 6 p. 364, Ch. 7 pp. 500–501). Broad coverage means shallow treatment per topic; chapter 2 (brain development) only minimally sampled.

---

## [isee-wg4] Reimagining Education: ISEE Assessment — Working Group 4 volume (Education: Data and Evidence)

- **Citation (APA, best effort from the document):** Duraiappah, A. K., van Atteveldt, N. M., et al. (Eds.). (2022). *Reimagining education: The International Science and Evidence based Education Assessment* (WG4 volume). UNESCO MGIEP.
- **File:** Literature/Literature on Curriculum design/Duraiappah & van Atteveldt - 2022 - Reimagining education The International Science and Evidence based Education WG04.pdf
- **Type:** report / framework (3 chapters on evidence-based education)
- **Core claims:** "What works" is insufficient; evidence-based education needs a three-step logic — causal ascription → effectiveness generalization ("what works best generally", from meta-analytic relative evidence) → local effectiveness prediction ("will it work here") — formalized as the EBE³ framework (Ch. 1). Dichotomous statistical-significance reading is misleading; effect sizes with compatibility intervals and explicit uncertainty should be standard (Ch. 2).
- **Evidence/methods:** Conceptual framework chapter; quantitative-methods chapter (EEF padlock ratings, effect sizes, months-of-learning conversion); Ch. 3 documents the EEF Evidence Database/Teaching & Learning Toolkit as proof of concept (e.g., phonics +5 months, 121 studies, very high security, pp. 167–169).
- **Relevance to our paper:** Methodological backbone for our curriculum-evaluation reporting standard: how to grade evidence strength, report uncertainty, and contextualize effectiveness claims — directly applicable to how we treat the (thin, self-report-heavy) evidence behind AI-literacy curricula. Tags: [assessment] [content-frameworks] [policy] [curriculum-difficulty]
- **Key points with locations:**
  - EBE³ framework and "relative evidence" definition; critique of single-study "what works" (Ch. 1, pp. 44–47, 85–87)
  - Worked example: identical ES = 0.10 with different CIs; significance-only interpretation "severely impedes" decisions (Ch. 2, pp. 102–104)
  - EEF database inclusion criteria (ecological validity ≥1 week/≥5 h; excludes lab studies) and Toolkit strand format (Ch. 3, pp. 127–131, 167–173)
- **Caveats:** 188 pp; read via synopsis + chapter sampling (Ch. 1 pp. 44–87, Ch. 2 pp. 102–104, Ch. 3 pp. 127–173, glossary pp. 182–184). Pro-quantitative orientation; qualitative evidence treated mainly as complementary.

---

## [wang-2024-robots-tpck] Physical Robots in Education: A Systematic Review Based on the Technological Pedagogical Content Knowledge Framework

- **Citation (APA, best effort from the document):** Wang, H., Luo, N., Zhou, T., & Yang, S. (2024). Physical robots in education: A systematic review based on the technological pedagogical content knowledge framework. *Sustainability, 16*(12), 4987. https://doi.org/10.3390/su16124987
- **File:** Literature/Literature on HandsOn/Wang et al - 2024 - Physical robots in education A systematic review based on the technological.pdf
- **Type:** review (systematic, PRISMA)
- **Core claims:** Across 92 empirical studies, physical robots are most used in language learning (37), with physical interaction the most common teaching strategy (31) and humanoid robots (esp. NAO, 31) the most common type. Evaluated learning results are predominantly cognitive (40%) > behavioral (38%) > affective (22%). Robots typically show agreeable/extroverted personalities and provide informational plus emotional support (62% of activities).
- **Evidence/methods:** WoS search (Aug 2023), 699 → 92 empirical journal studies; coded via TPCK components mapped to learning domain, teaching strategy, robot type, learning results, problems, robotic support, robotic personality.
- **Relevance to our paper:** State-of-the-art map for situating our Marty-robot curriculum; its problems catalog (novelty effect, teacher workload/expertise, distraction, younger learners' comprehension difficulty and emotional attachment, cost/fragility) feeds our Pedagogy/Didactics and safeguards analysis; cognitive-over-affective outcome bias mirrors our curriculum–assessment misalignment finding. Tags: [social-robots] [hands-on] [pedagogy] [age-appropriateness] [safeguards-behaviors] [assessment]
- **Key points with locations:**
  - Results distributions: domains, strategies, robot types, outcomes (Figs. 3–8, pp. 6–10)
  - Problems from teacher/learner/robot perspectives incl. novelty effect and shallow short interactions (Sec. 3.5, pp. 8–9)
  - Recommendation: align robot features with teaching strategy; preliminary workshops to reduce novelty effect (Sec. 4.2, 4.5, pp. 11–12)
- **Caveats:** Read in full (24 pp). WoS-only, English-only, excludes conference papers and self-report-only studies; coding-scheme dependent; TPCK mapping is loose (e.g., "robotic personality" as TPCK). Published in *Sustainability* (not an education journal); authors note superficial treatment of component interactions.

---

# Verification of existing review notes (secondary sources)

## [note-buildbots-p4] BuildBots_Paper4_Literature_Review.md

- **What it covers:** Comprehensive literature review for a related "BuildBots" study (robot assembly vs. interaction with Marty in children). Proposes a five-type activity categorization (creating/assembling/tinkering/programming/interacting), maps 29 papers to pre-registered hypotheses (H1–H13: engagement, learning, perception, anthropomorphism, attachment), and lists acquisition priorities with links.
- **Sources cited:** Papert (1980), Piaget (1975), Ackermann (2004); Freeman et al. (2014, PNAS); Ouyang & Xu (2024); Bai & Tian (2025); Hitron et al. (2019, CHI); Williams et al. (2019 AAAI PopBots; 2024 HRI Doodlebot); Druga et al. (2019); Diamond et al. (2019); Norton et al. (2012); Franke et al. (2010); Sun & Sundar (2016); Huang et al. (2013); Groom et al. (2009); IKEA-effect-robots (2024, PMC12240306); robotics & cognitive development (2023, PMC9988604); Zhong et al. (2022); Wang et al. (2024); Bullock et al. (2013); Martinez & Stager; Wilkinson & Petrich; Maker Ed resources.
- **Reliability/usability as secondary source:** Mostly reliable as a working bibliography: citations carry venues, numbers and open-access links, and the Wang et al. (2024) entry matches the actual paper (verified above). However, claims about paper contents are not verifiable without reading the originals; some entries are marked "[ACQUIRE]" or "check publication status" (Bai & Tian 2025), i.e., possibly not yet read/verified by the author; hypothesis-mapping is study-specific (BuildBots), so framing is instrumental rather than neutral. Use for citation discovery, then verify each paper directly.
- **Relevance to our paper:** The five-type hands-on activity framework (assembly vs. interaction distinction) and the ownership/demystification mechanisms are directly usable for our Pedagogy/Didactics dimensions with the Marty robot. Tags: [hands-on] [social-robots] [pedagogy] [didactics] [age-appropriateness]

## [note-categorization] categorization_framework_hands_on_activities.md

- **What it covers:** A standalone multi-dimensional framework for hands-on robot activities: 5 activity types × (teaching/learning model from Zhong et al. 2022; engineering design stages; technical domains; robot autonomy levels), with a comparative matrix (physical engagement, ownership, technical understanding, anthropomorphism, time, difficulty), psychological mechanisms and risks per type, and curriculum sequencing recommendations (interaction → assembly → programming → tinkering → creating).
- **Sources cited:** Zhong et al. (2022); Wang et al. (2024); Bullock et al. (2013); Norton et al. (2012); Franke et al. (2010); Sun & Sundar (2016); "IKEA robots (2024)"; Huang et al. (2013); Groom et al. (2009); Hitron et al. (2019); Williams et al. (2019, 2024); Ouyang & Xu (2024); Martinez & Stager; Maker Ed; Papert/Ackermann (constructionism); "MIT assembler robots (2022)" (vague, unverifiable as cited).
- **Reliability/usability as secondary source:** An original synthesis/framework document, not a literature summary — its comparative matrix cell values (e.g., "Creating = Very High ownership") are the author's reasoned judgments, not extracted data. Internally consistent and transparent about its BuildBots purpose; reference list is solid, but several mechanism claims rest on few studies. Usable as a conceptual scaffold for our curriculum's activity design; do not cite as evidence for empirical effects.
- **Relevance to our paper:** Ready-made analytical grid for characterizing Marty-based activities along engagement/ownership/anthropomorphism dimensions and for justifying activity sequencing in curriculum design. Tags: [hands-on] [pedagogy] [didactics] [content-frameworks] [curriculum-difficulty]

## [note-foundational-theory] foundational_theory_hands_on_learning.md

- **What it covers:** Establishes theoretical grounding for "hands-on learning" via five foundational sources (Dewey, Kolb, Bruner, Fleming & Mills VARK, Montessori), each with full citation, access links, key concepts and relevance; synthesizes a consensus definition (active physical engagement, enactive/kinesthetic, concrete experience) and argues that both assembly and operation of a robot count as hands-on; includes a draft introduction paragraph and acquisition links.
- **Sources cited:** Dewey (1938) *Experience and Education*; Kolb (1984/2015) *Experiential Learning*; Bruner (1966) *Toward a Theory of Instruction*; Fleming & Mills (1992) VARK; Montessori (1917) *The Advanced Montessori Method*; plus Hitron et al. (2019), Williams et al. (2019), Norton et al. (2012), Wang et al. (2024) in the application layer.
- **Reliability/usability as secondary source:** Good citation hygiene: corrected an earlier VARK date error (1992 not 2001), provides archive.org/publisher links, and explicitly flags the "learning styles" neuromyth caveat while retaining kinesthetic learning as a valid pedagogical construct — scientifically honest. However, the summaries of the five classics are standard textbook renderings; page-level claims should be checked against originals before quoting. Usable as a reliable orientation layer for theory.
- **Relevance to our paper:** Supplies the constructivist/experiential theory base (Dewey, Kolb, Bruner enactive mode) for the hands-on, robot-mediated pedagogy dimension of our curriculum and legitimizes analyzing both assembly and interaction activities. Tags: [hands-on] [pedagogy] [didactics] [age-appropriateness]

## [note-hands-on-litreview] hands-on_learning_literature_review.md

- **What it covers:** The parent literature review (29 numbered entries) underlying the other BuildBots notes: pre-registration papers (constructionism, active-learning meta-analyses, AI/robotics-specific studies, IKEA-effect/ownership studies) plus taxonomy/meta-analysis additions, key themes (engagement levels, psychological mechanisms, learning outcomes), research gaps, acquisition list and search strategy (9 documented web searches, April 2026).
- **Sources cited:** Same core set as BuildBots_Paper4 note: Papert, Piaget, Ackermann; Freeman et al. (2014); Diamond et al. (2019); Hitron et al. (2019); Williams et al. (2019, 2024); Druga et al. (2019); Huang et al. (2013); Groom et al. (2009); Norton et al. (2012); Franke et al. (2010); Sun & Sundar (2016); Zhong et al. (2022); Wang et al. (2024); Bullock et al. (2013); Bai & Tian (2025); Ouyang & Xu (2024); PMC 9988604; PMC 12240306; Martinez & Stager; Wilkinson & Petrich. One vague entry: "Effects of physically embodied educational robots (2026), J. Educational Psychology (anticipated)" — unverifiable, likely placeholder.
- **Reliability/usability as secondary source:** Transparent about provenance (search queries listed; open-access links; pre-registration origin) and largely duplicative of the BuildBots_Paper4 note (DRY issue across the folder). Full citations with venues/DOIs for most entries; weaknesses: two "anticipated"/PMC-number-only citations that need verification, and one-sentence annotations too thin to cite from. Use as the canonical acquisition checklist; verify items marked anticipated/PMC-only.
- **Relevance to our paper:** Curated, hypothesis-linked evidence base for the hands-on robotics pedagogy claims in our curriculum (engagement, learning outcomes, perception/anthropomorphism effects) — a time-saving secondary source for our Pedagogy and Didactics sections. Tags: [hands-on] [social-robots] [pedagogy] [assessment]

## [note-papers-to-acquire] papers_to_acquire.md

- **What it covers:** Pure acquisition/workflow list for the BuildBots literature: 5 high-priority open-access papers (Zhong 2022; IKEA-effect-robots 2024; robotics cognitive development 2023; Ouyang & Xu 2024; Wang et al. 2024), 5 medium-priority supplements, download/naming conventions, an annotation template, and a hypothesis-support map (H1–H13).
- **Sources cited:** Same 29-paper BuildBots corpus; links verified in the other notes for the MDPI/Frontiers/PMC items; book entries (Martinez & Stager, Wilkinson & Petrich) lack publication details.
- **Reliability/usability as secondary source:** Not a content source — a task list. Accurate as far as links/DOIs overlap with verified entries (Wang et al. 2024 DOI 10.3390/su16124987 matches the PDF reviewed above). Status flags ("check publication status" for Bai & Tian) indicate unfinished verification. Usable only for tracking acquisition state, not for claims.
- **Relevance to our paper:** Operational value only: identifies which hands-on/robotics papers the project still needs; the annotation template (methods, quotes with page numbers, critical notes) could be reused for our curriculum-paper literature pipeline. Tags: [hands-on] [social-robots]


---

<!-- ===== batch_5_root_assessment__validation_required.md ===== -->

# Literature Summaries — Batch 5 (root assessment & related)

Scope: 6 files. Summaries written after full reading of each document. Tags refer to the project's dimension/topic taxonomy.

## [aied26-intervention] Teaching Students to Question the Machine: An AI Literacy Intervention Improves Students Regulation of LLM Use in a Science Task

- **Citation (APA, best effort from the document):** Clerc, O., Abdelghani, R., Desvaux, C., Poisson, E., Oudeyer, P.-Y., & Sauzéon, H. (2026). Teaching students to question the machine: An AI literacy intervention improves students regulation of LLM use in a science task. *Proceedings of AIED 2026* (INRIA Bordeaux; University of Tübingen). OSF supplement: https://osf.io/fyu7c/
- **File:** `Literature/Clerc et al - 2026 - Teaching students to question the machine An AI literacy intervention improves.pdf`
- **Type:** empirical (controlled classroom study)
- **Core claims:** A brief (2-hour), classroom-feasible AI literacy workshop combining conceptual content (how LLMs work/fail) with procedural interaction heuristics improves middle-school students' regulation of LLM use and final-answer quality in science problem solving. Benefits operate via stronger monitoring-to-control coupling (acting on detected problems), not improved prompt discrimination per se. Self-reported GenAI attitudes/knowledge and metacognition (Jr. MAI) did not predict performance.
- **Evidence/methods:** N = 116 French students (grades 8–9, ages 13–15; intervention n = 76, control n = 40); six inquiry tasks with well-specified vs. underspecified suggested prompts; behavioral regulation measures; GPT-4o LLM-as-judge validated against humans (Krippendorff's α, advantage probability). Performance: 11.38 vs. 10.29/20, p = .040, r = .19.
- **Relevance to our paper:** Direct evidence that process/behavioral assessment reveals intervention effects invisible to self-report instruments — central to our curriculum–assessment misalignment argument; also a model of short, scalable AI literacy pedagogy near our target age. [assessment] [pedagogy] [age-appropriateness] [ai-literacy-def] [safeguards-behaviors]
- **Key points with locations:**
  - Intervention effects: less acceptance of underspecified prompts (51.5% vs. 66.7%, p = .044); more follow-up questions after underspecified prompts (59.2% vs. 27.9%, p < .001) (pp. 7–9, Figs. 3–4)
  - Null prediction by GenAI self-reports (r = 0.01) and Jr. MAI (r = 0.04); self-report vs. online regulation gap (pp. 9–11, §3.4, §4.3)
  - Workshop design: conceptual (hallucination, bias, sycophancy) + procedural heuristics; inquiry-cycle instruction (p. 5, §2.2)
- **Caveats:** Single school; no demographics collected; test 2 days post-workshop (durability unknown); modest absolute performance (~11/20); preprint-stage conference paper.

## [everyoneai-childdev] The Future of Child Development in the AI Era: Cross-Disciplinary Perspectives Between AI and Child Development Experts

- **Citation (APA, best effort from the document):** Neugnot-Cerioli, M., & Muss Laurenty, O. (2024). *The future of child development in the AI era: Cross-disciplinary perspectives between AI and child development experts*. everyone.ai. (No DOI/publisher metadata in document; year inferred from content covering events through May 2024.)
- **File:** `Literature/Neugnot-Cerioli & Laurenty - 2024 - The future of child development in the AI era Cross-disciplinary perspectives.pdf`
- **Type:** report (expert consultation + scoping literature review)
- **Core claims:** AI is becoming pervasive in children's environments (entertainment, education, conversational agents) during sensitive developmental periods (brain maturation to ~25 y), offering interactive-learning benefits but posing risks: displacement of rich sensory/social experiences, over-trust and anthropomorphization of AI agents, privacy-concept immaturity, gamification undermining intrinsic motivation, and unproven EdTech replacing effective methods. Advocates child-centered regulation, developer responsibility, and AI/human literacy education for all stakeholders.
- **Evidence/methods:** Interviews with 16 experts (AI/product development/child development; ~105 min each) plus a non-systematic literature review of child development and child–technology interaction research.
- **Relevance to our paper:** Provides developmental grounding for age-appropriateness decisions in our curriculum (11–12 y.o.), cautions on engagement-over-learning metrics, and documents children's epistemic over-trust in machines — relevant to robot-mediated instruction and safeguard behaviors. [age-appropriateness] [safeguards-behaviors] [social-robots] [hands-on] [ethics] [policy]
- **Key points with locations:**
  - Children's privacy understanding develops progressively; by age 11 comprehension improves but judgment lags (p. 11, §2.1.2)
  - Children >5 prefer technological informants; over-imitate robots; anthropomorphize (Eliza effect) and form attachments (pp. 23–24, §2.3.2)
  - EdTech critique: engagement-time metrics vs. learning; gamification shifts intrinsic→extrinsic motivation (Hanus & Fox, 2015); EVER four-pillars evaluation (pp. 18–19, §2.2.2)
- **Caveats:** Non-systematic review; small non-random expert sample; advocacy-oriented; no empirical testing of recommendations.

## [cps-ai-guidebook] AI Guidebook (Version 5.0) — Chicago Public Schools

- **Citation (APA, best effort from the document):** Chicago Public Schools. (2025). *AI guidebook* (Version 5.0, updated August 2025). CPS Office of Teaching and Learning & Department of Information and Technology Services. https://cps.edu/aiguidebook
- **File:** `Literature/Guidelines/Chicago Public Schools - 2025 - AI guidebook v50.pdf`
- **Type:** report (district policy/guidance)
- **Core claims:** CPS frames responsible GenAI adoption around five principles (equitable/accessible; ethical/transparent; human-centered; continuous improvement; accountable/sustainable) and a five-pillar AI literacy definition (foundational knowledge, practical application, ethical awareness, critical thinking, future-oriented perspective). It operationalizes policy through stakeholder-specific rules (students, parents, educators, administrators, ITS, vendors), tool vetting via the Ed Tech Catalog, and age-based access restrictions.
- **Evidence/methods:** Not empirical; governance document reviewed quarterly, issued under Board Information Security Policy 19-0828-P01, aligned with FERPA/COPPA/SOPPA.
- **Relevance to our paper:** A concrete, large-district instantiation of AI literacy definitions, age-appropriateness rules, and safeguard behaviors (citation of AI use, verification of outputs, caution about AI-detector false positives) that contextualize our curriculum's content and assessment-policy dimension. [policy] [ai-literacy-def] [safeguards-behaviors] [age-appropriateness] [ethics]
- **Key points with locations:**
  - Five-pillar AI literacy definition (p. 11, "AI Literacy")
  - Age restrictions table: ChatGPT/Perplexity 13+ with parental consent; Claude/Copilot 18+; Gemini parental consent (p. 24, "Age Appropriate Usage")
  - Caution on GenAI detection software (false positives, bias against English Learners); holistic assessment recommended (p. 25, "Monitoring Student Use"); classroom integration examples by school level (pp. 26–28)
- **Caveats:** Policy document, not research; no outcome data; US legal context (SOPPA/FERPA) limits transferability.

## [snapchat-myai-misinformation] Social Media and Artificial Intelligence—Understanding Medical Misinformation Through Snapchat's New Artificial Intelligence Chatbot

- **Citation (APA, best effort from the document):** Tandar, C. E., Bajaj, S. S., & Stanford, F. C. (2024). Social media and artificial intelligence—Understanding medical misinformation through Snapchat's new artificial intelligence chatbot. *Mayo Clinic Proceedings: Digital Health, 2*(2), 252–254. https://doi.org/10.1016/j.mcpdig.2024.04.004
- **File:** `Literature/Literature on AI Ethics/Tandar et al - 2024 - Social media and artificial intelligence—Understanding medical misinformation.md`
- **Type:** position (commentary with illustrative probing)
- **Core claims:** Snapchat's My AI — pinned by default for 383M daily users, 48% aged 15–25 — gives incomplete mental-health guidance and potentially harmful diet advice (calorie tracking, seizure diets, cutting food groups), risking misinformation and eating-disorder reinforcement in adolescents. Physicians, professional bodies, and tech companies must test chatbots, build misinformation toolkits, and integrate AI education into patient visits and digital literacy programs.
- **Evidence/methods:** Informal case study: authors posed mental-health, social, and diet questions to My AI and compared responses with physician practice; supported by cited literature, not systematic methods.
- **Relevance to our paper:** Concrete exemplar of why safeguard behaviors and critical evaluation of AI outputs must be taught to near-adolescent learners; supports our curriculum's ethics/critical-thinking content and the need to assess protective behaviors, not just knowledge. [safeguards-behaviors] [ethics] [age-appropriateness] [ai-literacy-def]
- **Key points with locations:**
  - My AI hallucination and harmful suggestions to minors (booze/sex advice to 13–15 y.o., per Washington Post) (p. 252, opening)
  - Chatbot's incomplete depression advice vs. physician follow-up questioning (p. 252, Fig. 1); eating-disorder-risk diet advice (p. 253, Fig. 2)
  - Mitigation proposals: clinician testing of chatbots, NAM/AMA toolkits, physician-approved training data, digital literacy programs (pp. 253–254)
- **Caveats:** 3-page commentary; anecdotal probes without systematic protocol; health-domain focus, not education; Markdown conversion has OCR artifacts but content fully legible.

## [pisa2029-mail] Navigating an Evolving Digital World: First Draft of the PISA 2029 Media and Artificial Intelligence Literacy (MAIL) Assessment Framework

- **Citation (APA, best effort from the document):** OECD. (2026). *Navigating an evolving digital world: First draft of the PISA 2029 Media and Artificial Intelligence Literacy (MAIL) Assessment Framework* (L. F. Vargas-Madriz, M. Piacentini, & the MAIL Expert Group). OECD. (Preliminary draft, subject to revision.)
- **File:** `Literature/OECD - 2026 - Navigating an evolving digital world PISA 2029 MAIL assessment framework first draft.pdf`
- **Type:** framework (international assessment framework)
- **Core claims:** MAIL is defined as the set of competences required to engage effectively, ethically and responsibly with digital content, media platforms and AI systems, structured around five competences — Reflect & Act Ethically and Responsibly (transversal), Access & Use, Analyse & Evaluate, Participate & Collaborate, Create — and three conceptual pairs (authors/audiences, messages/meanings, representations/realities). Assessment uses authentic short and long tasks across five purposes (relationships, learning, entertainment, persuasion, citizenship), with ~50% of time on Analyse & Evaluate + Create, plus questionnaires on attitudes, exposure and practices.
- **Evidence/methods:** Expert-group framework synthesis (OECD Secretariat + MAIL Expert Group), building on the EC-OECD AI Literacy Framework (OECD, 2025); includes draft low/intermediate/high student expectation progressions per competence.
- **Relevance to our paper:** The reference assessment framework for our paper's assessment dimension — its competence model, difficulty drivers, and performance-based task design are the benchmark against which our curriculum–assessment alignment findings are interpreted. [assessment] [content-frameworks] [ai-literacy-def] [curriculum-difficulty] [age-appropriateness]
- **Key points with locations:**
  - MAIL definition + five-competence model with transversal ethics (p. 25, Fig. 4.1; §4.1–4.5, pp. 26–35)
  - Difficulty drivers: context complexity, media diversity, tool variety, higher-order demands, open-endedness, authenticity, instruction ambiguity, scaffolding amount (pp. 44–45, §5.1.5)
  - Example long task: journalist lateral-reading scenario in simulated browser/chat environment (pp. 47–51, §5.2); questionnaire constructs incl. misinformation/manipulation susceptibility, AI literacy exposure (pp. 45–46, Table 5.2)
- **Caveats:** Explicitly a preliminary first draft (progressions to be revised after pilot/field trial); targets PISA's 15-year-olds, older than our 11–12 cohort; no psychometric results yet.

## [aied26-supplement] Supplementary Materials for "A Brief, Classroom-Feasible AI Literacy Intervention Improves Middle-School Students' Regulation of LLM-Based Problem Solving"

- **Citation (APA, best effort from the document):** [Anonymized authors]. (2026). *Supplementary materials for "A brief, classroom-feasible AI literacy intervention improves middle-school students' regulation of LLM-based problem solving."* Content identifies it as the supplement to the Clerc et al. AIED 2026 paper summarized above (same tasks, questionnaires, workshop, OSF link).
- **File:** `Literature/Anonymized authors - 2026 - Supplementary materials for A brief, classroom-feasible AI literacy.pdf`
- **Type:** empirical (supplementary materials: instruments, intervention content, validation protocols, extra analyses)
- **Core claims:** Documents the full measurement and intervention apparatus of the AIED26 study: French Jr. MAI (18 items) and adapted GenAI questionnaire (24 items, 6 subscales), the 2-hour workshop's pedagogical materials (bias, sycophancy, hallucination demonstrations; iterative predict→prompt→evaluate→revise cycle), and a rigorous LLM-as-judge validation protocol. Reports weak reliability for some GenAI subscales (Fairness & Ethics α = .26; E&EoU α = .42; SI α = .50), justifying cautious secondary use of self-reports.
- **Evidence/methods:** GPT-4o annotation validated via Krippendorff's α non-inferiority (δ = –0.05) and advantage-probability (ω = 1.00) vs. human raters; prompt-manipulation discrimination score D (final set mean 19.79/20) robust across 4 model backends.
- **Relevance to our paper:** A methodological template for our assessment dimension: validated LLM-as-judge scoring, behavioral process measures, and transparent reliability reporting — plus ready-made workshop didactics for teaching LLM failure modes. [assessment] [didactics] [pedagogy] [safeguards-behaviors] [ai-literacy-def]
- **Key points with locations:**
  - Questionnaire items + Cronbach's α values, incl. weak GenAI subscales (pp. 1–3, §S2)
  - Workshop materials: stereotype-bias image generation, sycophancy, hallucination examples; prompting task (pp. 3–5, §S3)
  - LLM-as-judge validation protocol and prompt discrimination results (pp. 6–9, §S4); follow-up behavior detail: 59.2% vs. 27.9%, p = .0003 (pp. 10–11, §S5.5)
- **Caveats:** Anonymized for review (authorship inferred from content match with the AIED26 paper); figures referenced but not rendered in text extraction; French-language instruments limit direct reuse.


---

<!-- ===== batch_6_llm_safety_childfacing__validation_required.md ===== -->

# Batch 6 — LLM Safety (Child-Facing) Literature Summaries

Summaries written after full reading of each source. Base path: `Literature/Literature on LLM safety/`.

---

## [educ-agents] AI-Powered Educational Agents: Opportunities, Innovations, and Ethical Challenges
- **Citation (APA, best effort from the document):** Córdova-Esparza, D.-M. (2025). AI-powered educational agents: Opportunities, innovations, and ethical challenges. *Information, 16*(6), 469. https://doi.org/10.3390/info16060469
- **File:** `Córdova-Esparza - 2025 - AI-powered educational agents Opportunities, innovations, and ethical challenges.pdf` (read via pre-extracted twin `Córdova-Esparza - 2025 - AI-powered educational agents Opportunities, innovations, and ethical challenges.txt`; PDF first page verified to match)
- **Type:** review (systematic literature review)
- **Core claims:** Hybrid human–AI workflows (teachers curating/moderating LLM output) outperform fully autonomous tutors. Technical choices (RAG, prompt engineering, fine-tuning, multi-agent debate) map onto pedagogical goals; evidence converges on five themes: retrieval grounding reduces hallucination, guardrails preserve integrity, multi-agent debate boosts accuracy, affective scaffolds raise persistence, co-orchestration mitigates equity risks.
- **Evidence/methods:** PRISMA-based 4-phase review of 82 studies (2023–Feb 2025, Scopus + Google Scholar), coded into six categories; author notes short study horizons, small samples, positive-result bias.
- **Relevance to our paper:** Strong support for the paper's hybrid design (Marty + LLM with teacher orchestration) and its Content/Didactics dimensions (guardrails, Socratic prompts, RAG grounding); its ethics section links to UNESCO/EC frameworks we also analyze. Tags: [content-frameworks] [pedagogy] [didactics] [safeguards-behaviors] [ethics] [assessment]
- **Key points with locations:** 32% error rate in GPT-generated algebra hints, errors reproduced by students (Sec. 3.6.1, citing Pardos & Bhandari); design principles for educational agents incl. "ethical and safe interaction" (Sec. 3.1.2); privacy/FERPA/GDPR mitigations incl. PII scrubbing, VPC deployment (Sec. 3.6.3).
- **Caveats:** Single-author review; corpus skews to higher education (little K-12/child focus); mixes peer-reviewed and industry sources.

---

## [constitutional-ai] Constitutional AI: Harmlessness from AI Feedback
- **Citation (APA, best effort from the document):** Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., … Kaplan, J. (2022). *Constitutional AI: Harmlessness from AI feedback* (arXiv:2212.08073). Anthropic.
- **File:** `Bai et al - 2022 - Constitutional AI Harmlessness from AI feedback.pdf` (read via twin `Bai et al - 2022 - Constitutional AI Harmlessness from AI feedback.txt`; PDF first page verified). **Duplicate check:** `Constitutional AI: Harmlessness from AI Feedback copy.pdf` differs in MD5 from the main PDF but shows identical title, author list, and abstract — treated as the same document and read once.
- **Type:** empirical (methods + experiments)
- **Core claims:** A harmless, non-evasive assistant can be trained with no human harm labels: the model critiques and revises its own outputs against a short natural-language "constitution" (supervised stage), then AI-generated preference labels train a preference model for RL from AI Feedback (RLAIF). RL-CAI matches or exceeds RLHF harmlessness while being far less evasive.
- **Evidence/methods:** Experiments on models up to 52B; 182,831 red-team prompts (42,496 human-written); Elo comparisons by crowdworkers; chain-of-thought improves AI harm identification toward preference-model accuracy.
- **Relevance to our paper:** Direct grounding for our curriculum's "training-time vs prompt-time safeguards" distinction: the constitution is the canonical example of training-time, principle-based behavioral control, and one of its 16 SL-CAI principles is explicitly age-appropriateness for children. Tags: [safeguards-behaviors] [content-frameworks] [ethics] [age-appropriateness]
- **Key points with locations:** Two-stage SL (critique→revision) + RLAIF pipeline (Fig. 1, Sec. 1.2); child-appropriateness principle in the constitution ("Did the assistant's preceding response include anything that may be inappropriate for young children?… revise to be more age-appropriate", Appendix C.1); over-training can cause Goodharting/boilerplate (Sec. 4.3).
- **Caveats:** arXiv v1 preprint (Dec 2022); principles chosen "ad hoc" by authors; dual-use concerns acknowledged (Sec. 6.2).

---

## [llm-edu-ethics] Ethical Considerations for Companies Implementing LLMs in Education Software
- **Citation (APA, best effort from the document):** Kontche Steve, M. (2024). Ethical considerations for companies implementing LLMs in education software. *International Journal of Innovative Science and Research Technology, 9*(8), 1856–1861. https://doi.org/10.38124/ijisrt/IJISRT24AUG1297
- **File:** `Steve - 2024 - Ethical considerations for companies implementing LLMs in education software.pdf` (read in full from PDF)
- **Type:** position
- **Core claims:** Companies integrating LLMs into education software must address five ethical challenges: data privacy, over-reliance on AI (eroding critical thinking), algorithmic bias, misinformation/content accuracy, and equitable access (digital divide). Recommends robust privacy policies (GDPR/HIPAA/FERPA), human-oversight features (manual overrides), AI-literacy training for educators, supplementary (not replacement) use, and standardized impact assessments.
- **Evidence/methods:** None — argumentative position paper with brief literature touchpoints (LLM history, example commercial apps per school level); cites UNESCO Education 2030.
- **Relevance to our paper:** Supplies a vendor/policy-side ethics checklist echoing our curriculum's rationale (children guided to critically evaluate AI output); the over-reliance and equitable-access arguments motivate our safeguards-behaviors content. Tags: [ethics] [policy] [safeguards-behaviors] [ai-literacy-def]
- **Key points with locations:** Five ethical challenges with company perspective (pp. 3–4, Sec. "Key Challenges and Risks"); practical recommendations incl. human oversight and educator AI-literacy training (p. 4, Sec. III); UNESCO human-centered AI quote (p. 4).
- **Caveats:** Low-tier journal (IJISRT), single author, no empirical data, some citation inaccuracies (e.g., GPT paper attributed to "Ilya Sutskever et al."; two different works both cited as [4]). Use cautiously as a secondary/opinion source.

---

## [discrim-eval] Evaluating and Mitigating Discrimination in Language Model Decisions
- **Citation (APA, best effort from the document):** Tamkin, A., Askell, A., Lovitt, L., Durmus, E., Joseph, N., Kravec, S., Nguyen, K., Kaplan, J., & Ganguli, D. (2023). *Evaluating and mitigating discrimination in language model decisions* (arXiv:2312.03689). Anthropic.
- **File:** `Tamkin et al - 2023 - Evaluating and mitigating discrimination in language model decisions.pdf` (read in full)
- **Type:** empirical / benchmark (evaluation methodology)
- **Core claims:** Presents a scalable method to measure LM discrimination in high-stakes decisions before deployment: LM-generated prompts across 70 decision scenarios with systematically varied demographics. Claude 2.0 shows mixed positive discrimination (toward women, non-binary, non-white subjects) and negative discrimination (against people >60); prompt-based interventions ("Illegal to discriminate", "Ignore demographics") reduce discrimination scores near zero while keeping ~92% correlation with original decisions.
- **Evidence/methods:** 9,450 decision questions (explicit demographics) plus name-based implicit variants; mixed-effects regression on logit p(yes); human validation of template quality (mean 4.76/5); dataset released on HuggingFace (Anthropic/discrim-eval).
- **Relevance to our paper:** Concrete, classroom-translatable demonstration that LLM outputs change with demographic wording — usable evidence/example for our bias and "verify AI output" content and for explaining prompt-level mitigation (a prompt-time safeguard). Tags: [safeguards-behaviors] [ethics] [ai-literacy-def] [assessment]
- **Key points with locations:** Method overview and "yes = positive outcome" design (Fig. 1, Sec. 2); discrimination patterns by age/race/gender, explicit vs. names (Fig. 2–3, Sec. 3.3); intervention tradeoff: low discrimination + high decision correlation (Fig. 6, Sec. 5.4).
- **Caveats:** Hypothetical scenarios (external validity limits acknowledged); single model (Claude 2.0); only age/race/gender; authors explicitly do not endorse LM use for these decisions. Adult decision contexts, not child-facing.

---

## [youthsafe] YouthSafe: A Youth-Centric Safety Benchmark and Safeguard Model for Large Language Models
- **Citation (APA, best effort from the document):** Yu, Y., Liu, Y., Zhang, J., Huang, Y., & Wang, Y. (2025). YouthSafe: A youth-centric safety benchmark and safeguard model for large language models. In *Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security (CCS '25)*, Taipei, Taiwan (arXiv:2509.08997). University of Illinois Urbana–Champaign.
- **File:** `Yu et al - 2025 - YouthSafe A youth-centric safety benchmark and safeguard model for large.pdf` (read in full)
- **Type:** benchmark + empirical
- **Core claims:** Introduces YAIR, the first youth-centric youth–GenAI safety benchmark (12,449 annotated snippets, 91 low-level risk types in a 3-tier taxonomy incl. grooming, boundary violation, emotional overreliance), showing existing moderation systems (OpenAI Moderation, Perspective API, LLaMA Guard3, WildGuard, Aegis) badly underperform on youth risks (F1 0.09–0.73). Their fine-tuned YouthSafe model reaches F1 0.88 / AUPRC 0.94.
- **Evidence/methods:** IRB-approved collection of 344 real chat logs from 15 US youth (13–21) across ChatGPT, Character.ai, etc., plus 1,572 LLM-generated synthetic dialogues; 3-expert annotation (IRR 0.84); machine+human validation (Cohen's κ 0.82); Aegis-based fine-tune evaluated on held-out human-validated test set.
- **Relevance to our paper:** The most central source in this batch: empirically validates exactly the gap our curriculum targets (mainstream safeguards miss youth-specific harms like emotional overreliance, undue influence, developmental harm) and provides a risk taxonomy and mitigation vocabulary for our safeguards content. Tags: [safeguards-behaviors] [age-appropriateness] [content-frameworks] [assessment] [ethics]
- **Key points with locations:** Three-tier youth-risk taxonomy with 6 high-level domains (Fig. 1, Sec. 3.1); false-negative rates 57–100% for baselines on developmental harm/undue influence vs. 17% for YouthSafe (Sec. 4.3.1, Fig. 3); role-play contexts cause borderline false positives (Sec. 4.3.4).
- **Caveats:** Focuses on teens 13–17/young adults 18–21, not our 11–12 age band (their synthetic prompts target ages 13–17); small real-world sample (n=15); snippet-based (single-turn-pair) evaluation; 13 risk types could not be synthesized; preprint (arXiv v1, Sep 2025).

---

## [gabriel-alignment] Artificial Intelligence, Values, and Alignment
- **Citation (APA, best effort from the document):** Gabriel, I. (2020). Artificial intelligence, values, and alignment. *Minds and Machines, 30*(3), 411–437. https://doi.org/10.1007/s11023-020-09539-2
- **File:** `Gabriel - 2020 - Artificial intelligence, values, and alignment.pdf` (read in full; title/authors identified from content — Iason Gabriel, DeepMind)
- **Type:** position / framework (philosophy)
- **Core claims:** Three propositions: (1) normative and technical aspects of AI alignment are interrelated (RL's optimizer structure fits consequentialism better than rights-based theories); (2) alignment targets differ fundamentally — instructions, expressed intentions, revealed preferences, informed preferences, interests/well-being, values — and a principle-based approach combining human direction with objective constraints is superior; (3) the central challenge is not finding the "true" morality but fair principles that gain reflective endorsement despite pluralism, via global overlapping consensus (human rights), veil of ignorance, or democratic/social-choice processes.
- **Evidence/methods:** Conceptual/philosophical analysis drawing on political theory (Rawls), moral philosophy, and ML literature.
- **Relevance to our paper:** The foundational theoretical justification for rule/principle-based AI governance that our curriculum teaches children (why an AI "constitution" or rules exist at all, and whose values they encode) — supports our content on safeguards and ethics discussions. Tags: [ethics] [content-frameworks] [safeguards-behaviors] [policy]
- **Key points with locations:** Six candidate alignment targets i–vi with critiques (Sec. 3, pp. 417–424); "alignment problem is political not metaphysical" + three fair-selection mechanisms (Sec. 4, pp. 425–432); technical methods constrain loadable values — RL vs. rights/satisficing (Sec. 2, pp. 413–417).
- **Caveats:** Pre-LLM (2020); no empirical component; abstract — needs heavy translation before use in child-facing claims; single-author (though peer-reviewed).

---

## [sparrow] Improving Alignment of Dialogue Agents via Targeted Human Judgements
- **Citation (APA, best effort from the document):** Glaese, A., McAleese, N., Trębacz, M., Aslanides, J., Firoiu, V., Ewalds, T., … Irving, G. (2022). *Improving alignment of dialogue agents via targeted human judgements*. DeepMind. (Sparrow technical report, September 2022; later arXiv:2209.14375)
- **File:** `Glaese et al - 2022 - Improving alignment of dialogue agents via targeted human judgements.pdf` (read in full, 77 pp.; title/authors identified from content — DeepMind's Sparrow paper)
- **Type:** empirical (system + methods)
- **Core claims:** Sparrow, a 70B information-seeking dialogue agent, is trained via RLHF with two additions: (1) decomposing good dialogue into 23 fine-grained natural-language rules rated separately (targeted judgements, rule-conditional reward model); (2) showing inline web evidence so raters can verify factual claims. Result: preferred over prompted baselines, breaks targeted rules only 8% of the time under adversarial probing, evidence-supported answers rated supported & plausible 78% of the time; but RL tuning amplifies distributional stereotype biases.
- **Evidence/methods:** Human per-turn preference + adversarial probing data; Preference RM + Rule RM; A2C RL with self-play and LM red-teaming; evaluations incl. Winogender/Winobias/BBQ bias, MMLU/TruthfulQA alignment tax.
- **Relevance to our paper:** The canonical "rule-based safeguards for a conversational agent" system: its self-anthropomorphism rules ("do not pretend to have a body/feelings/human identity") are exactly the deception/anthropomorphism-resistance content our curriculum teaches; evidence-citation mechanism models the "verify AI claims" behavior. Tags: [safeguards-behaviors] [content-frameworks] [ethics] [ai-literacy-def]
- **Key points with locations:** 23 rules incl. self-anthropomorphism cluster with rationale "Anthropomorphising systems can lead to overreliance or unsafe use" (Table 14, App. F); specific rules beat general "harm" rule for probing and annotation agreement (Sec. 3.5); RL increases stereotype bias scores (Sec. 3.6, Fig. 15); sample dialogue where agent denies personhood (Fig. 1).
- **Caveats:** Technical report, not peer-reviewed at time of writing; adult crowdworker context; Google Search dependence; authors note rules are incomplete and dual-use.

---

## [note-safe-companions] SAFE AI Companions Task Force Pre-Reading Summaries.md
- **What it covers:** Annotated pre-reading pack (15 items) for a "SAFE AI Companions" task force, shared via an everyone.ai partner Google Doc. Covers AI companionship risks and policy: Meta's leaked content-risk standards permitting sensual chats with minors (Reuters), the Adam Raine/ChatGPT suicide lawsuit (NBC), "My Boyfriend is AI" Reddit study (MIT Media Lab), emotional attachment & EU law, EU AI Act summary (FLI), Common Sense Media teen-trust survey, Alan Turing Institute survey on children (8–12) & GenAI, EDSAFE AI literacy blueprint/SAFE framework, smart-speaker child study, prosocial AI principles (Rithm Project), AI welfare (Eleos), Gallup teacher AI-time-savings, US Bank model benchmarking.
- **Sources cited:** Each entry links to a Google Drive copy of the underlying primary source (news articles, NGO reports, academic studies); the file itself adds no independent citations beyond those documents.
- **Reliability/usability as secondary source:** LOW as a citable source. The file explicitly states summaries were "generated with the assistance of ChatGPT" — risk of subtle distortion is real, and figures (percentages, dates) were not verified against primaries. Underlying items are mostly credible (Reuters, NBC, Common Sense Media, Turing Institute, MIT Media Lab preprint). Usable only as a discovery/orientation map: any claim must be re-verified against the linked primary before citation. Several Drive links may be access-restricted.
- **Relevance to our paper:** Highly on-topic orientation for our child-facing LLM safety motivation: child–AI emotional attachment, deceptive/anthropomorphic design, and current policy (EU AI Act, EDSAFE) — matches our curriculum's deception-resistance and safe-interaction strands. Tags: [safeguards-behaviors] [age-appropriateness] [policy] [social-robots] [ethics]


---

<!-- ===== batch_7_llm_safety_technical__validation_required.md ===== -->

# Batch 7: LLM Safety Technical Literature — Structured Summaries

**Scope:** Technical literature on LLM self-correction, error detection, verification, safety bypass, prompting infrastructure, and AI policy. Read for the AI & digital literacy curriculum paper (Marty robot, ages 11–12; 5 dimensions: Context, Content, Pedagogy, Didactics, Assessment). Primary use: support claims that LLM safeguards are imperfect and actively researched (training-time vs. prompt-time layers), and that error detection/self-correction is an open research problem.

**Reading note:** All 10 files were read via auto-converted PDF text. Papers 1, 2, 5, 6, 7, 8, 9, 10 read end-to-end. Papers 3 (CRITIC, 78 pp.) and 4 (ReaLMistake, 46 pp.) read in full for the main text; their long appendices (mostly prompt listings and worked examples) were read representatively (error analysis, ablations, data-creation sections).

---

## [self-correction-survey] Automatically Correcting Large Language Models: Surveying the Landscape of Diverse Self-Correction Strategies

- **Citation (APA, best effort from the document):** Pan, L., Saxon, M., Xu, W., Nathani, D., Wang, X., & Wang, W. Y. (2024). Automatically correcting large language models: Surveying the landscape of diverse automated correction strategies. *Transactions of the Association for Computational Linguistics, 12*, 484–506. (arXiv:2308.03188)
- **File:** Literature on LLM safety/Pan et al - 2024 - Automatically correcting large language models Surveying the landscape of.pdf
- **Type:** review
- **Core claims:** LLMs exhibit hallucination, unfaithful reasoning, toxicity, and flawed code; a promising remedy is self-correction with *automated* feedback (from the LLM itself, other models, tools, or knowledge sources), reducing reliance on costly human feedback. The paper taxonomizes correction along five axes: what is corrected, feedback source, feedback format, when feedback is applied (training-time, generation-time, post-hoc), and refinement strategy.
- **Evidence/methods:** Narrative survey with a conceptual framework (Language Model = patient, Critic = doctor, Refine model = treatment) and two large tables cataloguing ~70 representative works (RLHF, Self-Refine, Reflexion, CRITIC, SelfCheckGPT, multi-agent debate, etc.).
- **Relevance to our paper:** Directly supports the curriculum's distinction between training-time safeguards (RLHF, self-training) and prompt/generation-time safeguards (decoding guidance, post-hoc critique) — the exact layering taught with Marty. Confirms correction is an active, unresolved research area. Tags: [safeguards-behaviors] [content-frameworks] [ai-literacy-def]
- **Key points with locations:**
  - Taxonomy of correction timing (training / generation / post-hoc), §2.5, pp. 4–5
  - Post-hoc self-correction needs powerful LLMs; small models struggle to refine (§5.1, p. 11)
  - Open problems: no robust metrics for self-correction ability; continual self-improvement unstable (§7, pp. 15–16)
- **Caveats:** Published Aug 2023 (v2); fast-moving field, so recent methods are absent. Survey asserts effectiveness but later work (e.g., Huang et al. 2024, cited by others in this batch) shows intrinsic self-correction often fails without external feedback.

---

## [correctbench] CorrectBench: Automatic Testbench Generation with Functional Self-Correction using LLMs for HDL Design

- **Citation (APA, best effort from the document):** Qiu, R., Zhang, G. L., Drechsler, R., Schlichtmann, U., & Li, B. (2024). CorrectBench: Automatic testbench generation with functional self-correction using LLMs for HDL design. *arXiv preprint* arXiv:2411.08510.
- **File:** Literature on LLM safety/Qiu et al - 2024 - CorrectBench Automatic testbench generation with functional self-correction.pdf
- **Type:** empirical
- **Core claims:** LLM-generated hardware testbenches contain functional errors due to LLM instability (hallucination, "laziness"); adding functional self-validation and self-correction lifts pass rates from 33.33% (direct LLM generation) / 52.18% (prior AutoBench) to 70.13%. A validator using ~20 LLM-generated "imperfect" RTLs in an RTL-Scenario matrix reaches 88.85% validation accuracy.
- **Evidence/methods:** Experiments on 156 Verilog tasks (81 combinational, 75 sequential) with GPT-4o, Claude-3.5-Sonnet, GPT-4o-mini; two-stage "why-where-how" chain-of-thought corrector; ablations over validation criteria (50%/70%/100%-wrong).
- **Relevance to our paper:** Concrete evidence that LLM outputs need external validation loops and iterative correction to be trustworthy — supports the lesson that AI errors are normal and checkable. Tags: [safeguards-behaviors] [assessment]
- **Key points with locations:**
  - Main results: 70.13% vs 52.18% vs 33.33% Eval2 pass ratio (Table I, p. 5)
  - Corrector contributes 34.33% of validator-identified gains (§IV-B, Table III, p. 5)
  - Sequential circuits nearly 5× baseline after correction (§I, p. 1)
- **Caveats:** Hardware-design domain (HDL testbenches), not education; usable only as analogous evidence about LLM error-proneness and correction loops. Validation criterion (70%-wrong) acknowledged as possibly non-optimal.

---

## [critic] CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

- **Citation (APA, best effort from the document):** Gou, Z., Shao, Z., Gong, Y., Shen, Y., Yang, Y., Duan, N., & Chen, W. (2024). CRITIC: Large language models can self-correct with tool-interactive critiquing. *International Conference on Learning Representations (ICLR) 2024*. (arXiv:2305.11738)
- **File:** Literature on LLM safety/Gou et al - 2024 - CRITIC Large language models can self-correct with tool-interactive critiquing.pdf
- **Type:** empirical
- **Core claims:** Black-box LLMs can verify and amend their own outputs by interacting with external tools (search engines, code interpreters, toxicity APIs) in a verify-then-correct loop. CRITIC improves QA F1 by up to 7.7 points, math program synthesis by up to 7.0 points, and reduces toxicity probability by 79.2% — *without* extra training. Crucially, pure self-correction without external feedback yields marginal or even negative gains: LLMs are unreliable at validating their own outputs.
- **Evidence/methods:** In-context learning experiments on AmbigNQ/TriviaQA/HotpotQA, GSM8k/SVAMP/TabMWP, and RealToxicityPrompts with ChatGPT, text-davinci-003, LLaMA-2 (7B/13B/70B); ablations (CRITIC w/o Tool), oracle settings, manual error analysis (100 HotpotQA cases; 1319 GSM8k samples).
- **Relevance to our paper:** Strong evidence that (a) safeguards/self-checks fail without external grounding, (b) tool-based verification works — an accessible narrative for "why the robot double-checks." Tags: [safeguards-behaviors] [pedagogy] [didactics]
- **Key points with locations:**
  - "CRITIC w/o Tool" ablation: own critiques add ~0–2 F1, sometimes degrade performance (§4.1, p. 7)
  - Hallucination errors cut 36%→7% on HotpotQA, but 14.3% of corrections are wrong corrections (App. D.2, pp. 25–26)
  - Self-Eval barely above random (54%) at verifying own answers (App. D.1, pp. 24–25)
- **Caveats:** 78-page version with extensive prompt appendices; main text fully read, appendix read representatively. Results from 2023-era models (GPT-3.5, LLaMA-2); tool pipelines (Google scraping) affect reproducibility.

---

## [realmistake] Evaluating LLMs at Detecting Errors in LLM Responses

- **Citation (APA, best effort from the document):** Kamoi, R., Das, S. S. S., Lou, R., Ahn, J. J., Zhao, Y., Lu, X., Zhang, N., Zhang, Y., Zhang, R. H., Vummanthala, S. R., Dave, S., Qin, S., Cohan, A., Yin, W., & Zhang, R. (2024). Evaluating LLMs at detecting errors in LLM responses. *Conference on Language Modeling (COLM) 2024*. (arXiv:2404.03602)
- **File:** Literature on LLM safety/Kamoi et al - 2024 - Evaluating LLMs at detecting errors in LLM responses.pdf
- **Type:** benchmark
- **Core claims:** Introduces ReaLMistake, the first benchmark of objective, realistic, diverse errors in LLM responses (900 expert-annotated instances across math problem generation, fine-grained fact verification, answerability classification; four error categories: reasoning correctness, instruction-following, context-faithfulness, parameterized knowledge). Finding: even GPT-4 and Claude 3 detect LLM errors at very low recall; all 12 tested LLM detectors perform far below expert humans (95.7 F1).
- **Evidence/methods:** 14 expert annotators, 90 hours, ~6 min/instance; evaluation of 12 LLMs (7 open, 5 closed) as zero-shot error detectors; prompt-sensitivity (wording/position bias) and improvement-method analyses (self-consistency, majority vote, evaluation steps — none help).
- **Relevance to our paper:** Strong empirical support that automated checking of AI output is unreliable — justification for teaching children critical scrutiny rather than trust. Tasks use only high-school-level math/Wikipedia knowledge. Tags: [safeguards-behaviors] [assessment] [curriculum-difficulty]
- **Key points with locations:**
  - Stronger LLMs: higher precision but *lower* recall in error detection (§4.1, Fig. 5, pp. 7–8)
  - GPT-4 errs on >50% of benchmark tasks despite simple inputs (§3.1, Table 2, p. 5)
  - Detection recall sensitive to prompt wording (+16.9%) and option order (+27.2%) (§4.3, p. 9)
- **Caveats:** 46-page paper; appendix (annotation instructions, data examples) read representatively. Benchmark tasks are NLP-specific; detectors evaluated zero-shot only. Human benchmark based on 35 cases per setting.

---

## [output-constraints-attack] Output Constraints as Attack Surface: Exploiting Structured Generation to Bypass LLM Safety Mechanisms

- **Citation (APA, best effort from the document):** Zhang, S., Zhao, J., Xu, R., Feng, X., & Cui, H. (2025). Output constraints as attack surface: Exploiting structured generation to bypass LLM safety mechanisms. *arXiv preprint* arXiv:2503.24191. (Work in progress)
- **File:** Literature on LLM safety/Zhang et al - 2025 - Output constraints as attack surface Exploiting structured generation to bypass.pdf
- **Type:** empirical
- **Core claims:** Structured-output APIs (JSON schema, grammars) expose a *control-plane* attack surface orthogonal to prompt-level (data-plane) attacks. The proposed Constrained Decoding Attack (CDA), instantiated as (Chain) Enum Attack, hides malicious intent in schema grammar rules while the visible prompt stays benign, achieving 96.2% average attack success rate across GPT-4o, GPT-4o-mini, Gemini-2.0-flash, and five open-weight models with a single query — bypassing both external guardrails and internal alignment.
- **Evidence/methods:** Black-box attacks on 3 proprietary + 5 open-weight LLMs over five safety benchmarks (AdvBench, HarmBench, JailbreakBench, SorryBench, StrongREJECT); token-distribution analysis on Phi-3.5-MoE showing alignment concentrated in initial tokens ("shallow safety alignment").
- **Relevance to our paper:** Powerful, concrete demonstration that safeguards are imperfect and actively researched — including that safety alignment is shallow and prompt auditing has blind spots. Direct support for the curriculum's core claim. Tags: [safeguards-behaviors] [ethics]
- **Key points with locations:**
  - GPT-4o baseline 1.1% ASR vs Enum Attack 100% ASR on AdvBench (§3, §4.1.1, pp. 6–8)
  - Cross-benchmark average 96.2% ASR, 82.6% StrongREJECT (Table 4, p. 11)
  - "Output auditing is not a silver bullet" — BenignEnumAttack deadlocks auditors (Finding 2, §6, p. 12); mitigations: safety-preserving grammars, token provenance (§6, p. 12)
- **Caveats:** arXiv work-in-progress (Mar 2025), not peer-reviewed; contains harmful-content examples (content warning). Responsible-disclosure claims (OpenAI/Gemini notified) not independently verifiable.

---

## [lmql] Prompting Is Programming: A Query Language for Large Language Models

- **Citation (APA, best effort from the document):** Beurer-Kellner, L., Fischer, M., & Vechev, M. (2023). Prompting is programming: A query language for large language models. *Proceedings of the ACM on Programming Languages, 7*(PLDI), Article 186. https://doi.org/10.1145/3591300
- **File:** Literature on LLM safety/Beurer-Kellner et al - 2023 - Prompting is programming A query language for large language models.pdf
- **Type:** empirical (systems)
- **Core claims:** Proposes Language Model Programming (LMP): prompting generalized to scripting + output constraints, implemented as LMQL, a SQL-like query language with declarative constraints enforced *during* decoding via token masks. LMQL expresses advanced prompting schemes (chain-of-thought, ReAct, tool use) concisely, cuts inference cost 26–85% (billable tokens), and maintains or slightly improves accuracy.
- **Evidence/methods:** Formal eager partial-evaluation semantics (final/follow annotations, Brzozowski-derivative soundness proof); three case studies (Odd One Out/Date Understanding, ReAct on HotpotQA, GSM8k arithmetic) on GPT-J-6B, OPT-30B, GPT-3.5; metrics: LOC, model queries, decoder calls, billable tokens.
- **Relevance to our paper:** Foundational for understanding *constrained decoding* — the same mechanism weaponized by the CDA paper; useful to explain how output can be steered/restricted technically (a prompt-time layer). Tags: [safeguards-behaviors] [content-frameworks]
- **Key points with locations:**
  - LMQL syntax: decoder/query/from/where/distribute clauses (§3, Fig. 5, p. 8)
  - Constraints can force outputs the model "would have never explored" (§2.3, p. 7)
  - Cost reductions: 76% billable tokens on ReAct; 85% on arithmetic (§6.2–6.3, Table 5, pp. 20–21)
- **Caveats:** PLDI venue (programming languages), not safety-focused; no user study (acknowledged threat to validity). Constraints here are syntactic/format, not safety constraints — the safety implication is inferential.

---

## [streaming-vr] Real-time Verification and Refinement of Language Model Text Generation

- **Citation (APA, best effort from the document):** Ko, J., Baek, J., & Hwang, S. J. (2025). Real-time verification and refinement of language model text generation. *arXiv preprint* arXiv:2501.07824.
- **File:** Literature on LLM safety/Ko et al - 2025 - Real-time verification and refinement of language model text generation.pdf
- **Type:** empirical
- **Core claims:** Verify-then-refine methods that wait for complete generations are inefficient and suffer error propagation: an early incorrect token raises the chance later sentences are wrong (~37.6% of answers contain such cascading errors; derailment rates 26.3%/48.9% on ASQA/QuoteSum). Streaming-VR verifies and refines each sentence on-the-fly with external models, matching full refinement quality at ~39.8%/31.5% token savings and 1.95× lower latency.
- **Evidence/methods:** Sentence-level verifier (fine-tuned Mistral 7B / LLaMA-3.1 8B; 86.7–93.0 test accuracy) + GPT-4o refiner; ASQA and QuoteSum in closed-book, RAG, and ICL settings; verifier/refiner size ablations; self-VR (same model for all roles) comparison.
- **Relevance to our paper:** Shows layered defense-in-depth (generation + parallel verification + targeted refinement) and that small verifiers suffice while refiners must be strong — a nuanced "layered safeguards" example. Tags: [safeguards-behaviors] [assessment]
- **Key points with locations:**
  - Error propagation motivates mid-generation correction (§1, pp. 1–2; Fig. 4, p. 8)
  - Refinement with the same strong model (GPT-4o) can *degrade* good answers via over-correction (§4.3, pp. 5–6)
  - Intrinsic self-correction (Self-VR) underperforms — consistent with Huang et al. 2024 (§4.3, p. 8)
- **Caveats:** Verifier training data is LLM-augmented (risk of mislabeling, acknowledged). Factual-QA domain only; refinement converges to refiner-model quality, so gains depend on an external strong model.

---

## [reflexion] Reflexion: Language Agents with Verbal Reinforcement Learning

- **Citation (APA, best effort from the document):** Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems (NeurIPS) 36*. (arXiv:2303.11366)
- **File:** Literature on LLM safety/Shinn et al - 2023 - Reflexion Language agents with verbal reinforcement learning.pdf
- **Type:** empirical
- **Core claims:** Language agents can learn from trial-and-error without weight updates: agents convert scalar/binary feedback into *verbal* self-reflections stored in episodic memory, improving later attempts. Reflexion beats baselines by +22% (AlfWorld decision-making), +20% (HotPotQA reasoning), +11% (HumanEval), reaching 91% pass@1 on HumanEval vs GPT-4's 80%.
- **Evidence/methods:** Actor–Evaluator–Self-Reflection loop over ReAct/CoT agents; experiments on AlfWorld (134 tasks), HotPotQA (100 questions), HumanEval/MBPP/LeetcodeHardGym (Python & Rust); ablations on feedback type, memory, test generation; failure analysis (false-positive unit tests; WebShop local-minima failure).
- **Relevance to our paper:** A memorable, human-like learning-from-mistakes mechanism — pedagogically valuable analogy for teaching iteration and feedback; also shows agents' limits (self-evaluation dependence, no guarantees). Tags: [pedagogy] [safeguards-behaviors] [didactics]
- **Key points with locations:**
  - Framework: verbal feedback as "semantic gradient"; short- vs long-term memory (§3, pp. 3–5)
  - Ablation: removing self-reflection or test generation drops below/equal baseline (§4.3, Table 3, p. 8)
  - Failure on WebShop: cannot escape local minima needing creative exploration (App. B.1, p. 13)
- **Caveats:** HumanEval result depends on self-generated unit tests (false positives inflate pass@1 — authors acknowledge; MBPP-PY underperforms baseline for this reason). Gains shown to be emergent in strong models only (starchat-beta shows none, App. A).

---

## [self-consistent-errors] Too Consistent to Detect: A Study of Self-Consistent Errors in LLMs

- **Citation (APA, best effort from the document):** Tan, H., Sun, F., Liu, S., Su, D., Cao, Q., Chen, X., Wang, J., Cai, X., Wang, Y., Shen, H., & Cheng, X. (2025). Too consistent to detect: A study of self-consistent errors in LLMs. *arXiv preprint* arXiv:2505.17656.
- **File:** Literature on LLM safety/Tan et al - 2025 - Too consistent to detect A study of self-consistent errors in LLMs.pdf
- **Type:** empirical
- **Core claims:** Defines *self-consistent errors*: LLMs repeatedly generating the same wrong answer across stochastic samples. Unlike inconsistent errors, their frequency stays stable or increases with model scale — so they will persist as models grow. All four detector families (probability, prompt-based P(True), semantic entropy, supervised hidden-state probes) degrade substantially on these errors; consistency-based methods fall to/below random (AUROC ≤ 0.5). Cross-model probes (hidden states of an external verifier LLM) significantly help, since such errors rarely overlap across models (max 28.7%).
- **Evidence/methods:** Qwen2.5 (3–72B), Llama3.x (1–70B), Mistral-12B on SciQ and TriviaQA; k=15 samples with NLI-based semantic equivalence; AUROC gaps ∆ between consistent-error (CE) and inconsistent-error (IE) subsets; verifier selection and λ integration analyses.
- **Relevance to our paper:** Key insight for children: an AI repeating the same answer confidently does *not* mean it is right — consistency ≠ correctness, and errors can stem from widespread misconceptions in training data. Tags: [safeguards-behaviors] [ai-literacy-def] [ethics]
- **Key points with locations:**
  - Self-consistent errors stable/increasing with scale (Fig. 1, p. 2; Fig. 3, p. 8)
  - Example causes: pervasive internet misconceptions ("aluminum lightest structural metal"), confused concepts (new vs full moon) (Table 1, p. 3)
  - Cross-model probe gains across families; different-series and larger verifiers help more (Table 4, p. 5)
- **Caveats:** arXiv preprint (v3, Sep 2025), not peer-reviewed. Short-answer QA only; causes of self-consistent errors remain hypothesized, not established. Error labels assigned by an LLM judge (validated on 300 samples).

---

## [colorado-ai-act] The Colorado AI Act: A Compliance Handshake Between Developers and Deployers

- **Citation (APA, best effort from the document):** Leunig, S., Feldman, E., Schwartz, E., Dammaschk, N., Brown, S., Miller, C., Sullivan, P., & Mittal, A. (2025). *The Colorado AI Act: A compliance handshake between developers and deployers.* The Policy Update.
- **File:** Literature on LLM safety/Leunig et al - 2025 - The Colorado AI Act A compliance handshake between developers and deployers.pdf
- **Type:** policy
- **Core claims:** The Colorado AI Act (SB 24-205, enacted 2024, effective Feb 1, 2026) is the first comprehensive enforceable US state-level framework for *high-risk* AI — systems that make or substantially factor into consequential decisions (employment, housing, education, healthcare, etc.). It imposes a duty of "reasonable care" to avoid algorithmic discrimination on both developers (documentation, disclosure, impact-assessment support, 90-day incident reporting) and deployers (risk-management policy/program, impact assessments, consumer notices, monitoring, annual audits), creating a "compliance handshake."
- **Evidence/methods:** White-paper legal/practice analysis: obligation walk-throughs, exemptions (e.g., <50-employee deployers, federally regulated sectors), ambiguity analysis ("foreseeable risk," "substantial modification," no mandated bias-testing standard), checklists, impact-assessment template, 180-day MLOps roadmap.
- **Relevance to our paper:** Contextualizes classroom AI within real governance: education is explicitly a high-risk domain; demonstrates that society regulates AI because safeguards are imperfect — supports the curriculum's rationale and policy dimension. Tags: [policy] [ethics] [safeguards-behaviors]
- **Key points with locations:**
  - Definition of high-risk AI and algorithmic discrimination; AG enforcement (§2, pp. 4–5)
  - Developer duties: documentation, disclosure, incident reporting within 90 days (§3, pp. 6–9)
  - Ambiguities: undefined "foreseeable" risk and "substantial modification"; flexibility without bias-testing standards risks underenforcement (§6, pp. 18–22)
- **Caveats:** Practitioner white paper (The Policy Update, Aug 2025), not peer-reviewed; authors are compliance professionals (advocacy tone, "governance as business accelerator"). Note: Colorado subsequently delayed the Act's effective date (to June 2026 per public reports) — verify current status before citing dates.

---

## Cross-Batch Synthesis for the Curriculum Paper

1. **Safeguards are imperfect by design and by evidence:** shallow alignment + control-plane bypasses (CDA, 96.2% ASR), persistent self-consistent errors, and low error-detection recall even in GPT-4/Claude 3.
2. **Layered mitigation is the research consensus:** training-time (RLHF/self-training) vs generation-time (constrained decoding, streaming verification) vs post-hoc (CRITIC, Reflexion) — mirroring the curriculum's safeguard-layering content.
3. **External feedback beats self-reflection:** CRITIC w/o tools ≈ no gain; Self-VR degrades; self-evaluation ≈ random. Verification needs grounding (tools, other models, humans).
4. **Consistency ≠ correctness** — a memorable, teachable principle with strong empirical backing (Tan et al. 2025).
5. **Policy exists because technology fails:** Colorado AI Act treats education AI as high-risk, mandating documentation, impact assessments, and monitoring.


---

<!-- ===== batch_8_social_robots__validation_required.md ===== -->

# Batch 8 — Social Robots, Attachment & Anthropomorphism: Structured Summaries

Base folder: `Literature/Literature on Social robots/`. All files read in full with the Read tool (chunked where needed). Prepared for the Marty-robot AI & digital literacy curriculum paper (ages 11–12; attachment and robot perception measured; curriculum teaches AI/robots cannot feel).

---

## [Rabb2022-framework] An Attachment Framework for Human-Robot Interaction
- **Citation (APA, best effort from the document):** Rabb, N., Law, T., Chita-Tegmark, M., & Scheutz, M. (2022). An attachment framework for human-robot interaction. *International Journal of Social Robotics, 14*, 539–559. https://doi.org/10.1007/s12369-021-00802-9
- **File:** Literature on Social robots/Rabb et al - 2022 - An attachment framework for human-robot interaction.pdf
- **Type:** framework
- **Core claims:** "Attachment" in HRI is often used loosely, far from its psychological origin. The paper unifies the attachment literature into a single spectrum with "weak" and "strong" attachment as endpoints, grounded in classic attachment-theory functions (secure base, safe haven, proximity maintenance, separation distress). Different attachment figures (caregivers, pets, deities/symbols, objects, technologies, robots) fulfill different components; current robots generally afford only weak attachment.
- **Evidence/methods:** Conceptual analysis synthesizing psychological attachment theory and existing HRI attachment studies; categorizes where human–robot bonds sit on the spectrum.
- **Relevance to our paper:** Provides the theoretical backbone for interpreting our attachment measure: mild fondness for Marty is "weak attachment," not pathological bonding. [social-robots] [assessment] [ethics]
- **Key points with locations:**
  - Weak vs. strong attachment spectrum defined, Abstract & §1 (pp. 539–540)
  - Attachment in HRI as "far cry from its original psychological conception," §1 (p. 540)
  - Categorization of attachment figures and robots' place, later framework sections
- **Caveats:** Purely conceptual; no new empirical data.

---

## [Huang2013-lego] An Exploration of Robot Builders' Attachment to Their LEGO Robots
- **Citation (APA, best effort from the document):** Huang, L., Varnado, T., & Gillan, D. (2013). An exploration of robot builders' attachment to their LEGO robots. *Proceedings of the Human Factors and Ergonomics Society 57th Annual Meeting*, 1829–1833.
- **File:** Literature on Social robots/An Exploration of Robot Builders' Attachment to Their LEGO Robots.pdf
- **Type:** empirical (small mixed-methods)
- **Core claims:** Students who built LEGO robots over ~2 months showed strong positive emotions but low anxiety/avoidance about losing the robot — i.e., not attachment in the typical psychological sense. Sadness about dismantling stemmed from invested effort; students rationally noted robots could be rebuilt. The learning experience (especially solving challenging problems) was the strongest contributor to affection, not companionship.
- **Evidence/methods:** N = 16 college students in a fall-2012 robotics class; custom questionnaire plus reflective journals.
- **Relevance to our paper:** Closest analogue to our "students build Marty" design; suggests builder affection is effort/learning-driven, supporting a non-anthropomorphizing framing. [hands-on] [social-robots] [assessment]
- **Key points with locations:**
  - Main findings, Abstract (p. 1829)
  - No anxiety–avoidance attachment found; need for a dedicated instrument, Limitations (p. 1833)
  - Enjoyment–accomplishment link in journals, Results/Discussion (p. 1832–1833)
- **Caveats:** Very small sample; adult college students, not children; ad-hoc unvalidated instrument.

---

## [Law2022-attachment-review] Examining Attachment to Robots: Benefits, Challenges, and Alternatives
- **Citation (APA, best effort from the document):** Law, T., Chita-Tegmark, M., Rabb, N., & Scheutz, M. (2022). Examining attachment to robots: Benefits, challenges, and alternatives. *ACM Transactions on Human-Robot Interaction, 11*(4), Article 36. https://doi.org/10.1145/3526105
- **File:** Literature on Social robots/Law et al - 2022 - Examining attachment to robots Benefits, challenges, and alternatives.pdf
- **Type:** review / position
- **Core claims:** Human–robot attachment offers benefits (more natural interaction, robot effectiveness and acceptance, companionship, well-being) but poses risks: suboptimal use, unidirectional emotional bonds, deception, and subconscious influence. The authors recommend reconceptualizing human–robot relationships (e.g., as working alliances, robots as mediators of human contact, or transparent "smart devices") to retain benefits while mitigating harms.
- **Evidence/methods:** Analytical review of HRI literature on attachment; design/ethics guideline derivation.
- **Relevance to our paper:** Ethical warrant for our curriculum's transparency stance ("robots cannot feel"); names the unidirectional-bond risk our teaching aims to prevent. [ethics] [social-robots] [safeguards-behaviors]
- **Key points with locations:**
  - Ethical questions about attachment, §1 (pp. 36:1–36:2)
  - Benefits and challenges analysis, middle sections
  - Reconceptualization recommendations, final sections
- **Caveats:** Conceptual; not child- or classroom-specific empirical work.

---

## [Castaneda2025-wa] Exploring the Working Alliance Formation in AI Companions
- **Citation (APA, best effort from the document):** Castaneda, G. (2025). *Exploring the working alliance formation in AI companions* [Doctoral dissertation, Purdue University]. Department of Technology, Leadership and Innovation.
- **File:** Literature on Social robots/Castaneda - 2025 - Exploring the working alliance formation in AI companions.pdf
- **Type:** empirical (dissertation, mixed/quantitative)
- **Core claims:** Clinically validated AI companions (chatbots) build significantly stronger working alliances — approaching human–human levels — than non-validated ones. Demographics (sex, sexual orientation, race/ethnicity, anxiety/depression severity) did not significantly moderate alliance strength. Users valued ease of interaction, a judgment-free environment, and guidance. Proposes extending the WAI-SR with an "AI Alignment" subcomponent for ethical, safe AI companions.
- **Evidence/methods:** Survey-based comparison of working alliance (WAI-SR) across validated vs. non-validated AI companion users; 142-page dissertation.
- **Relevance to our paper:** Peripheral (adults, text chatbots, mental health) but informs how human–AI bonds are measured and how "alliance" differs from attachment — useful construct contrast for our robot-perception measures. [social-robots] [assessment] [ethics]
- **Key points with locations:**
  - Validated vs. non-validated alliance difference, Results chapters
  - Thematic findings (judgment-free interaction), qualitative results
  - WAI-SR "AI Alignment" proposal, Discussion/Recommendations
- **Caveats:** Not peer-reviewed journal article; adult mental-health context, not child education.

---

## [PRAISE2026-safety] Children's ambivalence toward safety of AI-driven social robots is not influenced by age or knowledge
- **Citation (APA, best effort from the document):** Anonymous Author(s). (under review, HRI 2026 submission). Children's ambivalence toward safety of AI-driven social robots is not influenced by age or knowledge. [Manuscript under review; ACM template placeholders visible].
- **File:** Literature on Social robots/Anonymous - 2026 - Children's ambivalence toward safety of AI-driven social robots HRI 2026 submission.pdf
- **Type:** empirical (mixed-methods)
- **Core claims:** Among 10–16-year-olds, AI knowledge increases with age, but ambivalence toward the safety of AI-driven social robots remains stable — neither age nor knowledge shifts it. Children hold nuanced beliefs alongside misconceptions (e.g., that an emotional bond with a robot ensures data privacy). The paper derives guidelines for AI-literacy curricula and transparent, controlled educational robot design.
- **Evidence/methods:** Survey (n = 71) plus focus groups (n = 36); quantitative attitude measures and thematic analysis.
- **Relevance to our paper:** Directly adjacent age band and topic (AI literacy + social robots + safety); supplies baseline evidence that knowledge alone does not fix safety misconceptions — a core justification for our curriculum. [ai-literacy-def] [safeguards-behaviors] [age-appropriateness] [social-robots] [ethics]
- **Key points with locations:**
  - Research questions and design, Abstract & §1 (p. 1)
  - Ambivalence stable despite rising knowledge, quantitative results
  - Misconceptions and curriculum/design guidelines, thematic analysis & discussion
- **Caveats:** Anonymous manuscript under review; not yet peer-reviewed.

---

## [Liu2024-reading] A social robot as your reading companion: exploring the relationships between gaze patterns and knowledge gains
- **Citation (APA, best effort from the document):** Liu, X., Ma, J., & Wang, Q. (2024). A social robot as your reading companion: Exploring the relationships between gaze patterns and knowledge gains. *Journal on Multimodal User Interfaces, 18*, 21–41. https://doi.org/10.1007/s12193-023-00418-5
- **File:** Literature on Social robots/Papers on social robots/Liu et al - 2024 - A social robot as your reading companion Exploring the relationships between.txt (PDF title verified against txt)
- **Type:** empirical
- **Core claims:** An embodied social robot giving feedback during e-reading significantly changes readers' gaze patterns, and different knowledge-gain levels differ in scanning method and reading depth (high gain linked to extensive, F-shaped scanning of key parts rather than uniform intensive reading). Gaze features — especially saccades — predict knowledge-gain level.
- **Evidence/methods:** Eye-tracking experiment with college students reading with a social robot companion; machine-learning classifiers (soft voting) reached 74.2% accuracy; real-time leave-one-out simulation with 60 participants reached 71.5%.
- **Relevance to our paper:** Indirect: shows how robot feedback measurably alters learning behavior and how gaze analytics can assess learning — methodological inspiration for assessment dimension. [social-robots] [assessment] [pedagogy]
- **Key points with locations:**
  - Robot feedback affects gaze patterns throughout reading, Abstract (p. 21)
  - Saccades as best predictors (74.2% accuracy), Abstract/prediction experiments (p. 21)
  - Real-time simulation (71.5%), Abstract (p. 21)
- **Caveats:** Adult university students, not children; reading task far from programming/robotics curriculum.

---

## [Tarakli2025-lbt] Robots and Children that Learn Together: Improving Knowledge Retention by Teaching Peer-Like Interactive Robots
- **Citation (APA, best effort from the document):** Tarakli, I., Vinanzi, S., Moore, R., & Di Nuovo, A. (2025). Robots and children that learn together: Improving knowledge retention by teaching peer-like interactive robots. *arXiv*. https://arxiv.org/abs/2506.18365
- **File:** Literature on Social robots/Papers on social robots/Tarakli et al - 2025 - Robots and children that learn together Improving knowledge retention by.txt (PDF title verified against txt)
- **Type:** empirical
- **Core claims:** Learning-by-Teaching with an autonomous, peer-like social robot (powered by Interactive Reinforcement Learning) yields significantly higher knowledge-retention gains than tablet self-practice, especially for grammar inference. Children with lower prior knowledge benefited most; children adapted teaching strategies over time, evidencing metacognitive engagement. Demonstrates feasibility of multiple autonomous robots in real classrooms simultaneously.
- **Evidence/methods:** Two between-subject experiments, 58 primary-school children, French vocabulary and grammar tasks; robot learned from children's evaluative feedback.
- **Relevance to our paper:** Strong evidence that child–robot teaching interactions in real classrooms boost retention — supports the pedagogy of our Marty-based activities. [pedagogy] [social-robots] [age-appropriateness] [hands-on]
- **Key points with locations:**
  - Interactive RL as cognitive model for teachable robots, Abstract (p. 1)
  - Higher retention in LbT condition, largest for low-prior-knowledge learners, Abstract (p. 1)
  - First multi-robot autonomous classroom deployment, Abstract/contributions (p. 1)
- **Caveats:** arXiv preprint (June 2025), not yet peer-reviewed.

---

## [Kozima2023-pretend] Communication as Joint Prediction: A Case Study of Robot-Mediated Pretend Play with Children at a Kindergarten
- **Citation (APA, best effort from the document):** Kozima, H. (2023). Communication as joint prediction: A case study of robot-mediated pretend play with children at a kindergarten. *2023 32nd IEEE International Conference on Robot and Human Interactive Communication (RO-MAN)*. https://doi.org/10.1109/RO-MAN57019.2023.10309527
- **File:** Literature on Social robots/Papers on social robots/Kozima - 2023 - Communication as joint prediction A case study of robot-mediated pretend play.txt (PDF title verified against txt)
- **Type:** empirical (case study) + theoretical modeling
- **Core claims:** In longitudinal interaction with a remotely controlled, simply designed robot (Keepon-like), 3–4-year-olds used the robot as a "pivot" to exchange and coordinate expectations; incongruent expectations gradually converged into shared fantasy. Interpreted via predictive coding: children project predictions (labeling a block as a rice ball, feeding it to the robot) and update them through visible collective action — joint prediction as the fundamental process of social communication.
- **Evidence/methods:** Longitudinal observations of 27 preschoolers in a kindergarten; qualitative case analysis with predictive-coding modeling.
- **Relevance to our paper:** Shows how even minimal robot embodiments invite rich social projection by young children — background for why children anthropomorphize classroom robots. [social-robots] [age-appropriateness] [pedagogy]
- **Key points with locations:**
  - Robot as pivot for expectation-sharing, Abstract (p. 1)
  - Predictive-coding interpretation of pretend actions, Abstract (p. 1)
  - Case observations with 27 preschoolers, §II+ case studies
- **Caveats:** Much younger children (3–4) than our 11–12 target; qualitative, single context, teleoperated robot.

---

## [Epley2018-mind] A Mind like Mine: The Exceptionally Ordinary Underpinnings of Anthropomorphism
- **Citation (APA, best effort from the document):** Epley, N. (2018). A mind like mine: The exceptionally ordinary underpinnings of anthropomorphism. *Journal of the Association for Consumer Research, 3*(4). https://doi.org/10.1086/699516
- **File:** Literature on Social robots/Papers on social robots/Epley - 2018 - A mind like mine The exceptionally ordinary underpinnings of anthropomorphism.txt (PDF title verified against txt)
- **Type:** position / theoretical review (special-issue introduction)
- **Core claims:** Anthropomorphism is not an extraordinary glitch but the ordinary output of social cognition: it is driven by two motivations (social connection; effectance — the need to explain/predict agents) plus bottom-up "elicited agent knowledge" (face, voice, movement). Anthropomorphism and dehumanization are inverse outcomes of the same mind-perception process. Poses four research questions: what counts as anthropomorphism, its causes, its consequences, and its inverse.
- **Evidence/methods:** Theoretical synthesis drawing on Epley, Waytz & Cacioppo's three-factor theory and consumer-behavior experiments (e.g., anthropomorphized autonomous vehicle increases trust).
- **Relevance to our paper:** Foundational theory explaining *why* children attribute feelings to Marty and what cues (voice!) trigger it — supports curriculum design that addresses mechanism, not just the belief. [social-robots] [ai-literacy-def] [didactics]
- **Key points with locations:**
  - Three-factor theory recap (connection, effectance, elicited agent knowledge), "Mechanisms of Mind Perception" section
  - Voice as a humanizing cue, same section
  - Four research questions, "Question 1–4" sections
- **Caveats:** Consumer-behavior context; not about children or education specifically.

---

## [Cheng2024-anthroscore] ANTHROSCORE: A Computational Linguistic Measure of Anthropomorphism
- **Citation (APA, best effort from the document):** Cheng, M., Gligorić, K., Piccardi, T., & Jurafsky, D. (2024). ANTHROSCORE: A computational linguistic measure of anthropomorphism. *arXiv*. https://arxiv.org/abs/2402.02056
- **File:** Literature on Social robots/Papers on social robots/Cheng et al - 2024 - ANTHROSCORE A computational linguistic measure of anthropomorphism.txt (PDF title verified against txt)
- **Type:** empirical (computational linguistics / methods)
- **Core claims:** ANTHROSCORE uses a masked language model to quantify how strongly a sentence's context frames a non-human entity as human (log-ratio of human vs. non-human pronoun probabilities at the masked entity). Validated against human judgments (κ = 0.87) and LIWC dimensions. Findings: anthropomorphism in CS/Stats papers has risen over 15 years; LM-related papers are most anthropomorphized; news headlines anthropomorphize more than the abstracts they cite.
- **Evidence/methods:** ~600K arXiv abstracts, ~55K ACL Anthology papers, ~14K news headlines; RoBERTa-based metric; robustness checks (pronoun removal, verb removal, reporting verbs).
- **Relevance to our paper:** Methodological tool and cautionary tale: anthropomorphic *language* shapes perception — relevant to how our curriculum and we ourselves write about Marty/AI; media-amplification finding supports critical AI literacy. [ai-literacy-def] [assessment] [ethics] [social-robots]
- **Key points with locations:**
  - Metric definition and validation, §3 (Methods)
  - Temporal increase; LM papers highest, §4.1–4.2 (Results)
  - News > abstracts anthropomorphism, §4.3
- **Caveats:** English-only pronoun method; arXiv preprint; about text, not child–robot interaction.

---

## [Goldman2024-animacy] Children's anthropomorphism of inanimate agents
- **Citation (APA, best effort from the document):** Goldman, E. J., & Poulin-Dubois, D. (n.d.). Children's anthropomorphism of inanimate agents. Concordia University. [Preprint marked "under review — do not cite without permission"; published version: *WIREs Cognitive Science* (2024).]
- **File:** Literature on Social robots/Papers on social robots/Goldman & Poulin-Dubois - 2024 - Children's anthropomorphism of inanimate agents.txt (PDF title verified against txt)
- **Type:** review
- **Core claims:** Infants and young children have a broad concept of sentient agency: objects displaying animate motion (self-propulsion, contingency, goal-directedness) trigger the same behaviors as people. Animism decreases with age — but social robots are an exception: children attribute fewer psychological properties to robots than to humans, yet still anthropomorphize them, depending on morphology, human-like behavior, and exposure. Children gradually learn artifacts are not alive but can serve as depictions of social agents and learning partners.
- **Evidence/methods:** Narrative review of developmental studies: gaze following, goal attribution, false-belief tasks, naïve biology ("insides") tasks, selective trust and word learning with robots.
- **Relevance to our paper:** Maps the developmental landscape our 11–12-year-olds sit at the top of; explains why robot morphology/behavior drive anthropomorphism — key for interpreting our robot-perception measures. [age-appropriateness] [social-robots] [ai-literacy-def] [assessment]
- **Key points with locations:**
  - Developmental decrease of animism; robots as exception, Abstract (p. 1)
  - 5-year-olds classify robots as mechanical but humanoid morphology creates uncertainty, sections on naïve biology (pp. 10–11, 22)
  - Children learn from robots; competence vs. morphology, Learning section (pp. 23–26)
- **Caveats:** Preprint explicitly asks not to be cited without permission; cite the published version instead.

---

## [vandenBerghe2021-toyfriend] A toy or a friend? Children's anthropomorphic beliefs about robots and how these relate to second-language word learning
- **Citation (APA, best effort from the document):** van den Berghe, R., de Haas, M., Oudgenoeg-Paz, O., Krahmer, E., Verhagen, J., Vogt, P., Willemsen, B., de Wit, J., & Leseman, P. (2021). A toy or a friend? Children's anthropomorphic beliefs about robots and how these relate to second-language word learning. *Journal of Computer Assisted Learning, 37*, 396–410. https://doi.org/10.1111/jcal.12497
- **File:** Literature on Social robots/Papers on social robots/Berghe et al - 2021 - A toy or a friend Children's anthropomorphic beliefs about robots and how these.txt (PDF title verified against txt)
- **Type:** empirical
- **Core claims:** Five-year-olds (N = 104) anthropomorphized a NAO tutor moderately and stably overall, but item-level beliefs shifted after seven L2 tutoring sessions: fewer biological/negative-emotion attributions, more cognitive ones (understands, remembers, recognizes me) — a shift toward "mechanical being with positive mental states." Boys and younger children decreased more. Pre-test anthropomorphism weakly *negatively* correlated with immediate word knowledge, while *increase* in anthropomorphism weakly correlated with delayed word knowledge.
- **Evidence/methods:** Part of the pre-registered L2TOR RCT; 12-item yes/no anthropomorphism questionnaire (α ≈ .72–.75) before/after seven robot-tutoring sessions; comprehension post-tests.
- **Relevance to our paper:** Rare multi-session longitudinal picture of how children's robot beliefs evolve with exposure; expectation-management recommendation matches our curriculum's transparency goal. [social-robots] [age-appropriateness] [assessment] [pedagogy]
- **Key points with locations:**
  - Item-level belief shifts, Table 2 & §3.2 (pp. 403–404)
  - Gender/age interactions with change, §3.2 (p. 404)
  - Expectation-management implications, §4.3–4.4 (pp. 405–407)
- **Caveats:** Correlational anthropomorphism–learning links are weak; younger (5yo) sample; custom (not standardized) questionnaire.

---

## [Baumann2023-trust] People Do Not Always Know Best: Preschoolers' Trust in Social Robots
- **Citation (APA, best effort from the document):** Baumann, A.-E., Goldman, E. J., Meltzer, A., & Poulin-Dubois, D. (2023). People do not always know best: Preschoolers' trust in social robots. *Journal of Cognition and Development*. https://doi.org/10.1080/15248372.2023.2178435
- **File:** Literature on Social robots/Papers on social robots/Baumann et al - 2023 - People do not always know best Preschoolers' trust in social robots.txt (PDF title verified against txt)
- **Type:** empirical (two pre-registered studies)
- **Core claims:** First direct human-vs-robot comparison in the classic selective-trust paradigm: 5-year-olds preferentially learn novel labels from a *competent robot* over an *incompetent human* — even while correctly judging the robot to have mechanical insides (naïve biology task). Three-year-olds endorse both equally, weighing social and epistemic cues together. Robot morphology (humanoid Nao vs. non-humanoid Cozmo) does not change the pattern; agency cues (speech, goal-directedness) suffice.
- **Evidence/methods:** Study 1: N = 95 (50 three-year-olds, 45 five-year-olds), Nao vs. human; Study 2: N = 89, Cozmo vs. human; Zoom administration; parental ToM (CSUS) and prosociality (CPBQ) measures (only weak ToM links found).
- **Relevance to our paper:** Epistemic trust in robots decouples from animacy beliefs by age 5 — children can treat a robot as a machine *and* a credible informant, supporting our "machine but useful" framing. [social-robots] [age-appropriateness] [pedagogy] [ai-literacy-def]
- **Key points with locations:**
  - 5-year-olds endorse competent robot despite mechanical categorization, Study 1 Results & Discussion (pp. 12–15)
  - Morphology irrelevant; Cozmo replication, Study 2 (pp. 15–20)
  - Implications for educational robots, General Discussion (pp. 20–24)
- **Caveats:** Online/video-based interaction; preschoolers, not pre-teens; weak/null links with ToM and prosociality measures.

---

## [vanStraten2023-transparent] Transparent robots: How children perceive and relate to a social robot that acknowledges its lack of human psychological capacities and machine status
- **Citation (APA, best effort from the document):** van Straten, C. L., Peter, J., & Kühne, R. (2023). Transparent robots: How children perceive and relate to a social robot that acknowledges its lack of human psychological capacities and machine status. *International Journal of Human-Computer Studies, 177*, 103063. https://doi.org/10.1016/j.ijhcs.2023.103063
- **File:** Literature on Social robots/Papers on social robots/van Straten et al - 2023 - Transparent robots How children perceive and relate to a social robot that.txt (PDF title verified against txt)
- **Type:** empirical (pre-registered between-subject experiment)
- **Core claims:** A Nao robot that itself explains its machine status and lack of psychological capacities (no feelings, no own thoughts, pre-programmed) reduces 8–10-year-olds' anthropomorphism (large effect, η² = .43), perceived similarity, closeness, and trust (small effects, η² ≈ .02). Anthropomorphism mediates the transparency effect on closeness and trust; perceived similarity mediates only closeness. Transparency can work "through the robot," without an adult.
- **Evidence/methods:** N = 276 children aged 8–10 (M = 9.5) at NEMO Science Museum; one 6–7 min guessing-game interaction (WoZ); validated self-report scales; PROCESS mediation.
- **Relevance to our paper:** Strongest empirical support for our curriculum's core move: telling children the robot can't feel measurably dampens anthropomorphism while effects on relationship are small — transparency need not destroy engagement. [safeguards-behaviors] [social-robots] [age-appropriateness] [ethics] [didactics]
- **Key points with locations:**
  - Manipulation texts (e.g., "I'm never happy, angry, or sad... I consist of plastic and wires"), Appendix A (p. 9)
  - ANOVA effects, Table 1 & §4.2 (p. 7)
  - Small effects on closeness/trust ≠ prevention of relationship formation, §5 (p. 8)
- **Caveats:** Single short interaction; some analyses underpowered (acknowledged); self-report only.

---

## [ReadingNotes] Reading notes.md — verification & assessment (secondary source)
- **File:** Literature on Social robots/Reading notes.md (124 lines + 3 embedded base64 screenshots; read in full — text spans lines 1–120; lines 121–125 are embedded PNG images, not text)
- **What it covers:** Personal reading notes on three works: (1) Henschel, Laban, & Cross (2021), *What Makes a Robot Social?* (Current Robotics Reports, 2(1), 9–19, doi:10.1007/s43154-020-00035-0) — most extensive: "social robot paradox," Sarrica et al.'s (2019) 8 user-perceived social characteristics, Baraka et al.'s 7 dimensions of social robots, social-cognition constructs (trust, attachment, empathy, acceptance, disclosure), and health/well-being applications (Paro pain/oxytocin study; Nao motivational-interviewing interventions; Robinson et al. 2020 behavior-change RCT); (2) Addlesee et al. (2024), *A Multi-party Conversational Social Robot Using LLMs* (HRI 2024 Companion, doi:10.1145/3610978.3641112) — citation plus evaluation-measures list (response time, turn exchanges, interruption rate, persona consistency, hallucinations...); (3) Pinto-Bernal, Biondina, & Belpaeme (2025), *Designing Social Robots with LLMs for Engaging Human Interaction* (Applied Sciences, 15(11):6377, doi:10.3390/app15116377) — quotes on ElevenLabs voice quality, singing failure anecdote, silence threshold (~1.8 s), ARI robot architecture figure.
- **Sources cited:** ~25 references with DOIs (e.g., Sarrica 2019; Wiese 2017; Wykowska 2016; Langer 2019; Naneva 2020; Dziergwa 2018; Cross 2019; Birnbaum 2016 ×2; Björling 2019; Hoffman 2014; Traeger 2020; Laban 2021; Dawe 2019; Geva 2020; Robinson 2020) — all plausible and consistent with the primary papers' reference lists.
- **Reliability as a secondary source:** Moderate. Verbatim quotes are sometimes quotation-marked, but paraphrase and quote are not systematically distinguished; bracket numbers refer to the primary papers' reference lists. Good for signposting (esp. the Henschel et al. review and the LLM-robot evaluation measures), but every claim must be re-verified against the primary source before citation. [social-robots] [assessment]

---

## [ElicitCSV] 06_Social_Robots_in_School_Settings_2023plus.csv — data table description (no full summary)
- **Files:** Literature on Social robots/06_Social_Robots_in_School_Settings_2023plus.csv and Literature on Social robots/Papers on social robots/06_Social_Robots_in_School_Settings_2023plus.csv
- **Identity check:** The two copies are byte-identical (verified with `diff`).
- **Content:** Elicit-style literature-export table; 16 lines = header + 15 paper rows. Columns: Title, Authors, DOI, DOI link, Venue, Citation count, Year, Abstract summary. Rows are 2024–2025 papers on LLM-powered social robots, educational agents, and AI literacy (e.g., Kajiwara & Kawabata 2024 chatbot-ethics curriculum; Elgarf et al. 2024 LLM storytelling robot & creativity; Williams et al. 2024 Doodlebot; Kim, Lee & Mutlu 2024 LLM-powered HRI; Latif et al. 2024 PhysicsAssistant; Grover 2024 Teaching AI to K-12; Almatrafi et al. 2024 AI-literacy review; Addlesee et al. 2024; Pinto-Bernal et al. 2025).
- **Purpose:** Scoping table for recent (2023+) work at the intersection of social robots in school settings and AI literacy. The "Abstract summary" column already contains one-line relevance judgments; several rows are explicitly flagged as *not* relevant to the query (e.g., Knoth et al. 2024 prompt engineering; SOTOPIA-π) — i.e., the export documents both hits and screened-out items. [social-robots] [ai-literacy-def]


---

<!-- ===== batch_9_existing_reviews__validation_required.md ===== -->

# Batch 9 — Verification of Existing In-Repo Literature Review Notes

> Audit of pre-existing review/notes files in the repo, assessing their trustworthiness as secondary sources for the Marty-robot AI & digital literacy curriculum paper (ages 11–12; Context, Content, Pedagogy, Didactics, Assessment; AICOS/MAILS instrument). Verified 2026-09-15. All five files were read in full.

---

## [R9-1] Review_of_Literature_on_AI_Literacy.md
(`Literature on AI literacy/Review_of_Literature_on_AI_Literacy.md`)

- **What it covers:** A broad synthesis claiming to cover ~30 papers on AI literacy: foundational frameworks, child development & AI, generative AI in education, social robots/HRI, anthropomorphism and trust, ethics & safety. Organizes content into core competencies (foundational knowledge, critical thinking, "human advantage"), the aiEDU AI Readiness Framework v2.0, age-appropriate progression (K-5, 6-8, 9-12), social robots in education (drawing on the Elicit CSV, R9-5), ethical considerations, implementation strategies, and research gaps.
- **Sources cited:** Ng et al. (2021) "Conceptualizing AI literacy: An exploratory review"; Kajiwara & Kawabata (2024) "AI literacy for ethical use of chatbot"; aiEDU AI Readiness Framework v2.0; "The Blueprint for Action: Comprehensive AI Literacy for All"; UNICEF AI Children Policy Guidance; "Elicit - Social robots in school settings (2023+)" — plus ~24 other entries listed **by title only, without authors, years, venues, or DOIs** (e.g., "A Toy or a Friend: Children's Anthropomorphic Beliefs About Robots", "ANTHROSCORE", "Constitutional AI"). The final References section is only 5 generic bullet points.
- **Reliability/usability as secondary source:** LOW. Most claims are not attributed to specific sources inline; the bulk of the "30 papers" list consists of bare titles that cannot be traced without extra work. The References section does not match the 30-item list (no authors/years/DOIs). Red flags: unverifiable aggregate claims ("30 Papers" count not substantiated), frameworks summarized without pinpoint citations, and the "Social Robots (2023+)" section paraphrases the Elicit CSV abstract-summaries rather than the papers themselves. Usable only as a discovery map, not as a citable source.
- **Which claims we could reuse (with verification) in our paper:**
  - Existence and structure of the aiEDU AI Readiness Framework v2.0 (three domains: Know Your Basics / Be a Critical Thinker / Lead with Human Advantage) — verify against the aiEDU original.
  - Ng et al. (2021) four-aspect AI literacy framework as a definitional anchor — we likely already have this; verify.
  - Kajiwara & Kawabata (2024) on students' acceptance of AI ethics teaching (traceable via Elicit CSV, DOI 10.1016/j.caeai.2024.100251).
  - General gap claims (assessment tools lacking, cultural Western bias, K-3 materials gap) — only as leads; each needs a real citation before use.
- **Relevance to our paper:** [ai-literacy-def] [content-frameworks] [age-appropriateness] [social-robots] [ethics] [assessment]

---

## [R9-2] AI_Literacy_Learning_Support_Analysis.md
(`Literature on AI literacy/AI_Literacy_Learning_Support_Analysis.md`)

- **What it covers:** An internal gap analysis (dated January 2025) testing the claim "what seems to lack in most AI literacies is how AI can support learning and human development." Reviews in-repo extracted texts of aiEDU, MIT AI Ethics, and Georgia AI4GA curricula for "learning support" content, identifies gaps (personal learning enhancement, human development, adaptive learning, self-regulated learning), and lists recent (2024–2025) initiatives addressing them.
- **Sources cited:** aiEDU AI Readiness Framework v2.0 (local extracted text); aiEDU SmartTeach AP CSP manual (local); MIT AI Ethics Education Curriculum (local); Georgia AI4GA units (local); "Synergizing Self-Regulation and AI Literacy" (2025, arXiv:2504.07125); MIT RAISE Inclusive AI Literacy & Learning (raise.mit.edu); "AI Literacy for All" curriculum (arXiv:2409.10552); San Jose State AI Literacy Essentials module; Day of AI (MIT RAISE); Evergreen Education AI Literacy Curriculum. Includes direct quotes from local curriculum files and working URLs.
- **Reliability/usability as secondary source:** MODERATE. Claims about curriculum content are attributed to specific local files with quotes (verifiable inside the repo). External sources given with links (arXiv IDs, institutional pages) but no full bibliographic details (authors/venues missing). The gap conclusion is an interpretation, not a systematic review — fine as motivation for our paper's novelty argument, but the underlying extracted-text files and arXiv papers should be checked before citing.
- **Which claims we could reuse (with verification) in our paper:**
  - Gap argument: existing AI literacy curricula under-address how AI supports students' own learning and self-regulated learning (verify via arXiv:2504.07125).
  - aiEDU SmartTeach positions AI as "supplement, not replacement" for learning (verifiable in local extracted text).
  - MIT RAISE / Day of AI / SJSU as examples of newer learning-support-oriented initiatives (links provided).
- **Relevance to our paper:** [content-frameworks] [pedagogy] [curriculum-difficulty] [ai-literacy-def]

---

## [R9-3] Teenage_AI_Knowledge_Requirements_Analysis.md
(`Literature on AI literacy/Papers on AI literacy/Teenage_AI_Knowledge_Requirements_Analysis.md`)

- **What it covers:** Extracts knowledge requirements for teenagers (14–18) from the OECD/EU AI Literacy Framework Review Draft (2025), organized into five domains (Nature of AI; AI reflects human choices; AI reshapes work; capabilities & limitations; AI in society) with coded knowledge statements (K1.1–K5.4), then compares the OECD/EU framework against Long & Magerko (2020), Ng et al. (2021), and the EDSAFE Blueprint for Action (2025), and gives implementation recommendations.
- **Sources cited:** OECD (2025) "Empowering learners for the age of AI: An AI literacy framework for primary and secondary education (Review draft)"; Long, D., & Magerko, B. (2020, CHI); Ng, D. T. K., Leung, J. K. L., Chu, S. K. W., & Qiao, M. S. (2021, Computers and Education: AI, 2, 100041); Blueprint for Action: Comprehensive AI Literacy for All (2025, EDSAFE AI Alliance). Reference list has authors/years/titles (mostly complete, but no DOIs/pages).
- **Reliability/usability as secondary source:** MODERATE-HIGH for orientation. Sources are named with near-complete citations; K-statements are presented as quotes/paraphrases from the OECD draft and are internally consistent with that framework's known structure. However, the knowledge statements were not checked here against the OECD PDF page-by-page, and the comparison sections are the note author's analysis. Target group (14–18) is older than our 11–12 cohort — usable for downward-scaffolding arguments only.
- **Which claims we could reuse (with verification) in our paper:**
  - The five knowledge domains / K1.1–K5.4 statements as a content-framework reference (verify against OECD 2025 draft PDF).
  - Comparative positioning of OECD/EU framework vs. Long & Magerko (2020) and Ng et al. (2021) — verify claims of "unique contributions" (environmental impact, IP issues) before asserting them.
  - Implementation principles (interdisciplinary integration, ethics woven throughout, hands-on learning, age-appropriate progression) — generic enough to reuse with OECD citation.
- **Relevance to our paper:** [content-frameworks] [age-appropriateness] [ai-literacy-def] [ethics] [policy]

---

## [R9-4] ai_literacy_assessments__validation_required.md
(`ai_literacy_assessments__validation_required.md`)

- **What it covers:** A well-structured review of AI literacy measurement: definitions/dimensions, major frameworks (OECD PISA 2029 MAIL; UNESCO AI Competency Framework for Students 2024; Long & Magerko 2020 competency map), validated instruments (AI-CI, AILQ, MAILS + short form, a Rasch-validated multidimensional scale, GLAT), the self-report vs. performance gap, COSMIN-based quality gaps, method comparison table, age-appropriateness table, and explicit implications for the BuildBots/CurriculumPaper context (MAILS at T1/T4/T7 + objective items).
- **Sources cited:** Yang et al. (2025, J. STEM Education Research, doi:10.1007/s41979-025-00166-z); OECD (2026) PISA 2029 MAIL draft framework; UNESCO (2024, doi:10.54675/JKJB9835); Long & Magerko (2020, doi:10.1145/3313831.3376727); Zhang, Perry & Lee (2025, AI-CI, IJAIED, ERIC EJ1461172); Ng et al. (2024, AILQ, BJET 55(3), doi:10.1111/bjet.13411); Carolus et al. (2023, MAILS, CHB: Artificial Humans 1(1), 100014); Koch et al. (2024, MAILS short form — flagged "details require verification"); Rasch scale (2025, HSSC, doi:10.1038/s41599-025-05670-6 — authors flagged "require verification"); Stanford SCALE GLAT (2024, arXiv:2411.00283); Lintner (2024, npj Science of Learning, doi:10.1038/s41539-024-00264-4); Clerc et al. (2026, AIED); Abdelghani et al. (2025, arXiv:2505.01106); Stanford SCALE (2026 misalignment report); Zhang, Prasad & Schroeder (2025, doi:10.1177/07356331251342081); Bewersdorff et al. (preprint); Palczyńska & Rynko (2021, as cited in Clerc et al.).
- **Reliability/usability as secondary source:** HIGH (best of this batch). Claims are attributed inline to specific sources; most references have DOIs/links; the file itself transparently flags items needing verification (Rasch scale authors, Koch et al. short MAILS details, Ng et al. 2023 author list). Still a secondary source: numbers (item counts, sample sizes, α values, the "3 of 16 performance-based" figure, negative-correlation finding) must be confirmed in the originals before publication, especially for AICOS/MAILS-adjacent claims.
- **Which claims we could reuse (with verification) in our paper:**
  - Self-report vs. performance gap: only 3/16 validated scales are performance-based (Lintner 2024); self-reports systematically overestimate (Bewersdorff preprint; Stanford SCALE 2026); middle-schoolers' self-reported expertise correlated negatively with performance (Abdelghani et al. 2025) — strong justification for our AICOS/MAILS mixed design.
  - MAILS (Carolus et al. 2023) instrument description and its limitation of not being validated for pre-teens; short form (Koch et al. 2024 — verify details).
  - AI-CI (Zhang, Perry & Lee 2025) as the only performance-based instrument validated for grades 5–8; AILQ (Ng et al. 2024) ABCE structure.
  - COSMIN quality gaps (no cross-cultural validity or measurement error testing on any scale) and the gap "no performance-based instrument for ages 6–11".
  - PISA 2029 MAIL (OECD 2026) five competence areas as external framing for our assessment dimension.
- **Relevance to our paper:** [assessment] [content-frameworks] [age-appropriateness] [ai-literacy-def] [policy]

---

## [R9-5] Elicit - Explore what we know about the use of social robots in school settings. Look specifically at papers with data after 2023, publishe.csv
(`Literature on AI literacy/Elicit - Explore what we know about the use of social robots in school settings. Look specifically at papers with data after 2023, publishe.csv`)

- **What it covers (data table):** An Elicit literature-search export on social robots in school settings, restricted to papers with data after 2023. **Columns (8):** Title, Authors, DOI, DOI link, Venue, Citation count, Year, Abstract summary. **Rows: 16 papers** (all 2024–2025). Purpose: raw input table for the "Social Robots (2023+)" section of R9-1; the Abstract summary column contains Elicit-generated one-line relevance/relevance-failure notes (several rows explicitly say "not relevant to the query").
- **Sources cited (papers listed):** Kajiwara & Kawabata (2024, CAEAI); Elgarf, Salam & Peters (2024, Frontiers in Robotics and AI); Córdova-Esparza (2025, Information); Williams et al. (2024, Doodlebot, HRI); Kim, Lee & Mutlu (2024, HRI); Latif, Parasuraman & Zhai (2024, RO-MAN, PhysicsAssistant); Ferrato et al. (2025, UMAP); Atuhurra (2024); Mishra, Welch & Popa (2024, autism LLM robot); Almatrafi, Johri & Lee (2024, CAEO systematic review); Knoth et al. (2024, CAEAI); Grover (2024, SIGCSE TS); Maiti & Goel (2024, arXiv); Pinto-Bernal, Biondina & Belpaeme (2025); Addlesee et al. (2024, HRI); Wang et al. (2024, SOTOPIA-π, ACL).
- **Reliability/usability as secondary source:** MODERATE as a search artifact, LOW as evidence. Bibliographic metadata (title/authors/DOI/venue/year) is mostly complete, but some rows lack DOI/venue (Atuhurra 2024; Mishra et al. 2024), and citation counts are a snapshot. The "Abstract summary" column is Elicit-AI-generated, sometimes stating conclusions (e.g., "hybrid workflows outperform autonomous tutors") without provenance, and ~5 rows are flagged as not relevant — the file needs filtering before use. Treat as a reading list, never as a citable claim source.
- **Which claims we could reuse (with verification) in our paper:**
  - Nothing directly — but the relevant rows are a vetted shortlist of post-2023 social-robot papers to read ourselves: Doodlebot (Williams et al. 2024), Elgarf et al. 2024 (LLM storytelling robot & creativity), Kim et al. 2024 (LLM-HRI design requirements), Latif et al. 2024 (PhysicsAssistant), Córdova-Esparza 2025 (human-in-the-loop educational agents), Kajiwara & Kawabata 2024 (AI ethics acceptance, 12–18 yo).
- **Relevance to our paper:** [social-robots] [hands-on] [pedagogy] [ethics] [age-appropriateness]

---

## Cross-file notes for the paper team
1. Only R9-4 meets near-citable secondary-source quality (inline attribution + DOIs + self-flagged verification items). R9-2 and R9-3 are usable with checks. R9-1 is a discovery map only; R9-5 is a raw search export.
2. Papers we should still read ourselves before citing (priority): Lintner (2024); Carolus et al. (2023, MAILS); Koch et al. (2024, MAILS short — full reference unresolved); Abdelghani et al. (2025); Clerc et al. (2026); Zhang, Perry & Lee (2025, AI-CI); Ng et al. (2024, AILQ); OECD (2025) AI literacy framework draft + OECD (2026) PISA 2029 MAIL draft; and the relevant R9-5 social-robot papers (Williams et al. 2024; Kim et al. 2024; Elgarf et al. 2024; Latif et al. 2024).
3. R9-1's "30 papers" list contains title-only entries (anthropomorphism/trust cluster) that are unverifiable as written — do not cite any claim traceable only to R9-1.


---

<!-- ===== batch_10_related_papers__validation_required.md ===== -->

# Batch 10 — Related Papers Summaries

## [23] A New Finnish National Core Curriculum for Basic Education (2014) and Technology as an Integrated Tool for Learning

- **Citation (APA, best effort from the document):** Vahtivuori-Hänninen, S., Halinen, I., Niemi, H., Lavonen, J., & Lipponen, L. (2014). A new Finnish national core curriculum for basic education (2014) and technology as an integrated tool for learning. In H. Niemi et al. (Eds.), *Finnish innovations & technologies in schools*. Sense Publishers. https://doi.org/10.1007/978-94-6209-749-0_2
- **File:** Literature/Literature on AI literacy/Related Papers/Vahtivuori-Hänninen et al - 2014 - A new Finnish national core curriculum for basic education (2014) and.txt
- **Type:** position / descriptive (policy chapter)
- **Core claims:** Finland's 2014 core curriculum reform (approx. 10-year cycle, FNBE-led, highly collaborative) embeds ICT as an integrated tool for learning and defines seven transversal competences (thinking & learning to learn; cultural literacy & expression; self-care/daily skills/safety; multiliteracy; ICT competence; working life & entrepreneurship; participation & sustainable future). Local authorities and highly trained teachers have substantial autonomy; the national document sets aims, not learning-outcome standards or prescribed methods.
- **Evidence/methods:** Descriptive account of the reform process, values and drafts, citing ATC21S (Binkley et al., 2012), KeyCoNet, PISA teacher-survey data and FNBE documents.
- **Relevance to our paper:** A national model for embedding digital/ICT competence cross-curricularly with aims-based (not test-based) assessment — a benchmark for our curriculum's Content and Assessment dimensions. [policy] [content-frameworks] [assessment] [pedagogy] [ai-literacy-def]
- **Key points with locations:**
  - Seven 21st-century transversal competences listed, incl. ICT competence (section "Collaborative and iterative planning…").
  - Assessment's purpose is "to promote learning and to encourage the learner"; self/peer assessment crucial; no national cohort tests or school rankings (same section).
  - Gamification and "joy of learning" emphasized; ICT used systematically across all grades and subjects (section "Versatile Environments for Learning").
- **Caveats:** Original .txt was unreadable (PDF font-encoding artifacts/control characters); content was recovered via a cleaned copy and verified by decoding the Caesar-shifted body text. Book page range not visible in the text.

## [24] Global Education Monitoring Report 2023: Technology in Education – A Tool on Whose Terms?

- **Citation (APA, best effort from the document):** UNESCO. (2023). *Global education monitoring report 2023: Technology in education — A tool on whose terms?* UNESCO Publishing.
- **File:** Literature/Literature on AI literacy/Related Papers/UNESCO - 2023 - Global education monitoring report 2023 Technology in education — A tool on.txt
- **Type:** report
- **Core claims:** Digital technology has changed but not transformed education; its value must be judged on equity, quality and efficiency, and the evidence base is weak, fast-outdated and partly industry-shaped. Access remains deeply unequal (1 in 4 primary schools lack electricity; 40%/50%/65% of primary/lower-/upper-secondary schools have internet), and governance lags (89% of 163 child-recommended edtech products could collect children's data; only 16% of countries guarantee education data privacy by law).
- **Evidence/methods:** Global synthesis of administrative data (UIS), surveys (TALIS, ICILS, TIMSS, PISA), PEER law/policy mapping, commissioned reviews and case studies.
- **Relevance to our paper:** Authoritative guardrails for our Context and Safeguards dimensions: effectiveness depends on pedagogy and contextualization, not device sophistication; digital skills and SEL need explicit curricula and teacher development. [policy] [safeguards-behaviors] [ai-literacy-def] [age-appropriateness] [ethics]
- **Key points with locations:**
  - Edtech shows small-to-medium positive learning effects with major evidence limits; One Laptop Per Child Peru (>1M laptops) had no learning impact; digital game-based learning improved maths outcomes across 43 studies, 2008–19 (Ch. 4 Key Messages).
  - ~90% of countries aspire to develop digital skills, 54% have standards; many adopt narrow commercial frameworks; only 3.2% of females vs 6.5% of males in 50 countries can write a computer program (Ch. 5 Key Messages).
  - AI shifts demand at task level; AI-complementary skills (tool selection, prompting, critical interpretation) appear in <1% of job ads; socioemotional skills gain weight (Focus 15.1, pp. 254–256). SEL: OECD survey in 10 cities shows an adolescent dip and a growing gender gap in emotional control by age 15; SEL theory informs edtech emotional design with mixed evidence (Focus 18.1, pp. 282–284).
- **Caveats:** 547-page report; the thematic part (Ch. 1–10 + report-level Key Messages) was read in full, but monitoring chapters 12–22 were covered only via the two technology-linked Focus boxes (15.1, 18.1) and Ch. 11's overview.

## [25] Faut-il interdire les téléphones portables à l'école pour protéger le développement cognitif des enfants? [Should mobile phones be banned at school to protect children's cognitive development?]

- **Citation (APA, best effort from the document):** Jacob, L., Laurenty, O., & Saayed, I. (n.d.). *Faut-il interdire les téléphones portables à l'école pour protéger le développement cognitif des enfants?* [Unpublished slide deck], course "Développement cognitif et apprentissage". (In French.)
- **File:** Literature/Literature on AI literacy/Related Papers/Jacob et al - n.d. - Faut-il interdire les téléphones portables à l'école.txt
- **Type:** position (student evidence-review presentation)
- **Core claims:** Weighs banning vs. pedagogically integrating phones for 6–12-year-olds: phones impair attention via limited cognitive resources, working-memory bottleneck and multitasking, yet can serve retrieval practice and engagement (e.g., Kahoot); concludes evidence is insufficient/mixed for outright bans.
- **Evidence/methods:** Slide-based review citing Dempsey et al. (2019, Growing Up in Ireland: phone ownership at age 9 associated with lower test scores at 9 and 13, cumulative effect), Soldatova et al. (2019, media multitasking), Meri et al. (2022/2023, screen exposure and reduced functional connectivity in attention networks), Sung et al. (2016, meta-analysis favouring mobile integration), Böttger & Zierer (2024, rapid review of bans), plus critiques of Beland & Murphy (2016) (small effect size ~0.06; non-replication in Norway/Sweden).
- **Relevance to our paper:** Directly age-relevant (6–12) evidence on devices, attention and wellbeing; supports structuring robot-based activities to avoid cognitive overload and unmanaged multitasking. [safeguards-behaviors] [age-appropriateness] [pedagogy]
- **Key points with locations:**
  - Stakeholder grid (teachers/parents/pupils) and >60 countries with classroom phone bans per GEM report (slide "Analyse des pièces…").
  - Dempsey et al. (2019): ownership at 9 (40%) vs 13 (98%); early ownership linked to lower academic scores (slides "Étude principale (1)").
  - High screen exposure linked to weaker functional connectivity in attention/cognitive-control networks (slide "Étude 3").
- **Caveats:** File name is a misnomer — content is a French student slide deck on phone bans, not a paper on digital citizenship/internet safety; references slide is truncated, so cited works were verified only as named on slides.

## [26] CASEL's SEL Framework: What Are the Core Competence Areas and Where Are They Promoted?

- **Citation (APA, best effort from the document):** Collaborative for Academic, Social, and Emotional Learning (CASEL). (n.d.). *CASEL's SEL framework: What are the core competence areas and where are they promoted?* https://www.casel.org/what-is-SEL
- **File:** Literature/Literature on AI literacy/Related Papers/CASEL - n.d. - CASEL's SEL framework What are the core competence areas.txt
- **Type:** framework
- **Core claims:** SEL is the process of acquiring/applying knowledge, skills and attitudes to develop healthy identities, manage emotions, achieve goals, show empathy, maintain relationships and make caring decisions. The "CASEL 5" (self-awareness, self-management, social awareness, relationship skills, responsible decision-making) applies across developmental stages and cultures, advanced equitably through coordinated settings.
- **Evidence/methods:** Framework brief synthesizing research; specifies SAFE instruction (Sequenced, Active, Focused, Explicit) and four key settings (classrooms, schools, families/caregivers, communities).
- **Relevance to our paper:** Provides a validated competence vocabulary for the social-emotional goals of robot-mediated collaborative learning and a systemic implementation lens for our Pedagogy and Context dimensions. [content-frameworks] [pedagogy] [age-appropriateness]
- **Key points with locations:**
  - CASEL 5 definitions with example sub-skills (section "The CASEL 5").
  - Classroom approaches: explicit instruction, cooperative/project-based learning, SEL integrated into academic subjects; SAFE quality criteria (section "The Key Settings — Classrooms").
  - SEL as lever for educational equity via school-family-community partnerships (sections "Schools", "Families/Caregivers", "Communities").
- **Caveats:** Short promotional brief; no publication date in the document (the 2020 framework update date is not printed); no primary evidence reported.

## [27] How Educational Are "Educational" Apps for Young Children? App Store Content Analysis Using the Four Pillars of Learning Framework

- **Citation (APA, best effort from the document):** Meyer, M., Zosh, J. M., McLaren, C., Robb, M., McCaffery, H., Golinkoff, R. M., Hirsh-Pasek, K., & Radesky, J. (2021). How educational are "educational" apps for young children? App store content analysis using the Four Pillars of Learning framework. *Journal of Children and Media, 15*(4), 526–548. https://doi.org/10.1080/17482798.2021.1882516
- **File:** Literature/Literature on AI literacy/Related Papers/Meyer et al - 2021 - How educational are educational apps for young children App store content.txt
- **Type:** empirical (content analysis)
- **Core claims:** Operationalizes the Four Pillars (Active "minds-on" learning, Engagement in the learning process, Meaningful learning, Social interaction) into a reliable 0–3 coding scheme and finds the top-downloaded "educational" apps are largely low quality: 58% scored ≤4/12. Free apps scored significantly worse on Engagement (Pillar 2) and overall, due to disruptive advertising and distracting rewards — a potential "digital quality divide" for lower-SES children.
- **Evidence/methods:** 124 apps (Google Play top free/paid, Apple top free/paid, plus 24 most-played apps from a preschool cohort study), double-coded (~20 min each; ICC .657–.947); t-tests, chi-square, Spearman correlations.
- **Relevance to our paper:** Supplies an operational, developmentally grounded rubric for judging whether learning activities are active, undistracted, meaningful and socially interactive — transferable criteria for our Didactics and Pedagogy dimensions and for arguing why a physical social robot (Marty) plus co-play beats screen-only "educational" media. [didactics] [content-frameworks] [age-appropriateness] [hands-on] [assessment]
- **Key points with locations:**
  - Coding scheme anchors per pillar (pp. 530–533; full scheme Appendix A, pp. 544–545).
  - 73% low-quality on Active Learning, 76% on Engagement, 64% on Meaningful Learning, 87% on Social Interaction; only 7 apps scored >8 (pp. 533–535).
  - Free vs paid: Pillar 2 (p < .0001) and total (p < .0047) significantly lower for free apps; non-profit PBS KIDS apps scored higher (p. 537).
- **Caveats:** US app stores, 2018–19 snapshot, preschool target (younger than our 11–12-year-olds); authors note scores are not absolute quality measures and do not link to measured learning gains.
