# ENARIS (EPFL) - Learning Points Analysis

## Curriculum Overview
- **Developer:** EPFL (École Polytechnique Fédérale de Lausanne)
- **Format:** 10 HTML modules
- **Target Age:** Secondary school
- **Focus:** Most technically comprehensive curriculum with deep CS fundamentals
- **Unique Strengths:** Only curriculum with depth 3 on 25+ advanced topics including narrow vs general AI, Map of AI taxonomy, all RL details, environmental statistics, GDPR, privacy paradox

## Learning Points Coverage (Depth ≥2)

### AI Fundamentals (Depth 3)
1. **AI definition** - Reflective definition-building, 8 examples rated 0-5, multiple definitions shown
2. **Narrow vs General AI** - Wall-E movie analysis, fictional vs real capabilities, decades of narrow progress
3. **Map of AI: Think, Know, Learn, Sense, Act** - Detailed taxonomy with examples, students classify systems

### Algorithms (Depth 2-3)
1. **Algorithm definition** (Depth 3) - Bubble Sort, Tic-Tac-Toe exercises, create algorithm for mundane tasks (opening door, making breakfast)
2. **Algorithms need specificity** (Depth 3) - Distance, speed, rotation details emphasized
3. **Algorithms as opinions** (Depth 2) - Stakeholder discussions

### Data Concepts (Depth 3)
1. **Data as representation** - Fundamental concept, choice examples (height vs voice pitch)
2. **More data vs diversity** - Overfitting/underfitting, diverse dataset solutions
3. **Overfitting** - Portrait background features problem detailed with solutions
4. **Underfitting** - Movie revenue example with feature engineering
5. **Transfer learning** - Fire→fracture example, training time reduction

### Machine Learning (Depth 2-3)
1. **Supervised learning** (Depth 3) - Full Module 4: Classification Game, AI for Oceans, game controller
2. **Classification vs regression** (Depth 3) - Explicit in SL module
3. **Training process** (Depth 3) - 5-step detailed process
4. **Real SL applications** (Depth 3) - Extensive: auto-focus, social media tagging, industrial defects, medical scans, spam with features
5. **Spam filters** (Depth 3) - Millions of labels, content/subject/sender/time features detailed
6. **Classification Game** (Depth 3) - Unplugged: students play SL algorithm (pen-and-paper)
7. **Pre-trained models** (Depth 3) - Browser training enabled, game controller uses this
8. **Bias in ML** (Depth 3) - Amazon (1yr dev, male data, disbanded 2018), Tay (16h, Twitter), detailed societal→algorithmic relationship
9. **Mitigation** (Depth 3) - Diverse datasets, grayscale, geometric transforms, domain caveats (when helps vs hurts)

### Neural Networks (Depth 2-3)
1. **Architecture** (Depth 3) - Feed-forward detailed, layers and connections
2. **Neurons, weights, layers** (Depth 3) - Weights connect activations, receptive fields
3. **Weight adjustment** (Depth 3) - Learning rule detailed, backpropagation
4. **Single neuron** (Depth 2) - Linear threshold unit mentioned
5. **Activation functions** (Depth 3) - Sigmoid, ReLU, leaky ReLU with formulas, bounded-range explanation, bias term
6. **Degrees of freedom** (Depth 2) - Calculation objective
7. **Receptive field** (Depth 2) - Neurons sensitive to input groups
8. **Division of labor** (Depth 2) - Early layers→simple, later→complex
9. **Von Neumann vs NNs** (Depth 2) - ALU, control, memory, I/O comparison

### Computer Vision (Depth 2-3)
1. **Images as grayscale/RGB** (Depth 3) - Binary storage, 0-255 values fundamental representation
2. **Edge detection** (Depth 3) - Matrix math, horizontal+vertical+combine pipeline, Sobel/Canny algorithms
3. **Flood fill** (Depth 3) - Seed spread, boundary detection, Minesweeper/Paint uses, broken boundary limitations
4. **Abstraction** (Depth 3) - Silhouettes suffice exercise (elephant)
5. **Viola-Jones** (Depth 3) - Sliding window, Haar features, frontal faces only
6. **Face detection vs recognition** (Depth 3) - Explicit distinction
7. **Face filters** - 2D limitation noted
8. **Adversarial examples** (Depth 2) - Discussion slide: traffic light fooling

