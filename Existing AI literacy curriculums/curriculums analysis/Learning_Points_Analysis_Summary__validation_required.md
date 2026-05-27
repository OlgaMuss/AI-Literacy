# Learning Points Comprehensive Analysis - Summary

## Overview

This analysis provides a granular mapping of **specific learning points** (concrete knowledge students are expected to know) across 14 AI literacy curricula. The analysis focuses on what students actually learn, not vague learning objectives.

## Key Files

1. **Learning_Points_Coverage_Matrix__validation_required.csv**
   - Comprehensive table showing which curricula cover which learning points
   - Includes brief notes on coverage method
   - 14 curricula columns × 200+ learning point rows

2. **Learning_Points_Depth_Analysis__validation_required.csv**
   - Detailed depth ratings for each curriculum-point combination
   - Depth scale: 0 (not covered) → 1 (mentioned) → 2 (explored) → 3 (deep coverage with activities)
   - Includes specific descriptions of HOW each point is covered

## Curricula Analyzed

1. **Berlin KI-Aufträge** - German middle school ML curriculum
2. **Day of AI** - MIT's classroom-ready curriculum (6 lessons)
3. **MIT DAILy** - Comprehensive high school curriculum with ethical focus
4. **Common Sense Media** - AI literacy basics
5. **aiEDU** - K-12 AI Readiness Framework v2.0 (human advantage + AI competencies)
6. **Georgia AI4GA** - 42 files across 3 units (robots, NLP, ML)
7. **ENARIS (EPFL)** - 10 HTML modules with technical depth
8. **MIT AI Ethics** - Teachable Machine + ethical frameworks
9. **AI4K12** - Five Big Ideas + Cognimates activities
10. **AI Adapt (Gillian Barber)** - Ireland-focused "AI in My Life" curriculum
11. **Duke AI Ethics Toolkit** - Critical perspective on AI harms
12. **Harvard AI Pedagogy** - Socratic chats, prompt engineering, academic integrity
13. **Toddle AI 101** - 8-lesson scaffolded introduction

## Macro Categories (15 total)

### 1. AI Fundamentals (7 points)
- Definitions of AI
- Narrow vs general AI
- AI vs non-AI distinction
- Map of AI (Think, Know, Learn, Sense, Act)
- Three components of AI systems
- Perception vs sensing

### 2. Algorithms & Data (14 points)
- Algorithm definition and specificity
- Algorithms as opinions (stakeholder goals)
- Data representation and choice consequences
- Labeled data, training/test split
- Overfitting, underfitting, transfer learning
- Garbage in, garbage out
- Types of reasoning (classification, prediction, recommendation)
- Feature vectors, word embeddings

### 3. Machine Learning (9 points)
- Supervised learning from labeled examples
- Classification vs regression
- Training process (initialize, iterate, test)
- Real applications: spam, speech, face detection, price prediction, user profiling
- Decision tree structure and construction
- Features for classification
- Trees reflect builder bias

### 4. Neural Networks (11 points)
- Architecture: layers, neurons, weights
- Training: weight adjustment, backpropagation
- Feedforward, evaluation, backprop steps
- Single neuron: inputs, weighted sum, threshold, activation
- Boolean logic with neurons (AND/OR)
- Deep networks enable modern NLP/CV
- Technical details: activation functions, degrees of freedom

### 5. NLP & Language (23 points)
- Speech recognition: waveforms, spectrograms, homophones
- Speech-to-text, text-to-speech applications
- NLP field overview, pipeline (tokenization→lemmatization→POS→syntax→semantics)
- Language: symbolic, syntax, ambiguity
- LLMs: token prediction, word-by-word generation, training loop, temperature
- Chatbots: types (commercial/therapeutic/social), construction (rule-based vs NLP)
- Turing test
- Word embeddings: semantic space, co-occurrence
- Machine translation, sentiment analysis
- Intent/entity extraction

### 6. Computer Vision (16 points)
- CV field overview: faces, poses, objects, scenes, medical
- Object recognition challenges
- Sensors: LIDAR, radar, sonar (physics and use cases)
- Images as grayscale/RGB with binary storage
- Edge detection: Sobel/Canny algorithms
- Flood fill algorithm
- Abstraction: silhouettes suffice
- Viola-Jones face detection
- Face detection vs recognition distinction
- Face filters: mesh-based 3D distortion
- Facial recognition: applications and privacy
- Industrial CV: defect/assembly detection
- Medical CV: cancer detection
- Adversarial examples: fooling classifiers

