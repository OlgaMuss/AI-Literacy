
# Curriculum Concept Mapping - Analysis Report

Generated: 2026-04-02 14:25

## Summary Statistics

- **Total curriculum concepts**: 57
- **Total survey items**: 17
- **Weeks analyzed**: 7
- **Average concepts per week**: 8.1 (SD=2.3)
- **Total instructional time**: 832 minutes (13.9 hours)

## Concept Repetition

### Most Repeated Concepts (appear in ≥3 weeks):
| Concept_Category   |   N_Weeks_Appearing | Weeks           |   Max_Spacing |
|:-------------------|--------------------:|:----------------|--------------:|
| LLM                |                   5 | [2, 3, 4, 6, 7] |             5 |
| Programming        |                   4 | [3, 4, 5, 6]    |             3 |
| Biases             |                   3 | [2, 3, 4]       |             2 |
| Sensors            |                   3 | [1, 4, 5]       |             4 |

### Least Repeated Concepts (appear in 1 week only):
| Concept_Category   |   N_Weeks_Appearing | Weeks   |   Max_Spacing |
|:-------------------|--------------------:|:--------|--------------:|
| AI definition      |                   1 | [2]     |             0 |
| Ethics             |                   1 | [6]     |             0 |

## Assessment Alignment

### By Week:
|   Week |   N_Concepts |   N_Assessed |   Pct_Assessed |
|-------:|-------------:|-------------:|---------------:|
|      1 |            5 |            5 |       100      |
|      2 |            8 |            6 |        75      |
|      3 |           10 |            1 |        10      |
|      4 |           10 |            6 |        60      |
|      5 |            7 |            4 |        57.1429 |
|      6 |           11 |            5 |        45.4545 |
|      7 |            6 |            0 |         0      |

**Overall**: 27 of 57 concepts (47.4%) have direct assessment items

## Concreteness Analysis

|   Concreteness_Level |   N_Concepts |   N_With_Assessment |   Pct_Assessed |
|---------------------:|-------------:|--------------------:|---------------:|
|                    2 |           42 |                  19 |        45.2381 |
|                    4 |            5 |                   1 |        20      |
|                    5 |           10 |                   7 |        70      |

**Interpretation**:
- Level 5 (Physical embodiment): Building robot, manipulating physical components
- Level 4 (Interactive application): Programming, using tools
- Level 3 (Hands-on demonstration): Activities, games, experiments
- Level 2 (Conceptual): Definitions, explanations, theoretical content

**Average concreteness**: 2.70 (SD=1.21)

## Potential Issues Identified

### Issue 1: Low Assessment Coverage
30 concepts (52.6%) have no direct assessment items.
This may explain why learning gains are difficult to detect—many taught concepts are not measured.

**Examples of unassessed concepts**:
['Machine Learning types (supervised, unsupervised, reinforcement)', 'Classification vs Generation', 'LLM architecture and training', 'How LLMs work (3 stages: unsupervised, supervised, reinforcement)', 'Existing LLMs (ChatGPT, etc.)', 'Prompts and prompt engineering', 'Sustainability of robots (materials, recycling)', 'Environmental impact (plastic, electronics, batteries)', 'Lithium and resource constraints', 'Social equity and AI access']

### Issue 2: Uneven Time Distribution
- Week with most concepts: Week 6 (11 concepts)
- Week with fewest concepts: Week 1 (5 concepts)
- Time per concept ranges from 12.0 to 20.5 minutes

**Implication**: Some concepts may have insufficient time for deep learning (cognitive load concerns).

### Issue 3: Concept Repetition Inconsistency
- High repetition concepts (≥3 weeks): 4 concepts
- Single-exposure concepts (1 week): 2 concepts

**Implication**: Single-exposure concepts may not benefit from spaced practice (learning science principle).

## Recommendations for Analysis

### 1. Exploratory Hypothesis:
Concepts with **higher repetition** and **higher concreteness** should show better learning gains.

### 2. Analysis Strategy:
- Group survey items by concept category
- Calculate learning gains per category (T7 - T1)
- Correlate with: repetition count, concreteness level, time allocated
- **Caveat**: Small N per category, exploratory only

### 3. Alternative Explanation for Noisy Data:
The **misalignment between taught concepts and assessed items** may explain high variability:
- Students learned concepts X, Y, Z
- Survey assessed concepts A, B, Z
- Only Z shows learning gains; A and B appear as "no learning"

## Files Generated

1. `curriculum_concept_to_item_mapping.csv` - Detailed mapping of concepts to items
2. `curriculum_weekly_summary.csv` - Week-by-week coverage summary
3. `concept_repetition_analysis.csv` - Concept repetition across weeks
4. `curriculum_mapping_report.md` - This report

## Next Steps

1. **Visual inspection**: Review mapping CSV to verify accuracy
2. **Manual corrections**: Adjust any miscategorized concepts
3. **Link to learning data**: Merge with T1, T4, T7 scores to analyze learning by concept
4. **Statistical analysis**: Test if repetition/concreteness predict learning gains
