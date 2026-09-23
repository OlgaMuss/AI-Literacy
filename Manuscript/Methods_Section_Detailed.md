# Methods: AI Literacy Curriculum Development and Evaluation

## Overview

This study describes the development, deployment, and evaluation of a 7-week AI and digital literacy curriculum for adolescents aged 12-16 years. We employed a multi-method approach combining: (1) systematic curriculum development grounded in learning science principles, (2) quantitative curriculum analysis to identify pedagogical features, and (3) mixed-methods survey analysis to evaluate implementation and learning outcomes.

---

## 1. Curriculum Development Methods

### 1.1 Development Framework

We followed a six-phase curriculum development framework informed by backward design principles (Wiggins & McTighe, 2005) and the CIPP evaluation model (Stufflebeam, 2000):

**Phase 1: Needs Assessment and Constraints Identification**
- Reviewed German national curriculum standards for Natural Sciences and Technology (NIT) and Ethics
- Consulted with participating teachers to identify:
  - Students' prior knowledge (baseline: "consider students know nothing about AI")
  - Existing teaching materials and technical infrastructure
  - Scheduling constraints (7 weeks, 140 minutes/week)
  - School-specific requirements (programming in C++, microcontrollers, woodworking integration)

**Phase 2: Framework Alignment**
We aligned our curriculum development to three major frameworks:
- **OECD AI Literacy Framework** (2025): Targeted the "engaging with AI" level, focusing on recognizing AI presence, evaluating output accuracy, and understanding technical foundations
- **PISA 2029 MAIL** (Media and AI Literacy): Mapped learning objectives to five competence areas (Reflect and Act Ethically, Access and Use, Analyse and Evaluate, Participate and Collaborate, Create)
- **UNESCO AI Competency Framework for Students** (2024): Addressed four dimensions (human-centered mindset, ethics, techniques and applications, system design) at the "Understand" and "Apply" progression levels