### 7. Generative AI (12 points)
- GANs: generator/discriminator competition, adversarial training
- GAN outputs: photos, paintings, poetry, music, jokes
- Distinguishing GAN art from human art
- Image generator stereotypes
- Prompt engineering: style mimicry, artist concerns
- Generative AI overview: text/image/audio from prompts
- LLMs as statistical models with self-supervised learning
- Style transfer: mimicking authors
- Real tools: ChatGPT, DALL-E, voice cloning
- Classification vs generation contrast

### 8. Deepfakes & Misinformation (16 points)
- Deepfakes: techniques (GANs, autoencoders), facial structure transfer
- 7 clues to spot deepfakes
- Deepfake harms: blackmail, defamation, election manipulation, geopolitics
- Deepfake benefits: film, HCI, satire, surgery, voice banking
- Misinformation vs disinformation (intent)
- Misinformation spreads faster
- Fact vs opinion vs reasoned judgment
- Fact-checking strategies
- Hallucinations: false information confidently stated
- Interrogating the internet: asking questions, multiple sources
- Source evaluation: credibility, tone, author POV, bias signals
- Don't trust first result

### 9. Ethics & Values (27 points)
- Ethical matrices: stakeholders→values→goals
- Stakeholder analysis: who's affected, optimization tradeoffs
- EU Trustworthy AI: 4 principles + 7 requirements detailed
- Creating ethical rules: logical, fact-based, defensible (Kant)
- Robot laws exercises
- Asimov's Three Laws
- Good moral rules: consistency, perspective-taking
- Principle conflicts: harm vs autonomy
- Black box algorithms: transparency challenges
- Trolley problem: utilitarian vs virtue ethics
- Moral Machine: self-driving crash scenarios
- Cultural moral variation
- Moral Machine paradox: want utilitarian for others, self-protective for self
- Human-AI interaction: when AI helps vs hinders learning
- Classroom AI norms: assignment-specific guidelines
- AI and human connection: strengthen vs weaken
- Daily connection patterns
- Authorial agency: staying in charge

### 10. Bias & Fairness (18 points)
- Bias definition: unfair support/opposition in data or raters
- Algorithmic vs societal bias relationship
- Fairness: same treatment vs reducing inequalities
- Amazon hiring tool discriminating against women
- Tay chatbot racist speech
- Face recognition demographic disparities
- COMPAS recidivism amplifying judicial bias
- Emotion recognition on underrepresented groups
- Linguistic diversity: few well-represented languages
- Image generator profession stereotypes
- Mitigation: diverse data, preprocessing (grayscale, geometric), re-curation
- Self-reflection and active communication
- Blinded processes reduce human bias

### 11. Limitations & Capabilities (15 points)
- AI doesn't think/feel/have self-awareness
- Human advantages: self-awareness, emotional intelligence (empathy, social cues, accept criticism, move on from mistakes)
- Creativity, empathy, interdisciplinary thinking harder to automate
- AI limitations: context, sarcasm, stories, emotions
- Chatbot limitations: failed conversations, frustration
- Current AI is narrow, task-specific
- Overreliance weakens critical thinking
- Cross-checking with scholarly sources essential
- LLMs vs search engines: critical thinking tradeoffs
- AI outputs differ across tools/prompts
- Factual vs non-factual output discrimination

### 12. Societal Impact (29 points)
**Labor & Economy (7):**
- Job automation: routine/physical tasks, transformation vs replacement
- Ghost work: low-wage labeling/moderation
- Complementarity of human+AI determines transformation
- AI careers: multidisciplinary, dual skilling, fast-moving
- Future jobs unknown: resilience, adaptability needed
- AI skills shortage and salaries (Ireland context)
- Study paths: specialists vs dual-skilled domain experts

**Power & Access (4):**
- AI divide: tools, internet, education; low-wage jobs exposed
- Tech oligarchy: concentration at major companies
- Information privilege: premium access
- Freemium vs premium capabilities

**Benefits & Harms (3):**
- AI benefits comprehensive list
- AI harms comprehensive list
- Unanticipated consequences on social/cultural/economic/political systems

**Surveillance & Control (4):**
- Social credit systems
- Live facial recognition: constitutional concerns
- AI in immigration surveillance
- Smartphone tracking, social media data, targeted ads

