# AI Literacy Curriculums Analysis

This folder contains comprehensive learning points analysis for 13 AI literacy curricula.

## Main Analysis Files

### 1. Learning_Points_Coverage_Matrix__validation_required.csv
**Purpose:** Quick reference showing which curricula cover which learning points

**Format:**
- Rows: 200+ specific learning points grouped into 15 macro categories
- Columns: 13 curricula
- Cells: Coverage status with brief "How Covered" notes

**Use this when:** You need to quickly see if a specific learning point is covered by any curriculum

### 2. Learning_Points_Depth_Analysis__validation_required.csv
**Purpose:** Detailed depth ratings for every curriculum-point combination

**Format:**
- Depth scale: 0 (not covered) → 1 (mentioned) → 2 (explored) → 3 (deep with activities)
- Two columns per curriculum: Depth rating + detailed "How Covered" description
- Same 200+ learning points as coverage matrix

**Depth Scale Definition:**
- **0 (Not covered):** Not mentioned
- **1 (Mentioned):** Brief reference, vocabulary (1-2 sentences)
- **2 (Explored):** Some detail with examples/light activities (multiple paragraphs or short activity)
- **3 (Deep):** Comprehensive with detailed explanation AND substantial activities/exercises/projects

**Use this when:** You need to understand HOW DEEPLY a curriculum covers specific topics

### 3. Learning_Points_Analysis_Summary__validation_required.md
**Purpose:** Executive summary with key findings and recommendations

**Contents:**
- Overview of all 15 macro categories
- Curriculum strengths comparison
- Coverage gaps identification (learning points with <3 curricula at depth ≥2)
- Recommendations for comprehensive curriculum design
- Depth distribution summary
- Usage guide for curriculum designers, researchers, teachers

**Use this when:** You need overview, trends, or recommendations

## Individual Curriculum Analysis Files

Each curriculum has a detailed markdown file with:
- Overview and unique strengths
- All learning points with depth ≥2 organized by category
- Depth 3 points highlighted (deepest coverage)
- Projects and activities list
- Coverage gaps
- Pedagogical approach
- Total counts

### Technical Depth Leaders
1. **ENARIS_EPFL_Learning_Points.md** - 65 depth-3 points (most comprehensive technical)
2. **Georgia_AI4GA_Learning_Points.md** - 35 depth-3 points (most hands-on activities)
3. **MIT_DAILy_Learning_Points.md** - 25 depth-3 points (ethical design focus)

### Specialized Focus
4. **aiEDU_Readiness_Framework_Learning_Points.md** - 30 depth-3 points (Indigenous AI, Human Advantage)
5. **Day_of_AI_Learning_Points.md** - 15 depth-3 points (LLM mechanics, classroom norms)
6. **Berlin_KI-Auftraege_Learning_Points.md** - 8 depth-3 points (advanced prompt engineering)

### Pedagogical Methods
7. **Harvard_AI_Pedagogy_Learning_Points.md** - 8 depth-3 points (Socratic dialogue, journalism literacy)
8. **Toddle_AI_101_Learning_Points.md** - 10 depth-3 points (scaffolding routines, thinking frameworks)

### Foundations & Ethics
9. **MIT_AI_Ethics_Learning_Points.md** - 3 depth-3 points (EU 7 requirements, Teachable Machine)
10. **AI4K12_Learning_Points.md** - 5 depth-3 points (Five Big Ideas, Cognimates)
11. **AI_Adapt_Ireland_Learning_Points.md** - 15 depth-3 points (careers, Ireland context)

### Critical Perspectives
12. **Duke_AI_Ethics_Toolkit_Learning_Points.md** - 5 depth-3 points (critical lens, systemic issues)

### Introductory
13. **Common_Sense_Media_Learning_Points.md** - 0 depth-3 points (entry-level awareness)

## 15 Macro Categories

1. **AI Fundamentals** (7 points) - Definitions, narrow vs general, perception
2. **Algorithms & Data** (14 points) - Recipes, opinions, data quality, features, embeddings
3. **Machine Learning** (9 points) - Supervised learning, classification/regression, decision trees
4. **Neural Networks** (11 points) - Architecture, training, single neurons, Boolean logic
5. **NLP & Language** (23 points) - Speech recognition, LLMs, chatbots, embeddings, translation
6. **Computer Vision** (16 points) - Perception, edge detection, faces, industrial/medical
7. **Generative AI** (12 points) - GANs, image/text generation, style transfer
8. **Deepfakes & Misinformation** (16 points) - Detection, harms/benefits, fact-checking, hallucinations
9. **Ethics & Values** (27 points) - Frameworks, trolley problem, Moral Machine, human-AI interaction
10. **Bias & Fairness** (18 points) - Definitions, examples, mitigation
11. **Limitations & Capabilities** (15 points) - What AI can't do, human advantages, overreliance
12. **Societal Impact** (29 points) - Labor, power, benefits/harms, surveillance, media, government
13. **Environmental Impact** (13 points) - Energy, water, carbon, mitigation
14. **Privacy & Data** (11 points) - Collection, usage guidelines, risks
15. **IP & Copyright** (8 points) - Ownership, fair use, academic integrity

