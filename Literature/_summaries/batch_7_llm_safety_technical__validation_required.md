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