### Reinforcement Learning (Depth 3) - MOST DETAILED
1. **RL concept** - Learning without being told how, only goals and actions; Module 5 with OpenAI video
2. **RL terms** - Agent, Environment, Action, State, Reward (core vocabulary)
3. **Q-learning** - Q(state, action) quality table, pick highest Q, update from rewards detailed
4. **Self-play training** - Lc0 chess vs evaluation functions comparison
5. **State space explosion** - Chess ~10^44, hexapawn example, manual tables infeasible
6. **Exploration vs exploitation** - Coin game, MENACE, maze with suboptimal policies
7. **RL in ad targeting** - Application example
8. **AlphaStar** - Huge action space (~10^26 vs chess ~40) comparison
9. **Coin Game** (Depth 3) - Physical board RL training exercise with Q-table updates

### Natural Language Processing (Depth 2-3)
1. **Chatbots** (Depth 3) - Full Module 3: commercial (24/7), therapeutic (ELIZA/Woebot), social (empathy/humor/mood Mitsuku) types
2. **Turing test** (Depth 3) - History, Loebner Prize tiers (Gold/Silver/Bronze), simplified classroom version
3. **Chatbot construction** (Depth 3) - Rule-based click/flow vs free text+NLP, decision trees, loops, dead ends
4. **Chatbot design** (Depth 3) - Flowchart principles
5. **Chatbot limitations** - No awareness emphasized
6. **Social media bots** (Depth 2) - Hashtag growth, weak conversation, data theft
7. **ELIZA (1966)** (Depth 2) - Historical therapeutic chatbot

