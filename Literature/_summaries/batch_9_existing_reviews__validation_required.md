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