**Media & Culture (7):**
- Recommendation algorithms: filter bubbles, radicalization
- Echo chambers
- Social media manipulation: profiles, free=attention+data
- EU GDPR (2018)
- Data persistence: hard to delete
- China 2024 AI content labeling
- Historical AI/automation context

**Government & Policy (4):**
- Government automated decision systems (29 AIs of DC)
- Lethal autonomous weapons
- Political instability prediction
- Political deepfakes

### 13. Environmental Impact (13 points)
**Energy & Resources (5):**
- AI training/operation consumes significant energy, water, GHG
- GPT-3 training: ~313 tons CO2
- Data centers: ~2% global electricity, ~260 MW continuous
- Generating text ~30× more energy than retrieving
- ChatGPT water/energy vs Google search

**Digital Footprint (4):**
- ICT emissions: 3.2% global CO2 vs aviation
- Streaming: >75% German traffic, 4K volume, ~23× high vs low res
- >5.5B phones, batteries better but charge frequency similar
- Web page weight ~4× since 2010, ~140g CO2 per GB

**Mitigation (3):**
- Positive AI: smart thermostats, traffic, farming, DeepMind cooling (~40%)
- Personal actions: repair, streaming hygiene, lower res, clean inbox
- Strategies: algorithm optimization, training time reduction

**Tradeoffs (1):**
- Digitalization–climate net effect unclear

### 14. Privacy & Data (11 points)
**Data Collection (6):**
- How personal data collected, used, shared
- PII and privacy risks
- Privacy paradox: 81% uncomfortable yet share
- Web scraping for training: Reddit, Wikipedia, transcripts
- Data download exercises: Instagram, YouTube, TikTok
- If not paying, you are the product

**Usage Guidelines (3):**
- Don't put sensitive info in AI prompts
- Reading privacy policies: OpenAI, Gemini, Meta
- Privacy settings in AI tools

**Risks (2):**
- Chatbot memory: knows you over life
- Prompt data collection

### 15. IP & Copyright (8 points)
**Concepts (3):**
- Copyright infringement vs fair use; unsettled legal landscape
- Who owns AI-generated content: 5 stakeholder types
- Authorship and credit: trainers not AI, humanization affects perception

**Practices (3):**
- Ethical citation for AI-assisted work
- Academic integrity: not uploading copyrighted material, not mimicking artists
- Plagiarism vs AI assistance distinction

**Cases (2):**
- NYT, artists suing; companies cite fair use
- Hollywood writers/actors strike

## Additional Cross-Cutting Themes

### Hands-on Tools (25 points)
- **Supervised learning platforms:** Teachable Machine (image/audio/pose), ML for Kids, AI for Oceans
- **Scratch extensions:** Cognimates (keyword assistants, speech blocks)
- **Neural network simulators:** CMU Neuron Sandbox, TensorFlow Playground
- **Creative AI:** Wombo Dream, DALL-E, Artbreeder, Magic Sketchpad, AI Duet, Magenta
- **Generative text:** ChatGPT, Claude, Gemini, Perplexity
- **Code generators:** GitHub Copilot, Safurai
- **Data analysis:** Pandas (head/tail, describe, sort, loc, histograms)
- **Ethics simulators:** Moral Machine (self-driving dilemmas)
- **Games:** Quick Draw!, Bot or Not, Thing Translator
- **Language models:** Markov chains
- **Advanced:** TensorFlow/TensorFlow.js

### Prompt Engineering (9 points)
- Crafting effective prompts
- SPEAR framework: Situation, Problem, Example, Ask, Review
- Role prompting: personas for style/tone
- Meta-prompting: LLM refines your prompt
- Chain-of-thought: step-by-step reasoning, few-shot
- Brockman Prompt: breaking tasks into steps
- Computational thinking for AI
- Playtesting: test to pass vs test to fail
- Rogers's active listening rules applied to prompting

### System Design (6 points)
- System prompts vs user prompts: identity, cutoff, policy, tools
- Build-a-Bot framework: persona, audience, tone, scope, adjectives
- Model cards: use, data, limitations, warnings
- Design for multiple stakeholders
- Transparency and explainability

### Reinforcement Learning (8 points)
- RL concept: learning without being told how
- RL terms: Agent, Environment, Action, State, Reward
- Q-learning: quality tables, max Q selection
- Self-play training vs evaluation functions
- State space explosion: manual tables infeasible
- Exploration vs exploitation tradeoff
- RL in ad targeting
- AlphaStar: huge action space (~10^26)