**Plus cross-cutting themes:**
- Hands-on Tools (25 platforms)
- Prompt Engineering (9 techniques)
- System Design (6 concepts)
- Reinforcement Learning (8 concepts)
- Real-world Case Studies (12 detailed)
- Unplugged Activities (6 types)
- Projects & Assessments (11 major)
- Specialized Topics (15 domain-specific)
- Literacy Meta-Skills (8 frameworks)
- Advanced Technical Topics (10 concepts)

## Quick Comparison Table

| Curriculum | Total Depth ≥2 | Depth 3 | Primary Strength | Notable Gap |
|------------|----------------|---------|------------------|-------------|
| ENARIS (EPFL) | ~80 | ~65 | Technical comprehension | Prompt engineering |
| Georgia AI4GA | ~50 | ~35 | Hands-on activities | Environmental impact |
| aiEDU | ~60 | ~30 | Indigenous AI, Snapshots | NN architecture |
| MIT DAILy | ~40 | ~25 | Ethical design | Environmental impact |
| Day of AI | ~30 | ~15 | LLM mechanics clarity | CV, RL, environment |
| AI Adapt (Ireland) | ~40 | ~15 | Careers, Ireland data | Technical depth |
| Toddle | ~30 | ~10 | Scaffolding routines | All technical |
| Berlin | ~20 | ~8 | Advanced prompting | CV, RL, environment |
| Harvard | ~25 | ~8 | Journalism, Socratic | Technical fundamentals |
| MIT AI Ethics | ~15 | ~3 | EU 7 requirements | Most technical |
| AI4K12 | ~25 | ~5 | Cognimates coding | Depth on Big Ideas |
| Duke | ~40 | ~5 | Critical perspective | Constructive skills |
| Common Sense | ~20 | 0 | Accessibility | All depth |

## Recommendations by Use Case

### For Comprehensive Technical Curriculum
**Core:** ENARIS (technical backbone) + Georgia (hands-on) + MIT DAILy (ethical design)  
**Additions:** Berlin (prompting) + aiEDU (frameworks)

### For Ethics & Society Focus
**Core:** MIT DAILy (ethical matrices) + Duke (critical lens) + AI Adapt (EU guidelines)  
**Additions:** aiEDU (Indigenous AI) + Harvard (journalism)

### For Classroom-Ready Lessons
**Core:** Day of AI (6 lessons) + Toddle (8 lessons with scaffolding)  
**Additions:** MIT DAILy (projects) + Georgia (activities)

### For Teacher Professional Development
**Core:** Harvard (pedagogy methods) + aiEDU (framework) + AI4K12 (standards)  
**Additions:** Toddle (routines) + Duke (critical lens)

### For Younger Students (K-8)
**Core:** AI4K12 (K-12 progressions) + Common Sense (accessible intro)  
**Additions:** aiEDU (K-5 to 9-12) + selected Georgia unplugged activities

### For Advanced/Technical Students
**Core:** ENARIS (deepest) + Georgia (ML pipeline) + Berlin (Pandas coding)  
**Additions:** MIT DAILy (GANs) + aiEDU (LLM technical)

## Coverage Gaps Across All Curricula

Learning points with <3 curricula at depth ≥2:
- Narrow vs General AI (only ENARIS depth 3)
- Map of AI taxonomy (only ENARIS depth 3)
- All detailed RL concepts (only ENARIS depth 3)
- Overfitting/underfitting/transfer learning (only Georgia depth 3)
- Single neuron Boolean logic (only Georgia depth 3)
- Sensor physics (only Georgia depth 3)
- Advanced prompt engineering (only Berlin depth 3)
- Indigenous AI (only aiEDU depth 3)
- 18 journalism pitfalls (only Harvard depth 3)
- SAMR AI edition (only Toddle depth 3)
- Tech oligarchy critique (only Duke depth 2)
- Ghost work detailed (only Duke/Harvard depth 3)

## Data Sources
All analysis based on:
- Primary curriculum documents (PDFs, DOCX, HTML)
- Extracted text files (where binary formats needed conversion)
- Official learning objectives documents
- Teacher guides and student worksheets
- Web-based lesson pages

**Total source documents processed:** 100+

**Date Generated:** April 2, 2026

---

## File Naming Convention
- `[Curriculum_Name]_Learning_Points.md` - Individual curriculum analysis
- `__validation_required` suffix on all generated files per workspace rules
