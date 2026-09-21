# Curriculum-Assessment Alignment Report (rebuilt pipeline)

**Data lineage:** concepts from slide decks in `Developped curriculum/`; item inventory parsed from codebook tables with merged cells forward-filled and cross-checked against administered columns in `combined_df-Table 1.csv`; links from human-validatable mapping table; context/pedagogy from deck agendas. No keyword matching used. Organized along the five dimensions: Context, Content, Pedagogy, Didactics, Assessment.


## 1. Context

- Weekly sessions: **7**, total instructional time ~**980 min** (16.3 h)
- Condition split (Build vs Control activity) in weeks: 2, 3, 4
- Measurement waves: T1 (pre, W1), T4 (mid, W4), T7 (post, W7) - identical 23-item knowledge battery at all three waves
- Language of instruction: German (W1 deck in English; W2/W4 Control decks bilingual German/English)

## 2. Content

- Concepts in enacted curriculum: **51** (see `curriculum_concepts__validation_required.csv`)

### 2.1 Concepts per theme

| Theme | Concepts |
|---|---|
| AI | 2 |
| AI ethics | 4 |
| AI limitations | 4 |
| AI safety | 4 |
| AI use | 6 |
| Hardware | 3 |
| LLM | 5 |
| ML | 3 |
| Microcontrollers | 3 |
| Programming | 10 |
| Robots | 2 |
| Sensors | 5 |

### 2.2 Mapping to UNESCO AI competency framework for students (2024)

| UNESCO competency block (level) | Concepts |
|---|---|
| AI techniques and applications > Application skills (L2 Apply) | 12: W4_05, W4_07, W5_01, W5_02, W5_03, W5_04, W5_05, W5_11, W5_12, W5_13, W6_04, W7_02 |
| AI techniques and applications > AI foundations (L1 Understand) | 10: W2_01, W2_02, W2_03, W2_04, W2_05, W2_06, W2_07, W2_08, W2_09, W4_01 |
| Ethics of AI > Embodied ethics (L1 Understand) | 5: W2_10, W4_02, W4_03, W6_05, W6_06 |
| beyond framework: sensors/robotics hardware | 5: W5_06, W5_07, W5_08, W5_09, W5_10 |
| Ethics of AI > Safe and responsible use (L2 Apply) | 4: W4_04, W4_08, W6_10, W7_04 |
| beyond framework: microcontrollers | 3: W6_01, W6_02, W6_03 |
| beyond framework: LLM safeguards | 2: W6_09, W7_03 |
| beyond framework: robotics hardware | 2: W1_03, W3_01 |
| AI system design > Problem scoping (L1 Understand) | 1: W4_06 |
| AI techniques and applications > Creating AI tools (L3 Create) | 1: W5_14 |
| Ethics of AI > Ethics by design (L3 Create) | 1: W6_07 |
| beyond framework: LLM behavior control | 1: W7_01 |
| beyond framework: anthropomorphism/deception resistance | 1: W6_08 |
| beyond framework: robotics operation | 1: W3_02 |
| beyond framework: robotics taxonomy | 1: W1_01 |
| beyond framework: social robotics | 1: W1_02 |

- Concepts entirely **beyond the UNESCO framework**: **17** of 51 (robotics hardware, sensors, microcontrollers, LLM safeguards, anthropomorphism/deception resistance, LLM behavior control)
- Concepts mapped to a UNESCO block but extending beyond it: **3**
- Concepts at **L1 Understand** blocks: 16; at L2 Apply blocks: 16; at L3 Create blocks: 2 (several L2/L3 blocks were taught at reduced depth - see 'taught at ... depth' notes in the concepts table)

### 2.3 Reverse coverage: framework suggestions vs. enacted curriculum

**UNESCO AI CFS competency blocks (12):**

| Block | Covered by concepts |
|---|---|
| Human agency | - not covered |
| Human accountability | - not covered |
| Citizenship in the AI era | - not covered |
| Embodied ethics | 5: W2_10, W4_02, W4_03, W6_05, W6_06 |
| Ethics by design | 1: W6_07 |
| Safe and responsible use | 4: W4_04, W4_08, W6_10, W7_04 |
| AI foundations | 10: W2_01, W2_02, W2_03, W2_04, W2_05, W2_06, W2_07, W2_08, W2_09, W4_01 |
| Application skills | 12: W4_05, W4_07, W5_01, W5_02, W5_03, W5_04, W5_05, W5_11, W5_12, W5_13, W6_04, W7_02 |
| Creating AI tools | 1: W5_14 |
| Problem scoping | 1: W4_06 |
| Architecture design | - not covered |
| Iteration and feedback | - not covered |