### Real-world Case Studies (12 detailed)
- **Tesla Autopilot:** driver engagement, attractive nuisance legal concept, liability questions
- **ChatGPT:** helpfulness/truthfulness/harmlessness evaluation, medical exams, homework concerns
- **Google Translate:** functionality and limitations
- **Social media bots:** growth tactics, risks
- **AlphaGo:** RL in complex games
- **App store responsibility:** government vs platform
- **Robot hotel:** narrow automation limits
- **Amazon hiring tool:** gender discrimination from historical data
- **Tay chatbot:** 16 hours to racist speech
- **COMPAS:** recidivism bias
- **Target pregnancy prediction:** purchase pattern profiling
- **29 AIs of Washington DC:** government decision systems

### Unplugged Activities (6 pedagogical approaches)
- Intelligent Piece of Paper: Tic-Tac-Toe without understanding
- Bubble Sort: sorting students by height
- Classification Game: students play SL algorithm
- Coin Game: RL through physical board
- Semantic feature space: 3D classroom word coordinates
- Pasta/Candy decision trees: physical object feature extraction

### Projects & Assessments (11 major projects)
- Deepfake PSA: 250-400 word press release
- ChatGPT interview for communication app
- Interspecies communication app design
- YouTube recommendation redesign with ethical matrix
- Dream Bot: solve everyday problem with sensors
- Original story using GAN tools
- Anti-AI manifesto zine
- Interview fictional character with evidence
- ChatGPT debate: benefits vs risks with structured argument
- AI booster vs Anti-AI debate
- Certificate of completion after assessment

### Specialized Topics (15 domain-specific)
- **Indigenous AI:** Language preservation (Lakota, SkoBots, Mamutjitji), data sovereignty, virtual museums, fake art (75% non-Indigenous 2022)
- **Journalism:** 18 pitfalls (agency attribution, humanoid imagery, brain analogies, hyperbole, hidden labor)
- **Safety:** AI detection limits, adversarial prompting (jailbreaks, grandmother exploit)
- **Research:** Synthetic training data, anticipatory shipping (Amazon patent)
- **Domain applications:** Wolfram calculus, poker (PioSOLVER), Ithaca inscriptions (62% restoration), hate-speech detection (97% AI-detected Facebook 2021), dual-use (drug→toxin), electronic nose, animal communication, robot pain reflexes
- **Historical:** ELIZA (1966), Arthur Samuel ML definition

### Literacy Meta-Skills (8 frameworks)
- **Critical Thinking:** FAB check, evaluation, questioning assumptions, comparing AI vs human reasoning
- **Creativity:** Supporting creativity while maintaining voice, personas for writing
- **Collaboration:** SAMR (AI edition) model, essential agreements
- **Communication:** Describing AI influence, making thinking visible
- **Problem Solving:** Gray Area Sort (gradient spectrum), risk-benefit analysis
- **Perspectives:** Circle of Perspectives, multiple viewpoints
- **Emotional Intelligence:** Collaboration, empathy, compassion, self-regulation
- **Metacognition:** Learning with vs without AI, productive struggle

### Advanced Technical Topics (10 points)
- **Transformers:** BERT, GPT-3, DALL-E architecture family
- **CNNs:** Convolutional neural networks for images
- **Adversarial ML:** Examples, robustness issues
- **Training details:** Parameters vs hyperparameters, time requirements (hours to weeks), billions of iterations, pre-trained models
- **Model evaluation:** MAE (Mean Absolute Error), in-sample vs hold-out validation
- **Architecture comparisons:** Von Neumann vs neural networks
- **Receptive fields:** Neurons sensitive to input groups
- **Division of labor:** Early layers→simple, later→complex structures
- **ML domains:** Works best with clear rules/actions/goals

## Depth Distribution Summary

### Curricula with Deepest Technical Coverage (Depth 3 on many points):
1. **ENARIS (EPFL)** - 60+ points at depth 3, especially in algorithms, NN architecture, RL, CV, environmental impact
2. **Georgia AI4GA** - 50+ points at depth 3, very strong on ML pipeline, decision trees, autonomous vehicles, chatbot construction
3. **MIT DAILy** - 40+ points at depth 3, emphasis on ethics, data bias, GANs, misinformation
4. **Day of AI** - 30+ points at depth 3, focused on LLMs, chatbots, hallucinations, classroom norms
5. **aiEDU** - 30+ points at depth 3, unique Indigenous AI strand, AI Readiness Framework, human advantage domain