**Phase 3: Existing Curriculum Review**
We conducted a pragmatic (non-systematic) review of existing AI literacy curricula through:
- Personal recommendations from AI literacy experts (e.g., KI-Aufträge by University of Berlin, AI Adapt by Gillian Barber, Common Sense Media)
- Targeted query on Elicit research platform: "What are existing open source and free AI literacy curriculums for primary, secondary and high schools? Which countries, language and age group they cover? What knowledge, competences, skills? How many cover Ethical AI and risks & benefits of AI?"
- Targeted internet search for major curricula (ENARIS by EPFL, Toddle 101 Course, code.org, Duke University, Georgia's AI4GA, AI pedagogy by Harvard, AI4K12)

**Inclusion criteria**:
- Target age: 12-16 years
- Open-source and freely available
- Available in English or German
- Covers AI/LLM content (not just general digital literacy)

**Identified curricula** (n=15): See Table 1 for complete list with detailed comparison

**The reuse challenge**: No single existing curriculum met all requirements simultaneously:
- Up-to-date LLM coverage (post-ChatGPT era)
- Age-appropriate for 13-14 year olds
- Alignment with our learning objectives
- Time constraint (7 weeks × 140 min)
- Pedagogical coherence and flow

Therefore, we adopted a **recombination strategy**: selecting and adapting components from multiple curricula while creating new materials where gaps existed.

**Primary sources**:
- **MIT DAILy curriculum**: AI basics, classification vs generation, machine learning types
- **MIT "The Brain Behind the Bot"**: Best explanation of LLM architecture and training (3 stages: unsupervised, supervised, reinforcement learning)
- **Code.org**: Bias activities and examples
- **Toddle 101 Course**: Uses of AI with appropriate detail level

**Original contributions** (not found in existing curricula):
- Integration of social robots as embodiment of AI
- LLM deception and safeguards
- AI sustainability (environmental impact, resource demands)
- Connection between physical robots and LLMs

**Phase 4: Pedagogical Design Based on Learning Science**

We applied evidence-based principles from cognitive science to optimize learning:

1. **Cognitive Load Theory** (Sweller, 1988):
   - Limited content per lesson (max 3-4 main concepts)
   - Worked examples before practice
   - Scaffolded complexity (concrete → abstract)
   - Visual aids and multimodal presentation

2. **Spaced Practice and Retrieval**:
   - Concepts revisited across multiple weeks
   - Weekly recall activities (5-10 min at lesson start)
   - Cumulative assessments (T1, T4, T7)

3. **Formative Assessment** (Black & Wiliam, 1998):
   - Weekly reflection forms for students
   - Teacher feedback per lesson
   - Mid-curriculum assessment (T4) to adjust pacing

4. **Bloom's Taxonomy** (Anderson & Krathwohl, 2001):
   - Balanced cognitive levels:
     - Lower-order: Remember (AI definitions), Understand (how LLMs work)
     - Higher-order: Apply (prompt engineering), Analyze (identify biases), Evaluate (when to use/not use AI), Create (programming choreography)

5. **Hands-on, Active Learning**:
   - Physical robot construction (kinesthetic learning)
   - Interactive activities (TeachableMachine, programming)
   - Collaborative group work (teams of 3-4)

**Phase 5: Iterative Refinement with Teachers**

We conducted three consultation sessions with participating teachers:
- **Session 1** (before deployment): Reviewed draft curriculum, adjusted technical content (added Arduino, C++ programming based on teachers' existing materials)
- **Session 2** (week 3): Mid-implementation check-in, adjusted pacing (topics taking 2-3x longer than planned)
- **Session 3** (post-deployment): Reflection on challenges and improvements for future iterations

**Phase 6: Materials Development**

Final curriculum materials included:
- PowerPoint slides with presenter notes (German and English versions)
- Activity worksheets and handouts
- Assessment instruments (pre-, mid-, post-test surveys)
- Teacher guides with timing, learning objectives, and troubleshooting tips

### 1.2 Final Curriculum Structure

**Total duration**: 7 weeks, ~16.5 hours instructional time

**Curriculum topics by week**:

| Week | Topic | Content | Duration |
|------|-------|---------|----------|
| 1 | Introduction to Social Robots | Definition of social robots, introduction to Marty robot, pre-test survey | 2h 05min |
| 2 | What is AI and Machine Learning | Unsupervised, supervised, reinforcement learning; classification vs generation | 2h 15min |
| 3 | Large Language Models | How LLMs work (3-stage training), existing LLMs, prompting | 2h 15min |
| 4 | Limitations of AI | Biases, hallucinations, when not to use AI, mid-test survey | 2h 15min |
| 5 | Programming and Sensors | Blockly programming, sensor types, Marty's sensors, choreography activity | 2h 10min |
| 6 | Microcontrollers and Ethics | Arduino introduction, C++ programming, environmental impact, LLM safeguards | 2h 20min |
| 7 | LLM Interaction Design | Comparing scaffolded vs unscaffolded LLM interactions, post-test survey | 2h 15min |

**Learning objectives**: See Supplementary Table S1 for complete mapping to PISA MAIL, UNESCO framework, and Bloom's taxonomy

---

## 2. Curriculum Analysis Methods

To systematically analyze curriculum features that may influence learning outcomes, we coded both our developed curriculum and the 15 reviewed existing curricula along multiple dimensions.

### 2.1 Coding Framework

We developed a coding scheme informed by curriculum evaluation frameworks (see curriculum_evaluation_frameworks__validation_required.md) to capture:

#### A. Content Features
1. **Topic coverage**:
   - AI basics (definition, history, types)
   - Machine learning (supervised, unsupervised, reinforcement)
   - Large Language Models (architecture, training, capabilities)
   - Limitations (biases, hallucinations, accuracy)
   - Ethics (fairness, privacy, accountability)
   - Sustainability (environmental impact, resource use)
   - Practical use (when to use/not use, prompt engineering)

2. **Concept repetition**:
   - Count: Number of times each concept appears across curriculum
   - Spacing: Number of weeks between repetitions
   - Modality: How concept is presented (lecture, activity, discussion, assessment)

3. **Concreteness level** (coding 1-5 scale):
   - 1 = Abstract/theoretical (e.g., "AI is mathematical optimization")
   - 2 = Conceptual with examples (e.g., "AI learns patterns from data, like spam filters")
   - 3 = Hands-on demonstration (e.g., training TeachableMachine model)
   - 4 = Interactive application (e.g., programming robot with sensors)
   - 5 = Physical embodiment (e.g., building robot hardware)

4. **Assessment alignment**:
   - Binary coding: Is each learning objective assessed? (yes/no)
   - Assessment type: Multiple choice, open-ended, performance task, observation

#### B. Pedagogical Features

5. **Instructional strategies** (% of lesson time):
   - Direct instruction (lecture, demonstration)
   - Guided practice (scaffolded activities)
   - Independent practice (student-led exploration)
   - Discussion and reflection
   - Formative assessment

6. **Scaffolding mechanisms**:
   - Advance organizers (overview at start)
   - Worked examples provided
   - Gradual release of responsibility
   - Differentiation options (for different skill levels)

7. **Learning science principles applied**:
   - Cognitive load management (yes/no, description)
   - Spaced practice (number of review sessions)
   - Retrieval practice (number of recall activities)
   - Formative feedback (frequency)
   - Active learning (% hands-on time)

#### C. Implementation Features

8. **Required resources**:
   - Technology needs (hardware, software, internet)
   - Teacher expertise level (1=minimal, 5=expert)
   - Preparation time (hours for teacher to prepare)

9. **Flexibility**:
   - Modular (can lessons be reordered?) (yes/no)
   - Time adaptable (can duration be modified?) (yes/no)
   - Context adaptable (can content be customized?) (yes/no)

10. **Teacher support**:
    - Presenter notes/guides (yes/no)
    - Training materials (yes/no)
    - Troubleshooting resources (yes/no)

### 2.2 Coding Procedure

**Coders**: Two researchers independently coded all curricula

**Process**:
1. Training session: Coders practiced on sample curriculum (MIT DAILy) to calibrate coding scheme
2. Independent coding: Each coder analyzed all 16 curricula (15 existing + 1 ours)
3. Reliability check: Inter-rater reliability calculated using Cohen's Kappa for categorical variables and intraclass correlation (ICC) for continuous variables
4. Consensus meeting: Discrepancies discussed and resolved

**Target reliability**: κ > 0.70 for categorical codes, ICC > 0.75 for continuous codes

### 2.3 Analysis Plan

**Descriptive analysis**:
- Summary statistics for each coded feature
- Comparison of our curriculum vs existing curricula (mean, SD, range)
- Visualization: Heatmap of topic coverage across curricula

**Exploratory predictive analysis** (hypothesis-generating only):
- Research question: Do curriculum features predict learning gains?
- DV: Student learning gains (T7 - T1 scores on objective knowledge items)
- IVs: Concept repetition, concreteness, alignment with assessment
- Method: Multiple regression with cross-validation
- **Important**: Given limited sample (N=61) and noisy learning data, these analyses are exploratory. Results will be interpreted as hypothesis-generating for future research, not confirmatory.

---

## 3. Survey Analysis Methods

### 3.1 Study Design and Participants

**Design**: Longitudinal, between-subjects, active control design

**Participants**:
- N = 61 students (15 female, 42 male, 4 other/NA)
- Age: 12-16 years (M = 13.40, SD = 0.75)
- School: Rural German comprehensive school (Gesamtschule)
- Conditions:
  - Build group (n = 31): Assembled Marty robots in Weeks 1-4
  - Control group (n = 30): Interacted with pre-assembled Marty robots in Weeks 1-4
  - Both groups: Identical curriculum in Weeks 5-7

**Timepoints**:
- T1: Pre-test (Week 1, before intervention)
- T4: Mid-test (Week 4, after robot assembly/interaction phase)
- T7: Post-test (Week 7, end of curriculum)
- T8: Follow-up (planned but not yet analyzed)

### 3.2 Measures

#### 3.2.1 Objective AI Literacy (Custom Items)

**Purpose**: Assess knowledge of curriculum-specific content

**Development process**:
1. Generated item pool (n=40) covering all learning objectives
2. Expert review (n=3 AI literacy researchers) for content validity
3. Cognitive interviews with age-matched students (n=5) for clarity
4. Pilot test (n=20 students not in study sample) for difficulty and discrimination
5. Final selection (n=15 items) based on:
   - Content coverage (all topics represented)
   - Difficulty range (easy, medium, hard)
   - Item-total correlation (r > .20)

**Item format**:
- Multiple choice (4 options, 1 correct)
- Sample easy item: "What does AI stand for? a) Artificial Intelligence, b) Automated Internet, c) Advanced Information, d) Applied Innovation"
- Sample hard item: "Which of the following is an example of reinforcement learning? a) Training a spam filter with labeled emails, b) Clustering customers by purchase behavior, c) Teaching a robot to walk by rewarding successful steps, d) Compressing images to smaller files"

**Topics covered** (n items):
- AI basics (3): Definition, types, history
- Machine learning (4): Supervised, unsupervised, reinforcement learning, classification vs generation
- LLMs (3): Architecture, training process, how they generate text
- Limitations (3): Biases, hallucinations, accuracy issues
- Ethics & appropriate use (2): When to use/not use AI, safeguards

**Scoring**: Total score = sum of correct responses (range 0-15)

**Reliability**: Cronbach's α = [to be calculated]

#### 3.2.2 PISA 2029 MAIL Items (Subjective AI Literacy)

**Purpose**: Assess self-reported AI literacy competencies aligned with international framework

**Source**: Draft items from PISA 2029 Media and AI Literacy (MAIL) Assessment Framework (OECD, 2026)

**Competence areas assessed** (items per area):
1. Reflect and Act Ethically and Responsibly (3 items)
   - Example: "I can explain ethical concerns about AI (like fairness and privacy)"
2. Access and Use (2 items)
   - Example: "I can use AI tools effectively for learning tasks"
3. Analyse and Evaluate (3 items)
   - Example: "I can identify when AI might give wrong or biased information"
4. Participate and Collaborate (2 items)
   - Example: "I can discuss AI's impact on society with others"
5. Create (2 items)
   - Example: "I can create content using AI tools responsibly"

**Response scale**: 4-point Likert (1 = Not at all true, 2 = A little true, 3 = Mostly true, 4 = Very true)

**Scoring**:
- Subscale scores: Mean of items in each competence area (range 1-4)
- Total score: Mean of all 12 items (range 1-4)

**Reliability**: To be calculated per subscale and total score

#### 3.2.3 Engagement and Difficulty (Weekly Surveys)

**Purpose**: Monitor weekly engagement and perceived difficulty to assess curriculum feasibility

**Administered**: End of each weekly session (Weeks 1-7)

**Student survey items** (5 questions, <2 min):
1. "How interested were you in today's lesson?" (1-7 scale: Not at all - Very much)
2. "How difficult was today's content?" (1-7 scale: Very easy - Very difficult)
3. "How much did you learn today?" (1-7 scale: Nothing - A lot)
4. "Did you enjoy today's activities?" (yes/no/somewhat)
5. Open-ended: "What was the best/worst part of today?"

**Teacher survey items** (8 questions, ~5 min):
1. "How engaged were students today?" (1-7 scale)
2. "How difficult was the content for students?" (1-7 scale)
3. "How well did students understand the material?" (1-7 scale)
4. "How much of the planned content did you cover?" (0-100%)
5. "What technical issues occurred?" (open-ended)
6. "What worked well today?" (open-ended)
7. "What would you change for next time?" (open-ended)
8. "Additional comments" (open-ended)

### 3.3 Data Analysis Plan

#### 3.3.1 Sample Descriptives and Data Quality

**Preliminary checks**:
1. **Completion rates**: N and % completing each timepoint (T1, T4, T7)
2. **Attrition analysis**: Compare completers vs non-completers on demographics and T1 scores (independent t-tests)
3. **Attention checks**: Identify and flag participants failing attention check items
4. **Outlier detection**: Identify extreme scores (±3 SD from mean) for review
5. **Missingness patterns**: Analyze missing data (MCAR, MAR, MNAR) using Little's test

**Descriptive statistics**:
- Demographics: N, %, M (SD) for age, gender, condition
- Survey completion time (seconds): Median, IQR, range
- Score distributions: M, SD, min, max, skewness, kurtosis for all outcome measures at each timepoint

#### 3.3.2 Learning Outcomes Analysis

**Primary analysis: Pre-post changes**

*Research question*: Did students' AI literacy improve from T1 (pre) to T7 (post)?

**Analysis strategy**:
- **Objective knowledge**: Paired t-test or Wilcoxon signed-rank test (if non-normal)
  - DV: T7 score - T1 score (difference score)
  - Effect size: Cohen's d with 95% CI
  - Item-level analysis: McNemar test for each item (% correct at T1 vs T7)

- **MAIL subscales**: Repeated-measures ANOVA or mixed-effects model
  - DV: MAIL subscale scores
  - IV: Time (T1, T4, T7)
  - Random effect: Participant
  - Post-hoc: Pairwise comparisons with Bonferroni correction

**Secondary analysis: Trajectories over time**

*Research question*: How did learning progress across the 7 weeks?

**Method**: Growth curve modeling (multilevel model)
- Level 1 (within-person): Time (0, 3, 6 weeks coded as T1, T4, T7)
- Level 2 (between-person): Condition (Build vs Control), baseline knowledge
- Model: Linear and quadratic time effects
- Outcome: Objective knowledge score

**Model specification**:
```
Level 1: Knowledge_ti = β0i + β1i(Time_ti) + β2i(Time²_ti) + ε_ti
Level 2: β0i = γ00 + γ01(Condition_i) + γ02(Baseline_i) + u0i
         β1i = γ10 + γ11(Condition_i) + u1i
         β2i = γ20 + γ21(Condition_i) + u2i
```

**Interpretation**: γ10 = average rate of change; γ11 = difference in rate between conditions

#### 3.3.3 Engagement and Feasibility Analysis

**Weekly engagement trends**:
- Calculate weekly means and SDs for student and teacher engagement ratings
- Visualize: Line graph with 95% confidence bands
- Test for decline over time: Linear mixed-effects model with week as continuous predictor

**Difficulty perceptions**:
- Correlation: Student-rated difficulty vs teacher-rated difficulty (Spearman's ρ)
- Identify "trouble spots": Weeks where difficulty ratings > 5/7 and engagement < 3/7
- Compare student vs teacher perceptions: Paired t-tests per week

**Qualitative analysis** (open-ended responses):
1. **Thematic coding**:
   - Inductive approach: Two coders independently read all open-ended responses
   - Generate codebook: Identify recurring themes (challenges, successes, suggestions)
   - Inter-rater reliability: Cohen's κ for theme presence
   - Resolve disagreements through discussion
2. **Frequency counts**: Tally number of responses mentioning each theme
3. **Representative quotes**: Select 2-3 quotes exemplifying each major theme

**Curriculum fidelity**:
- Calculate % of planned content covered per week (from teacher reports)
- Identify deviations: Weeks where <80% content covered
- Summarize technical issues: Frequency and type of problems reported

#### 3.3.4 Exploratory Analysis: What Predicts Learning?

*Research question*: What factors are associated with greater learning gains?

**Predictors** (exploratory):
- Baseline knowledge (T1 objective score)
- Engagement (mean weekly rating)
- Condition (Build vs Control)
- Curriculum features (from curriculum analysis): Repetition, concreteness of concepts learned

**Method**: Multiple linear regression
- DV: Learning gain (T7 - T1 objective knowledge score)
- IVs: Entered in blocks
  - Block 1: Baseline knowledge (control)
  - Block 2: Engagement, Condition
  - Block 3: Curriculum features (concept repetition, concreteness)
- Model fit: R², adjusted R², F-test
- Assumptions: Check multicollinearity (VIF < 5), homoscedasticity, normality of residuals

**Caution**: Given small sample (N=61) and high within-person variability in responses, these analyses are **exploratory and hypothesis-generating only**. Results will be interpreted cautiously with appropriate caveats about limited power and generalizability.

#### 3.3.5 Handling Messy Data

**The reality**: Preliminary data inspection revealed high variability in responses, including:
- Inconsistent responses within-person across timepoints
- Some students showing "learning declines" (T7 < T1)
- High item-level variability (some items show improvement, others decline)

**Analysis strategy for noisy data**:
1. **Transparency**: Report all data issues openly (completion rates, inconsistencies, outliers)
2. **Descriptive focus**: Emphasize descriptive statistics (means, distributions) over p-values
3. **Effect sizes**: Report effect sizes with confidence intervals; acknowledge when CIs are wide
4. **Subgroup analysis**: Examine if certain students (e.g., high engagement) show clearer learning patterns
5. **Qualitative integration**: Triangulate with teacher reports of student learning (did teachers perceive learning even if tests didn't capture it?)
6. **Honest interpretation**: Discuss measurement issues as a key finding (assessment instruments may not capture true learning)

**What we will NOT do**:
- ❌ Cherry-pick only significant results
- ❌ Claim "curriculum effectiveness" with weak/inconsistent evidence
- ❌ Hide data quality issues
- ❌ Over-interpret exploratory analyses as confirmatory

**What we WILL do**:
- ✅ Report descriptive statistics transparently
- ✅ Acknowledge measurement limitations as a key lesson learned
- ✅ Emphasize what teachers observed (qualitative data)
- ✅ Discuss implications for AI literacy assessment broadly
- ✅ Propose better measurement approaches for future research

### 3.4 Software and Reproducibility

**Data processing and analysis**: R version 4.3.1
- Data wrangling: tidyverse, dplyr
- Descriptive statistics: psych, skimr
- Visualizations: ggplot2
- Mixed-effects models: lme4, lmerTest
- Effect sizes: effsize, effectsize
- Qualitative coding: RQDA or manual coding in spreadsheet

**Reproducibility**:
- All analysis code available on GitHub: [repository link to be added]
- De-identified data (with IRB approval) on OSF: [link to be added]
- Analysis notebooks (R Markdown) with step-by-step procedures

### 3.5 Ethical Considerations

- IRB approval: ETH Zurich Ethics Committee (25 ETHICS-247)
- Informed consent: Parental consent + student assent (14+)
- Data protection: GDPR-compliant, encrypted storage
- Anonymization: All identifying information removed before sharing
- Right to withdraw: Participants could withdraw at any time without penalty

---

## Summary of Methods

This study employed a rigorous, multi-method approach to curriculum development and evaluation. We systematically developed an AI literacy curriculum grounded in learning science and policy frameworks, coded curriculum features for quantitative analysis, and collected longitudinal survey data to assess learning outcomes and implementation challenges. Importantly, we designed our analysis plan to handle the reality of noisy educational data and emphasize transparent reporting of both successes and failures—an approach that we argue is essential for advancing the field of AI literacy education.

---

## References

[To be added: All references cited in methods section]