- UNESCO blocks with at least one enacted concept: **7/12**

**PISA 2029 MAIL competences (5):**

| Competence | Direct mappings | Indirect mappings |
|---|---|---|
| Reflect and Act Ethically and Responsibly | 6: W2_10, W4_06, W4_08, W6_05, W6_06, W6_10 | 1: W6_07 |
| Access and Use | 5: W2_08, W4_05, W4_07, W5_04, W7_02 | - |
| Analyse and Evaluate | 8: W2_02, W2_03, W2_09, W4_01, W4_02, W4_04, W6_08, W7_04 | 6: W2_01, W2_04, W2_05, W2_06, W2_07, W4_03 |
| Participate and Collaborate | - | - |
| Create | 7: W5_01, W5_03, W5_05, W5_11, W5_14, W6_04, W7_01 | 3: W5_02, W5_12, W5_13 |

- MAIL competences touched: **4/5**; 'Participate and Collaborate' (online discourse, co-creation, conflict de-escalation) has zero coverage - candidate gap for v2

## 3. Pedagogy

| Week | Title | Task types | Configuration | Condition difference |
|---|---|---|---|---|
| 1 | Introduction to social robots | presentation/lecture; small-group research task (robot examples); hands-on building (legs); plenary presentations | groups of 3-4; whole class; individual questionnaire | none identified (single W1 deck) |
| 2 | AI competence (AI and LLMs) | lecture with embedded questions; classify-or-generate card activity (5 min); ML-types worksheet; hands-on Soekia GPT exploration; building (Build) vs robot soccer tournament (Control) | groups of 3-5; individual worksheets; whole class | Build: continue legs/arms; Control: Marty penalty shootout with pre-assembled robots |
| 3 | Large language models (review and re-teach) | structured review of W2; AI-or-not activity with answer key; ML-types activity; LLM lecture; building arms/head (Build) vs obstacle parkour (Control) | groups of 3-5; whole class | Build: arms and head; Control: obstacle parkour |
| 4 | Limits of AI | lecture (bias types; hallucinations; uses; when-not-to-use; prompt engineering; cheat sheet); bias-hunting activity on 3 real LLMs; Marty testing/repair (Build) vs escape game (Control) | groups; individual; whole class | Build: connect/calibrate/test Marty; Control: escape game |
| 5 | Programming with Marty | lecture via cooking metaphor (commands; parameters; loops; libraries); guided Blockly exploration; choreography project (find movements; program 1-min dance; test; present); sensor lecture; sensor dashboard exploration; sensor-triggered choreography challenge | groups; individual programming; plenary presentations | none identified (single W5 deck) |
| 6 | Microcontrollers and AI ethics | lecture (microcontrollers; pins; C++); Arduino hands-on (LED eyes); ethics/sustainability lecture; LLM safety-testing activity with Marty (probing; adding safeguard prompt; model comparison) | groups; whole class | none identified (single W6 deck) |
| 7 | Marty as learning partner | review (microcontrollers; LLM ethics); instruction-writing task; two comparative learning tests (own instructions vs pre-built frame); structured discussions; closing discussion | groups; whole class discussion; individual questionnaire | none identified (single W7 deck) |

## 4. Didactics

### 4.1 Instructional role (mastery expectation) of concepts

| Mastery | Concepts | Share |
|---|---|---|
| core | 0 | 0% |
| working | 0 | 0% |
| exposure | 0 | 0% |

### 4.2 New concepts introduced per week (pacing)

| Week | New concepts |
|---|---|
| 1 | 3 |
| 2 | 10 |
| 3 | 2 |
| 4 | 8 |
| 5 | 14 |
| 6 | 10 |
| 7 | 4 |

### 4.3 Weaving with previous concepts (revisits / spacing)

- **W2_01** introduced W2, revisited W3
- **W2_02** introduced W2, revisited W3
- **W2_03** introduced W2, revisited W3
- **W2_04** introduced W2, revisited W3
- **W2_05** introduced W2, revisited W3
- **W2_06** introduced W2, revisited W3
- **W2_07** introduced W2, revisited W3
- **W2_08** introduced W2, revisited W3
- **W2_09** introduced W2, revisited W3
- **W2_10** introduced W2, revisited W3
- **W6_01** introduced W6, revisited W7
- **W6_03** introduced W6, revisited W7
- **W6_04** introduced W6, revisited W7
- **W6_08** introduced W6, revisited W7
- **W6_09** introduced W6, revisited W7

### 4.4 Misconceptions explicitly addressed