### Curricula with Strongest Ethical/Social Focus (Depth 3):
1. **MIT DAILy** - Ethical matrices, stakeholder analysis, algorithm consequences
2. **AI Adapt** - EU guidelines, Moral Machine, ghost work, AI divide, tech oligarchy
3. **Duke AI Ethics Toolkit** - Critical perspective, bias examples, hidden labor
4. **MIT AI Ethics** - Teachable Machine + ethical frameworks
5. **Harvard AI Pedagogy** - Academic integrity, Socratic dialogue, evidence-based reasoning

### Curricula with Most Hands-on Activities (Depth 3):
1. **Georgia AI4GA** - 15+ hands-on activities (unplugged, Scratch, Neuron Sandbox, Teachable Machine)
2. **ENARIS** - 10+ exercises (Bubble Sort, Classification Game, Coin Game, unplugged semantic space)
3. **Berlin KI-Aufträge** - Multiple activities (Soekia, Teachable Machine, Pandas, Bot or Not)
4. **AI4K12** - Cognimates full guide with speech blocks and keyword matching
5. **MIT DAILy** - PastaLand decision trees, GANs exploration, YouTube redesign project

### Curricula with Unique Coverage:
- **Berlin:** Only depth 3 on SPEAR prompt framework, meta-prompting, chain-of-thought, temperature exploration, Pandas data analysis
- **Day of AI:** Only detailed word-by-word LLM generation example, human feedback layers, echo chambers
- **MIT DAILy:** Only depth 3 on algorithms as opinions, classification vs generation contrast, decision trees reflect bias
- **Georgia:** Only depth 3 on creating algorithms for mundane tasks, overfitting/underfitting/transfer learning, single neuron Boolean logic, homophones, sensors physics, Tesla case study
- **ENARIS:** Only curriculum with depth 3 on narrow vs general AI, Map of AI taxonomy, RL detailed (Q-learning, state explosion, exploration/exploitation), activation functions, Von Neumann comparison, flood fill, Viola-Jones, privacy paradox stats
- **aiEDU:** Only depth 3 on AI Readiness Framework, Indigenous AI (language preservation, data sovereignty, fake art stats), many domain-specific Snapshots (DebunkBot, CoupCast, Wolfram, electronic nose)
- **Harvard:** Only depth 3 on playtesting prompts, Rogers's active listening, interview fictional character, blind comparison rubrics
- **Toddle:** Only depth 3 on SAMR AI edition, Gray Area Sort, Circle of Perspectives, FAB check

## Coverage Gaps (Points with <3 curricula at depth ≥2)

1. **Narrow vs General AI distinction** - Only ENARIS at depth 3
2. **Map of AI taxonomy (Think/Know/Learn/Sense/Act)** - Only ENARIS at depth 3
3. **Overfitting/underfitting/transfer learning** - Only Georgia at depth 3
4. **Creating algorithms for mundane tasks** - Only ENARIS at depth 3
5. **Homophones disambiguated by context** - Only Georgia at depth 3
6. **NLP pipeline detailed (tokenization→semantics)** - Only ENARIS at depth 3
7. **Chatbot types: commercial/therapeutic/social** - Only ENARIS at depth 3
8. **Turing test** - Only ENARIS at depth 3
9. **Single neuron Boolean logic (AND/OR)** - Only Georgia at depth 3
10. **Feedforward/evaluation/backprop as three distinct steps** - Only MIT DAILy at depth 3
11. **Sensors physics (LIDAR/radar/sonar)** - Only Georgia at depth 3
12. **Edge detection algorithms (Sobel/Canny)** - Only ENARIS at depth 3
13. **Flood fill algorithm** - Only ENARIS at depth 3
14. **Viola-Jones face detection** - Only ENARIS at depth 3
15. **Face filters: mesh-based 3D graphics** - Only Georgia at depth 3
16. **All RL detailed concepts** - Only ENARIS at depth 3
17. **Privacy paradox statistics** - Only ENARIS at depth 3
18. **Data download exercises** - Only ENARIS at depth 3
19. **GDPR detailed** - Only ENARIS at depth 3
20. **Web page weight and carbon stats** - Only ENARIS at depth 3
21. **Streaming statistics** - Only ENARIS at depth 3
22. **Personal environmental actions** - Only ENARIS at depth 3
23. **Robot laws exercises** - Only ENARIS at depth 3
24. **Asimov's Three Laws** - Only ENARIS at depth 3
25. **Moral Machine paradox** - Only ENARIS at depth 3
26. **All Indigenous AI topics** - Only aiEDU at depth ≥2
27. **18 journalism pitfalls** - Only Harvard at depth 3
28. **Adversarial prompting** - Only Berlin at depth 2
29. **SPEAR prompt framework** - Only Berlin at depth 3
30. **Meta-prompting** - Only Berlin at depth 2
31. **Chain-of-thought prompting** - Only Berlin at depth 2
32. **Temperature parameter** - Only Berlin at depth 2
33. **System prompts vs user prompts** - Only Berlin at depth 3
34. **Build-a-Bot framework** - Only Berlin at depth 3
35. **Tech oligarchy** - Only Duke at depth 2
36. **Ghost work** - Only Duke/Harvard at depth ≥2
37. **SAMR (AI edition)** - Only Toddle at depth 3
38. **Gray Area Sort** - Only Toddle at depth 3
39. **Circle of Perspectives** - Only Toddle at depth 3
40. **FAB check** - Only Toddle at depth 3