### Generative AI (Depth 2-3)
1. **GANs** (Depth 3) - Module 8: iterative training, style transfer, deepfake link
2. **Transformer architecture** (Depth 3) - BERT, GPT-3, DALL-E family explained
3. **Style transfer** (Depth 2) - Transformers in Arts module
4. **AI art tools** (Depth 3) - App lab: Wombo, DALL-E Mini, Gaugan2, Autodraw, AI Duet, Arbitrary Style Transfer with behavior descriptions
5. **Can AI create art?** (Depth 3) - Module 8: tool vs collaborator, authorship questions
6. **AI as collaborator** (Depth 3) - Holly Herndon Spawn as responsible example
7. **AI art examples** (Depth 3) - Barrat, Belamy (Christie's), Beethoven/Schubert completions, Botnik Harry Potter, Nees 1960s
8. **AI music** (Depth 2) - Examples in Arts module
9. **Botto** (Depth 2) - DAO + community voting, NFTs
10. **Prompt engineering for art** (Depth 2) - Authorship in Arts module

### Deepfakes (Depth 2-3)
1. **Deepfakes** (Depth 3) - Module 9: GANs+autoencoders, facial structure/expression transfer, large video pools
2. **Deepfake harms** (Depth 3) - Detailed list: blackmail, defamation, bullying, identity theft, election, geopolitics
3. **Deepfake benefits** (Depth 2) - Film, HCI, satire, surgery listed

### Ethics & Values (Depth 2-3)
1. **Ethical matrices** (Depth 2) - Throughout modules
2. **Stakeholder analysis** - Multiple contexts
3. **EU Trustworthy AI 4 principles** (Depth 3) - Human autonomy, Fairness, Harm prevention, Traceability with definitions, tensions, mitigation
4. **Creating ethical rules** (Depth 3) - Kant's universalization, perspective-taking, logical/fact-based/defensible
5. **Robot laws exercise** (Depth 3) - Robot butler activity with presentation, weak-point finding
6. **Asimov's Three Laws** (Depth 3) - Referenced as historical framework
7. **Good moral rules** (Depth 3) - Consistent cases, perspective-taking criteria
8. **Principle conflicts** (Depth 3) - Harm vs autonomy in predictive policing example
9. **Black box algorithms** (Depth 2) - Ethics module mention
10. **Trolley problem** (Depth 3) - Bentham (utilitarian) vs Kant (virtue ethics) detailed
11. **Moral Machine** (Depth 3) - moralmachine.net exercise with worksheet, decision log, discussion prompts
12. **Cultural moral variation** (Depth 2) - Mentioned in module
13. **Moral Machine paradox** (Depth 3) - Research results: want utilitarian for others, self-protective for self
14. **Perspective-taking** (Depth 2) - Emphasis throughout
15. **Transparency** (Depth 3) - Traceability principle, black box problem

### Environmental Impact (Depth 2-3) - MOST DETAILED
1. **AI energy/water/GHG** (Depth 3) - Module 10 full focus: ICT 3.2% CO2, data center stats
2. **GPT-3 training CO2** (Depth 3) - ~313 tons specific stat
3. **Data centers** (Depth 3) - ~2% global electricity, ~260 MW Google, virtualization, cooling upgrades
4. **ICT emissions** (Depth 3) - 3.2% vs aviation comparison
5. **Streaming statistics** (Depth 3) - >75% German/60% global traffic, 4K volume, ~23× high vs low res
6. **Phone statistics** (Depth 3) - >5.5B phones, batteries 50% better but charge frequency similar
7. **Web page weight** (Depth 3) - ~4× since 2010, ~140g CO2 per GB with WebsiteCarbon.com
8. **Positive AI for environment** (Depth 3) - Smart thermostats, traffic, farming, DeepMind cooling (~40%) detailed
9. **Personal actions** (Depth 3) - Repair, streaming hygiene, lower res, clean inbox detailed tips
10. **Mitigation strategies** (Depth 2) - Server virtualization, green hardware, behavior change
11. **Digitalization–climate tension** (Depth 2) - Net effect unclear discussion

### Privacy & Social Media (Depth 2-3)
1. **Personal data collection** (Depth 3) - Module 9: detailed profiles, ~1GB/user/day, Instagram ~1000 photos/sec
2. **Social media manipulation** (Depth 3) - Module 9 full focus: GDPR, data volume, targeted ads mechanism, filter bubbles
3. **EU GDPR** (Depth 3) - 2018 rules, processing, right to info, fines, EU-US Privacy Shield
4. **Data persistence** (Depth 3) - Internet Archive, Wayback Machine exercises with §78 UrhG, child protection, jurisdiction rights
5. **Privacy paradox** (Depth 2) - 81% uncomfortable yet share stat
6. **Web scraping** (Depth 2) - Module 9 mentions training data sources
7. **Data download exercises** (Depth 3) - Instagram, YouTube, TikTok step-by-step procedures
8. **If not paying, you're the product** (Depth 2) - Mentioned
9. **Recommendation algorithms** (Depth 2) - Ethics discussion

### Other Advanced Topics (Depth 2-3)
1. **TensorFlow/TensorFlow.js** (Depth 2) - Advanced option
2. **Deep networks enable NLP/CV** - Examples in modules
3. **CNNs** - Resources mention
4. **Training time** (Depth 2) - Hours to weeks noted
5. **ML best in clear domains** (Depth 2) - Games popular (RL context)
6. **Quiz activities** (Depth 3) - Multiple throughout modules

## Unplugged Activities
1. **Bubble Sort** (Depth 3) - Sorting students by height
2. **Classification Game** (Depth 3) - Students play SL algorithm
3. **Coin Game** (Depth 3) - RL board game
4. **Think-pair-share** (Depth 3) - Recommended throughout

## Total Learning Points with Depth ≥2: ~80 points

## Depth 3 Points: ~65 points (HIGHEST)
Focus areas: Complete technical depth across AI, ML, NN, RL, CV, NLP, environmental impact with statistics, GDPR, ethics

## Coverage Gaps (Minimal)
- Prompt engineering (SPEAR, meta-prompting)
- Indigenous AI
- Journalism literacy
- Academic integrity specifics
- Some hands-on coding (Pandas, modern LLM tools)

## Pedagogical Approach
- Unplugged activities for foundational concepts
- Technical exercises with calculations
- Philosophy and ethics integrated
- Environmental focus unique
- European policy context (GDPR, EU ethics)
- Statistics and research citations throughout
- Quiz-based assessment
- Movie examples (Wall-E for narrow AI)
- Think-pair-share collaborative learning
