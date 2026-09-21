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