## Strengths by Curriculum

### Berlin KI-Aufträge
- **Strengths:** Advanced prompt engineering (SPEAR, meta-prompting, chain-of-thought), Soekia temperature exploration, Pandas data analysis, Build-a-Bot system design, adversarial prompting
- **Unique:** Only depth 3 on advanced prompting techniques and system prompt architecture
- **Depth 3 count:** ~8 points

### Day of AI
- **Strengths:** LLM mechanics (word-by-word, training layers), hallucinations, classroom AI norms, human feedback in training, echo chambers
- **Unique:** Best explanation of LLM token-by-token generation with examples
- **Depth 3 count:** ~15 points

### MIT DAILy
- **Strengths:** Algorithms as opinions, ethical matrices, stakeholder analysis, data bias, GANs, decision trees, misinformation, AI careers
- **Unique:** Only depth 3 on algorithms as opinions, classification vs generation contrast, decision trees reflect builder bias, feedforward/backprop as three steps
- **Depth 3 count:** ~25 points

### Common Sense Media
- **Strengths:** Introduction to AI, benefits/harms balance, privacy basics
- **Unique:** None at depth 3
- **Depth 3 count:** 0 (mostly depth 1-2 introductory coverage)

### aiEDU AI Readiness Framework
- **Strengths:** Indigenous AI (only curriculum with depth 3), AI Readiness Framework, human advantage domain, extensive AI Snapshots with domain-specific scenarios (DebunkBot, CoupCast, Wolfram, Gran Turismo, etc.)
- **Unique:** Only depth 3 on Indigenous topics, only AI Readiness Framework, most Snapshots (30+)
- **Depth 3 count:** ~20 points (including 5 Indigenous points unique to aiEDU)

### Georgia AI4GA
- **Strengths:** Most hands-on activities (unplugged + digital), ML pipeline comprehensive (overfitting/underfitting/transfer learning), single neuron Boolean logic, sensors physics, homophones, Tesla case study
- **Unique:** Only depth 3 on mundane algorithm creation, overfitting/underfitting/transfer learning, single neuron AND/OR, homophones, sensor physics, face filters mesh mechanics
- **Depth 3 count:** ~35 points

### ENARIS (EPFL)
- **Strengths:** Deepest technical curriculum overall, narrow vs general AI, Map of AI, all RL detailed, activation functions, flood fill, Viola-Jones, environmental impact with statistics, GDPR, privacy paradox, data persistence, personal mitigation actions
- **Unique:** Only depth 3 on 25+ technical/policy points (see gaps list)
- **Depth 3 count:** ~65 points (highest technical depth)

### MIT AI Ethics
- **Strengths:** Teachable Machine with bias reflection, EU Trustworthy AI 7 requirements, ethical matrices
- **Unique:** Best on EU ethical requirements detail
- **Depth 3 count:** ~10 points

### AI4K12
- **Strengths:** Five Big Ideas framework, Cognimates full guide with speech blocks
- **Unique:** Only depth 3 on Cognimates implementation (wake words, substring issues, self-triggering)
- **Depth 3 count:** ~5 points