- **W2_02**: rule-based automation is not AI
- **W2_03**: predictions are forecasts of trends; not oracles
- **W2_09**: chatbots do not learn from talking to you; the model does not change
- **W4_01**: AI output is not neutral truth; it reflects its input data
- **W4_04**: LLMs do not 'know' facts; generated text can be fabricated and must be verified
- **W4_08**: AI has no emotions or wishes and cannot attach to you
- **W5_07**: sensors cannot detect emotions or feelings
- **W6_08**: AI cannot have feelings; wishes; or a personal history - apparent personality comes from training data

## 5. Assessment

### 5.1 Item inventory

- Knowledge items administered (all waves T1/T4/T7): **23**
- Codebook items never administered: **8** (LLMmc_1, LLMmc_2, LLMmc_3, LLMmc_4, LLMmc_5, LLMmc_6, LLMmc_7, LLMmc_8)
- Administered but missing from codebook: GA17
- Item format: all 4-option multiple choice, digital, individual

### 5.2 Coverage by instructional role (mastery)

Non-assessment is only problematic for *core* concepts; *exposure* concepts are taught to spark curiosity or prepare later learning and are legitimately unassessed.


**Core concepts NOT assessed (alignment gaps to fix):**


**Core concepts only partially assessed:**


### 5.3 Full coverage table per week

| Week | Concepts | Assessed | Partial | Not assessed |
|---|---|---|---|---|
| 1 | 3 | 1 | 0 | 2 |
| 2 | 10 | 4 | 2 | 4 |
| 3 | 2 | 0 | 0 | 2 |
| 4 | 8 | 3 | 1 | 4 |
| 5 | 14 | 6 | 1 | 7 |
| 6 | 10 | 3 | 2 | 5 |
| 7 | 4 | 0 | 0 | 4 |

### 5.4 Orphan items (assessed but not taught)

- None: every administered item links to >=1 taught concept.

Unresolved (item text not recoverable): GA17

### 5.5 Timing: intended (codebook) vs enacted week

| Item | Intended week (codebook) | Enacted week (taught) | Delta |
|---|---|---|---|
| microcontrollers_1 | 4 | 6 | +2 |
| microcontrollers_2 | 4 | 6 | +2 |
| GA10 | 2 | 4 | +2 |
| LLMdesign_1 | 2 | 4 | +2 |
| EA05 | 3 | 4 | +1 |
| GA04 | 3 | 4 | +1 |
| PR1 | 4 | 5 | +1 |
| PR2 | 4 | 5 | +1 |
| PR3 | 4 | 5 | +1 |
| PR4 | 4 | 5 | +1 |

### 5.6 Coverage matrix per item

| Item | Concept | Link | Intended W | Enacted W |
|---|---|---|---|---|
| CA12 | W2_02 | primary | 2 | 2 |
| CI29 | W2_04 | primary | 2 | 2 |
| CI31 | W2_05 | primary | 2 | 2 |
| DA09 | W2_01 | primary | 2 | 2 |
| DA09 | W2_02 | partial | 2 | 2 |
| EA05 | W4_03 | partial | 3 | 4 |
| EA05 | W4_02 | primary | 3 | 4 |
| EA11 | W6_05 | primary | 6 | 6 |
| GA04 | W4_04 | primary | 3 | 4 |
| GA10 | W2_09 | partial | 2 | 2 |
| GA10 | W4_07 | primary | 2 | 4 |
| GA13 | W2_04 | primary | 2 | 2 |
| GA13 | W2_07 | partial | 2 | 2 |
| GA16 | W6_06 | partial | 6 | 6 |
| GA17 | W6_06 | unknown |  | 6 |
| LLMdesign_1 | W4_07 | primary | 2 | 4 |
| PR1 | W5_01 | primary | 4 | 5 |
| PR2 | W5_03 | primary | 4 | 5 |
| PR3 | W5_11 | primary | 4 | 5 |
| PR4 | W6_04 | partial | 4 | 6 |
| PR4 | W5_05 | primary | 4 | 5 |
| UA19 | W2_05 | primary | 2 | 2 |
| microcontrollers_1 | W6_02 | primary | 4 | 6 |
| microcontrollers_2 | W6_01 | primary | 4 | 6 |
| robotparts_1 | W1_03 | primary | 1 | 1 |
| robotparts_2 | W1_03 | primary | 1 | 1 |
| sensors_1 | W5_10 | partial | 5 | 5 |
| sensors_1 | W5_09 | primary | 5 | 5 |
| sensors_2 | W5_06 | primary | 5 | 5 |
| sensors_2 | W5_09 | partial | 5 | 5 |