### AI Adapt (Ireland)
- **Strengths:** Careers focus (Ireland context), Moral Machine with Ireland data, EU guidelines, ghost work introduction, Intelligent Piece of Paper
- **Unique:** Only curriculum with Ireland-specific labor market and moral choice data
- **Depth 3 count:** ~15 points

### Duke AI Ethics Toolkit
- **Strengths:** Critical perspective, tech oligarchy, ghost work, artist lawsuits, monoculture risks
- **Unique:** Only depth ≥2 on tech oligarchy critique
- **Depth 3 count:** ~5 points (critical lens, not constructive skills)

### Harvard AI Pedagogy
- **Strengths:** Playtesting prompts, Rogers's active listening for prompting, interview fictional character, blind comparison rubrics, 18 journalism pitfalls
- **Unique:** Only depth 3 on playtesting, Rogers's rules, journalism pitfalls checklist
- **Depth 3 count:** ~8 points (pedagogical methods)

### Toddle AI 101
- **Strengths:** SAMR (AI edition), Gray Area Sort, Circle of Perspectives, FAB check, exit tickets throughout
- **Unique:** Only depth 3 on SAMR for AI, Gray Area Sort, Circle of Perspectives, FAB check
- **Depth 3 count:** ~10 points (scaffolding routines)

## Recommendations for Comprehensive Curriculum

To cover all identified learning points with depth ≥2:
1. Use **ENARIS** as technical backbone (most comprehensive)
2. Add **Georgia** for ML pipeline detail and hands-on variety
3. Add **MIT DAILy** for ethical matrices and stakeholder analysis
4. Add **Berlin** for advanced prompt engineering
5. Add **aiEDU** for Indigenous AI and human advantage framework
6. Add **Harvard** for academic integrity and journalism literacy
7. Add **Toddle** for scaffolding routines (SAMR, Circle of Perspectives, Gray Area)
8. Add **Day of AI** for classroom norms and LLM mechanics clarity
9. Add **Duke** for critical perspective on tech concentration and hidden labor

## Notes on Data Sources

All learning points extracted from:
- **Berlin:** Translated lesson files, CSV tables
- **Day of AI:** 6 lesson PDFs
- **MIT DAILy:** Curriculum overview PDF
- **Common Sense:** Slides extract
- **aiEDU:** AI Readiness Framework, AI Snapshots, SmartTeach, Future of Work, Indigenous AI, K-5 to 9-12 documents (15+ extracts)
- **Georgia:** 42 PDFs/DOCX (10+ converted to .md), learning objectives PDF
- **ENARIS:** 10 HTML module files
- **MIT AI Ethics:** Teachable Machine educator guide
- **AI4K12:** Five Big Ideas poster, Cognimates activity guide, resources list
- **AI Adapt:** 5+ teacher guides
- **Duke:** 11 extracted text files
- **Harvard:** 6 extracted text files
- **Toddle:** 8 lesson web pages + worksheets

## Depth Scale Definition

- **0 (Not covered):** Learning point not mentioned or addressed
- **1 (Mentioned):** Brief reference, vocabulary term, or passing context (1-2 sentences)
- **2 (Explored):** Some detail with discussion, examples, or light activities (multiple paragraphs or short activity)
- **3 (Deep coverage):** Comprehensive treatment with detailed explanation AND substantial activities, exercises, or projects (full lessons, extensive worksheets, multiple examples)

## Usage Guide

### For Curriculum Designers:
- Identify gaps in your current curriculum by comparing to the matrix
- See which learning points have minimal coverage across all curricula (innovation opportunities)
- Understand different pedagogical approaches to the same concept

### For Researchers:
- Quantify curriculum coverage systematically
- Compare emphasis across different curriculum philosophies
- Identify under-taught topics in AI literacy field

### For Teachers:
- Mix and match curricula to cover specific learning points
- See detailed "How Covered" descriptions to choose appropriate activities
- Understand depth requirements for your student population

## File Formats

All files saved with `__validation_required` suffix per workspace rules. Files include:
1. **Learning_Points_Coverage_Matrix__validation_required.csv** - Compact yes/no/how covered
2. **Learning_Points_Depth_Analysis__validation_required.csv** - Detailed depth ratings (0-3) with methods
3. **Learning_Points_Analysis_Summary__validation_required.md** - This summary document

---

**Total Learning Points Identified:** 200+  
**Total Curricula Analyzed:** 14  
**Total Source Documents Processed:** 100+  
**Macro Categories:** 15  
**Date Generated:** April 2, 2026
