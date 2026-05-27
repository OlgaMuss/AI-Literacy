"""
Curriculum Concept to Learning Measure Mapping Script

This script creates a systematic mapping between:
1. Concepts taught in each week of the curriculum
2. Objective learning items in the survey
3. Curriculum features (repetition, concreteness, assessment alignment)

Author: Curriculum Analysis
Date: April 2026
"""

import pandas as pd
import numpy as np
from pathlib import Path
import re

# Set up paths
DATA_DIR = Path("/Users/olga/Olga's workspace/Publications/AI and DL curriculum paper/Data_analysis/Data")
CODEBOOK_DIR = DATA_DIR / "Buildbots_Codebook_15122025-2"
OUTPUT_DIR = Path("/Users/olga/Olga's workspace/Publications/AI and DL curriculum paper/Data_analysis")

print("="*80)
print("CURRICULUM CONCEPT MAPPING - VALIDATION & CREATION")
print("="*80)

# ============================================================================
# STEP 1: Load Learning Objectives Codebook
# ============================================================================
print("\n[STEP 1] Loading Learning Objectives Codebook...")

learning_obj_path = CODEBOOK_DIR / "Learning objectives-Table 1.csv"
print(f"Reading: {learning_obj_path}")

df_learning = pd.read_csv(learning_obj_path, sep=';')
print(f"✓ Loaded {len(df_learning)} learning objective items")
print(f"✓ Columns: {list(df_learning.columns)}")

# Check for missing data
print("\n[VALIDATION] Missing data check:")
for col in df_learning.columns:
    n_missing = df_learning[col].isna().sum()
    pct_missing = (n_missing / len(df_learning)) * 100
    if n_missing > 0:
        print(f"  - {col}: {n_missing} missing ({pct_missing:.1f}%)")

# ============================================================================
# STEP 2: Extract Week-Concept Mapping from Codebook
# ============================================================================
print("\n[STEP 2] Extracting week-concept mapping from codebook...")

# Clean week column (handle various formats)
df_learning['Week_Clean'] = df_learning['Week'].fillna('').astype(str)
df_learning['Week_Number'] = df_learning['Week_Clean'].str.extract(r'(\d+)').astype(float)

# Summary by week
week_summary = df_learning.groupby('Week_Clean').agg({
    'Learning topics': 'count',
    'Learning objective': lambda x: ', '.join(x.dropna().unique()[:3])  # First 3 unique objectives
}).reset_index()
week_summary.columns = ['Week', 'N_Items', 'Sample_Objectives']

print("\n✓ Items per week:")
print(week_summary.to_string(index=False))

# ============================================================================
# STEP 3: Define Curriculum Concepts Per Week (from curriculum materials)
# ============================================================================
print("\n[STEP 3] Defining curriculum concepts covered per week...")

# Based on "Curriculum for Marty project.pdf" and teaching materials
curriculum_concepts = {
    'Week 1': {
        'concepts': [
            'Social robots definition',
            'Types of robots (social vs industrial vs virtual agents)',
            'Marty robot introduction',
            'Robot components (motors, sensors, computer)',
            'Robot parts identification'
        ],
        'activities': ['Robot classification cards', 'Marty assembly (legs)', 'Pre-test survey'],
        'assessment_time': 60,  # minutes
        'instructional_time': 60  # minutes (excluding assessment)
    },
    'Week 2': {
        'concepts': [
            'What is AI (definition, characteristics)',
            'AI vs non-AI applications',
            'Machine Learning types (supervised, unsupervised, reinforcement)',
            'Classification vs Generation',
            'LLM introduction',
            'LLM limitations (hallucinations, biases)',
            'LLM uses (brainstorming, summarizing, tutoring)',
            'Prompt engineering basics'
        ],
        'activities': ['TeachableMachine activity', 'Building session', 'AI concept practice tasks'],
        'assessment_time': 5,
        'instructional_time': 130
    },
    'Week 3': {
        'concepts': [
            'LLM architecture and training',
            'How LLMs work (3 stages: unsupervised, supervised, reinforcement)',
            'Existing LLMs (ChatGPT, etc.)',
            'Prompts and prompt engineering',
            'Sustainability of robots (materials, recycling)',
            'Environmental impact (plastic, electronics, batteries)',
            'Lithium and resource constraints',
            'Social equity and AI access',
            'Cultural bias in AI',
            'Feedback loops and tipping points'
        ],
        'activities': ['LLM review', 'Sustainability game', 'Assembly continuation'],
        'assessment_time': 5,
        'instructional_time': 130
    },
    'Week 4': {
        'concepts': [
            'Biases in AI (gender, racial, algorithmic)',
            'Hallucinations in LLMs',
            'When NOT to use AI',
            'Strategies for appropriate AI use',
            'Programming basics (commands, variables, functions, parameters)',
            'Loops and conditionals (if-else)',
            'Libraries',
            'Marty architecture (motors, sensors)',
            'Sensors (infrared, color)',
            'Motor function'
        ],
        'activities': ['Bias case studies', 'Programming Marty emotions', 'Choreography creation', 'Mid-test survey'],
        'assessment_time': 11,
        'instructional_time': 124
    },
    'Week 5': {
        'concepts': [
            'Blockly programming',
            'Sensor types (general)',
            'Marty sensors (infrared, color)',
            'How sensors work',
            'Sensor input in programming',
            'Dance choreography programming',
            'Sensor-triggered actions'
        ],
        'activities': ['Program dance choreography', 'Explore sensor board', 'Trigger choreography with obstacle sensor'],
        'assessment_time': 5,
        'instructional_time': 130
    },
    'Week 6': {
        'concepts': [
            'Microcontrollers (definition, function)',
            'Arduino Nano introduction',
            'C++ programming',
            'AI ethics (transparency, privacy, alignment)',
            'Mental health impacts of AI',
            'Over-reliance on AI',
            'Manipulation and persuasion by AI',
            'Misinformation and content accuracy',
            'Sustainability impacts (energy, water)',
            'Equity and accessibility',
            'LLM safeguards'
        ],
        'activities': ['Arduino programming', 'LLM voice interaction testing', 'Safeguard exploration'],
        'assessment_time': 5,
        'instructional_time': 135
    },
    'Week 7': {
        'concepts': [
            'Microcontroller review',
            'LLM safeguards review',
            'Scaffolded vs unscaffolded LLM interactions',
            'LLM interaction design',
            'Educational applications of LLMs',
            'Responsible AI use synthesis'
        ],
        'activities': ['Mnemonic creation with LLM (2 rounds)', 'Compare scaffolded/unscaffolded', 'Post-test survey'],
        'assessment_time': 12,
        'instructional_time': 123
    }
}

print("\n✓ Curriculum structure defined for 7 weeks")
for week, data in curriculum_concepts.items():
    print(f"  {week}: {len(data['concepts'])} concepts, {len(data['activities'])} activities")

# ============================================================================
# STEP 4: Map Concepts to Survey Items
# ============================================================================
print("\n[STEP 4] Mapping curriculum concepts to survey items...")

# Create mapping dataframe
mapping_rows = []

for idx, row in df_learning.iterrows():
    learning_topic = row['Learning topics']
    learning_obj = row['Learning objective']
    week = row['Week_Clean']
    item_english = row['English']
    item_difficulty = row['Item difficulty']
    category = row['Category']
    
    # Skip empty rows
    if pd.isna(learning_topic) and pd.isna(learning_obj):
        continue
    
    # Extract week number
    week_num_match = re.search(r'Week (\d+)', week) if isinstance(week, str) else None
    week_num = int(week_num_match.group(1)) if week_num_match else None
    week_key = f'Week {week_num}' if week_num else None
    
    # Get concepts for this week
    if week_key and week_key in curriculum_concepts:
        concepts_this_week = curriculum_concepts[week_key]['concepts']
        activities_this_week = curriculum_concepts[week_key]['activities']
        n_concepts = len(concepts_this_week)
        n_activities = len(activities_this_week)
    else:
        concepts_this_week = []
        activities_this_week = []
        n_concepts = 0
        n_activities = 0
    
    # Determine concreteness level (1-5)
    # Based on learning objective and item content
    concreteness = None
    if pd.notna(learning_obj):
        obj_lower = str(learning_obj).lower()
        if any(x in obj_lower for x in ['part', 'component', 'motor', 'sensor', 'robot']):
            concreteness = 5  # Physical embodiment
        elif any(x in obj_lower for x in ['program', 'code', 'command', 'loop']):
            concreteness = 4  # Interactive application
        elif any(x in obj_lower for x in ['activity', 'example', 'case']):
            concreteness = 3  # Hands-on demonstration
        elif any(x in obj_lower for x in ['definition', 'explain', 'describe']):
            concreteness = 2  # Conceptual with examples
        else:
            concreteness = 2  # Default: conceptual
    
    # Count concept repetition (how many times this concept appears across weeks)
    # We'll calculate this later after all concepts are extracted
    
    mapping_row = {
        'Week': week,
        'Week_Number': week_num,
        'Learning_Topic': learning_topic,
        'Learning_Objective': learning_obj,
        'Survey_Item_English': item_english[:100] + '...' if pd.notna(item_english) and len(str(item_english)) > 100 else item_english,
        'Item_Difficulty': item_difficulty,
        'Category': category,
        'N_Concepts_This_Week': n_concepts,
        'N_Activities_This_Week': n_activities,
        'Concreteness_Level': concreteness,
        'Concepts_Covered': '; '.join(concepts_this_week) if concepts_this_week else '',
        'Activities': '; '.join(activities_this_week) if activities_this_week else ''
    }
    
    mapping_rows.append(mapping_row)

df_mapping = pd.DataFrame(mapping_rows)
print(f"✓ Created mapping with {len(df_mapping)} survey items")

# ============================================================================
# STEP 5: Analyze Concept Repetition
# ============================================================================
print("\n[STEP 5] Analyzing concept repetition across weeks...")

# Create a concept database with normalized names
all_concepts = []
for week_key, week_data in curriculum_concepts.items():
    week_num = int(week_key.split()[1])
    for concept in week_data['concepts']:
        all_concepts.append({
            'week': week_num,
            'concept': concept,
            'concept_normalized': concept.lower().strip()
        })

df_concepts = pd.DataFrame(all_concepts)

# Count repetitions of key concepts
concept_keywords = {
    'AI definition': ['what is ai', 'ai definition', 'characteristics of ai'],
    'Machine Learning': ['machine learning', 'supervised', 'unsupervised', 'reinforcement'],
    'LLM': ['llm', 'large language model', 'language model'],
    'Hallucinations': ['hallucination'],
    'Biases': ['bias', 'biases'],
    'Ethics': ['ethics', 'ethical', 'responsibility'],
    'Sustainability': ['sustainability', 'environmental', 'resource'],
    'Programming': ['programming', 'code', 'command', 'loop', 'variable', 'function'],
    'Sensors': ['sensor'],
    'Motors': ['motor'],
    'Microcontroller': ['microcontroller', 'arduino'],
    'Prompting': ['prompt'],
    'Safeguards': ['safeguard']
}

# Count how many weeks each concept appears
concept_repetition = {}
for concept_name, keywords in concept_keywords.items():
    weeks_appearing = set()
    for idx, row in df_concepts.iterrows():
        if any(kw in row['concept_normalized'] for kw in keywords):
            weeks_appearing.add(row['week'])
    concept_repetition[concept_name] = {
        'n_weeks': len(weeks_appearing),
        'weeks': sorted(list(weeks_appearing)),
        'spacing': max(weeks_appearing) - min(weeks_appearing) if weeks_appearing else 0
    }

print("\n✓ Concept repetition analysis:")
for concept, stats in sorted(concept_repetition.items(), key=lambda x: x[1]['n_weeks'], reverse=True):
    if stats['n_weeks'] > 0:
        print(f"  {concept}: {stats['n_weeks']} weeks (weeks {stats['weeks']}, spacing: {stats['spacing']} weeks)")

# ============================================================================
# STEP 6: Add Repetition Data to Mapping
# ============================================================================
print("\n[STEP 6] Adding concept repetition to mapping...")

def find_concept_category(learning_obj, learning_topic):
    """Categorize learning objective into concept category"""
    if pd.isna(learning_obj) and pd.isna(learning_topic):
        return None, 0
    
    text = f"{learning_topic} {learning_obj}".lower()
    
    for concept_name, keywords in concept_keywords.items():
        if any(kw in text for kw in keywords):
            return concept_name, concept_repetition[concept_name]['n_weeks']
    
    return 'Other', 0

df_mapping['Concept_Category'] = df_mapping.apply(
    lambda row: find_concept_category(row['Learning_Objective'], row['Learning_Topic'])[0], 
    axis=1
)
df_mapping['Concept_Repetition_N_Weeks'] = df_mapping.apply(
    lambda row: find_concept_category(row['Learning_Objective'], row['Learning_Topic'])[1], 
    axis=1
)

print(f"✓ Categorized {len(df_mapping[df_mapping['Concept_Category'].notna()])} items into concept categories")

# ============================================================================
# STEP 7: Calculate Assessment Alignment
# ============================================================================
print("\n[STEP 7] Calculating assessment alignment...")

# Check if concepts taught in a week are assessed
df_mapping['Taught_In_Week'] = df_mapping['Week_Number'].notna()
df_mapping['Has_Assessment_Item'] = df_mapping['Survey_Item_English'].notna()

alignment_by_week = df_mapping.groupby('Week_Number').agg({
    'Learning_Objective': 'count',
    'Has_Assessment_Item': 'sum'
}).reset_index()
alignment_by_week.columns = ['Week', 'N_Objectives', 'N_Assessed']
alignment_by_week['Pct_Assessed'] = (alignment_by_week['N_Assessed'] / alignment_by_week['N_Objectives']) * 100

print("\n✓ Assessment alignment by week:")
print(alignment_by_week.to_string(index=False))

# ============================================================================
# STEP 8: Validation Checks
# ============================================================================
print("\n[STEP 8] Running validation checks...")

print("\n[CHECK 1] Verify all weeks have content:")
weeks_expected = set(range(1, 8))
weeks_found = set(df_mapping['Week_Number'].dropna().astype(int))
missing_weeks = weeks_expected - weeks_found
if missing_weeks:
    print(f"  ⚠ WARNING: Missing content for weeks: {sorted(missing_weeks)}")
else:
    print(f"  ✓ All 7 weeks have content")

print("\n[CHECK 2] Verify survey items have proper difficulty coding:")
difficulty_values = df_mapping['Item_Difficulty'].dropna()
print(f"  ✓ {len(difficulty_values)} items have difficulty ratings")
if len(difficulty_values) > 0:
    # Try to extract numeric values from difficulty strings
    try:
        difficulty_numeric = pd.to_numeric(difficulty_values.str.extract(r'(-?\d+\.?\d*)')[0], errors='coerce')
        difficulty_numeric = difficulty_numeric.dropna()
        if len(difficulty_numeric) > 0:
            print(f"  ✓ Difficulty range: {difficulty_numeric.min():.2f} to {difficulty_numeric.max():.2f}")
        else:
            print(f"  ℹ Difficulty values: {difficulty_values.unique()[:5]}")
    except:
        print(f"  ℹ Difficulty values: {difficulty_values.unique()[:5]}")

print("\n[CHECK 3] Check for orphan items (no week assigned):")
orphan_items = df_mapping[df_mapping['Week_Number'].isna()]
print(f"  ℹ {len(orphan_items)} items without week assignment")
if len(orphan_items) > 0:
    print(f"    Topics: {orphan_items['Learning_Topic'].value_counts().to_dict()}")

print("\n[CHECK 4] Verify concept categories distribution:")
category_dist = df_mapping['Concept_Category'].value_counts()
print(category_dist.to_string())

print("\n[CHECK 5] Check concreteness level distribution:")
concreteness_dist = df_mapping['Concreteness_Level'].value_counts().sort_index()
print(concreteness_dist.to_string())

# ============================================================================
# STEP 9: Create Summary Statistics
# ============================================================================
print("\n[STEP 9] Creating summary statistics...")

# Concept coverage summary
concept_coverage = []
for week_key, week_data in curriculum_concepts.items():
    week_num = int(week_key.split()[1])
    
    # Count how many items assess this week's content
    items_this_week = df_mapping[df_mapping['Week_Number'] == week_num]
    
    concept_coverage.append({
        'Week': week_num,
        'N_Concepts_Taught': len(week_data['concepts']),
        'N_Activities': len(week_data['activities']),
        'N_Survey_Items': len(items_this_week),
        'Instructional_Time_Min': week_data['instructional_time'],
        'Assessment_Time_Min': week_data['assessment_time'],
        'Minutes_Per_Concept': week_data['instructional_time'] / len(week_data['concepts']) if week_data['concepts'] else 0
    })

df_coverage = pd.DataFrame(concept_coverage)
print("\n✓ Curriculum coverage summary:")
print(df_coverage.to_string(index=False))

print(f"\n✓ Total concepts taught: {df_coverage['N_Concepts_Taught'].sum()}")
print(f"✓ Total survey items: {df_mapping['Has_Assessment_Item'].sum()}")
print(f"✓ Average concepts per week: {df_coverage['N_Concepts_Taught'].mean():.1f}")
print(f"✓ Average time per concept: {df_coverage['Minutes_Per_Concept'].mean():.1f} minutes")

# ============================================================================
# STEP 10: Create Detailed Concept-Item Mapping Table
# ============================================================================
print("\n[STEP 10] Creating detailed concept-item mapping table...")

# Expand mapping to have one row per concept per item
detailed_rows = []

for week_key, week_data in curriculum_concepts.items():
    week_num = int(week_key.split()[1])
    
    # Get all items for this week
    items_this_week = df_mapping[df_mapping['Week_Number'] == week_num]
    
    # For each concept in this week
    for concept in week_data['concepts']:
        # Find matching survey items
        matching_items = []
        for idx, item_row in items_this_week.iterrows():
            # Check if item relates to this concept (keyword matching)
            item_text = f"{item_row['Learning_Topic']} {item_row['Learning_Objective']}".lower()
            concept_lower = concept.lower()
            
            # Extract key words from concept
            concept_keywords_local = concept_lower.split()[:3]  # First 3 words
            if any(kw in item_text for kw in concept_keywords_local):
                matching_items.append({
                    'item_id': idx,
                    'item_text': item_row['Survey_Item_English'],
                    'difficulty': item_row['Item_Difficulty']
                })
        
        # Determine concreteness
        concept_lower = concept.lower()
        if any(x in concept_lower for x in ['component', 'motor', 'sensor', 'assembly', 'robot part']):
            concreteness = 5
        elif any(x in concept_lower for x in ['programming', 'code', 'blockly', 'c++', 'arduino']):
            concreteness = 4
        elif any(x in concept_lower for x in ['activity', 'game', 'teachablemachine', 'testing']):
            concreteness = 3
        elif any(x in concept_lower for x in ['example', 'case study', 'uses of']):
            concreteness = 3
        elif any(x in concept_lower for x in ['definition', 'what is', 'introduction']):
            concreteness = 2
        else:
            concreteness = 2
        
        # Find concept category and repetition
        category_match = None
        repetition_count = 0
        for cat_name, cat_keywords in concept_keywords.items():
            if any(kw in concept_lower for kw in cat_keywords):
                category_match = cat_name
                repetition_count = concept_repetition[cat_name]['n_weeks']
                break
        
        detailed_rows.append({
            'Week_Number': week_num,
            'Week': week_key,
            'Concept': concept,
            'Concept_Category': category_match or 'Other',
            'Concreteness_Level': concreteness,
            'Repetition_N_Weeks': repetition_count,
            'N_Matching_Items': len(matching_items),
            'Has_Assessment': len(matching_items) > 0,
            'Matching_Item_IDs': ', '.join([str(x['item_id']) for x in matching_items]) if matching_items else '',
            'Item_Difficulties': ', '.join([str(x['difficulty']) for x in matching_items if pd.notna(x['difficulty'])]) if matching_items else '',
            'Instructional_Time_Min': week_data['instructional_time'],
            'N_Concepts_Week': len(week_data['concepts']),
            'Time_Per_Concept_Min': week_data['instructional_time'] / len(week_data['concepts'])
        })

df_detailed = pd.DataFrame(detailed_rows)
print(f"✓ Created detailed mapping with {len(df_detailed)} concept rows")

# ============================================================================
# STEP 11: Final Validation
# ============================================================================
print("\n[STEP 11] Final validation checks...")

print("\n[FINAL CHECK 1] Concepts without assessment items:")
no_assessment = df_detailed[~df_detailed['Has_Assessment']]
print(f"  ℹ {len(no_assessment)} concepts ({len(no_assessment)/len(df_detailed)*100:.1f}%) have no direct assessment items")
print(f"    Examples: {no_assessment['Concept'].head(5).tolist()}")

print("\n[FINAL CHECK 2] Concepts with highest repetition:")
high_rep = df_detailed.nlargest(5, 'Repetition_N_Weeks')[['Concept', 'Repetition_N_Weeks', 'Has_Assessment']]
print(high_rep.to_string(index=False))

print("\n[FINAL CHECK 3] Concreteness distribution:")
concreteness_summary = df_detailed.groupby('Concreteness_Level').agg({
    'Concept': 'count',
    'Has_Assessment': 'sum'
}).reset_index()
concreteness_summary.columns = ['Concreteness_Level', 'N_Concepts', 'N_With_Assessment']
concreteness_summary['Pct_Assessed'] = (concreteness_summary['N_With_Assessment'] / concreteness_summary['N_Concepts']) * 100
print(concreteness_summary.to_string(index=False))

print("\n[FINAL CHECK 4] Week-by-week summary:")
week_summary_final = df_detailed.groupby('Week_Number').agg({
    'Concept': 'count',
    'Has_Assessment': 'sum',
    'Concreteness_Level': 'mean',
    'Repetition_N_Weeks': 'mean',
    'Time_Per_Concept_Min': 'first'
}).reset_index()
week_summary_final.columns = ['Week', 'N_Concepts', 'N_Assessed', 'Avg_Concreteness', 'Avg_Repetition', 'Time_Per_Concept']
week_summary_final['Pct_Assessed'] = (week_summary_final['N_Assessed'] / week_summary_final['N_Concepts']) * 100
print(week_summary_final.to_string(index=False))

# ============================================================================
# STEP 12: Save Output Files
# ============================================================================
print("\n[STEP 12] Saving output files...")

# Save detailed mapping
output_detailed = OUTPUT_DIR / "curriculum_concept_to_item_mapping.csv"
df_detailed.to_csv(output_detailed, index=False)
print(f"✓ Saved: {output_detailed}")

# Save summary by week
output_summary = OUTPUT_DIR / "curriculum_weekly_summary.csv"
df_coverage.to_csv(output_summary, index=False)
print(f"✓ Saved: {output_summary}")

# Save concept repetition analysis
df_repetition = pd.DataFrame([
    {
        'Concept_Category': cat,
        'N_Weeks_Appearing': stats['n_weeks'],
        'Weeks': str(stats['weeks']),
        'Max_Spacing': stats['spacing']
    }
    for cat, stats in concept_repetition.items()
]).sort_values('N_Weeks_Appearing', ascending=False)

output_repetition = OUTPUT_DIR / "concept_repetition_analysis.csv"
df_repetition.to_csv(output_repetition, index=False)
print(f"✓ Saved: {output_repetition}")

# ============================================================================
# STEP 13: Generate Report
# ============================================================================
print("\n[STEP 13] Generating analysis report...")

report = f"""
# Curriculum Concept Mapping - Analysis Report

Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}

## Summary Statistics

- **Total curriculum concepts**: {len(df_detailed)}
- **Total survey items**: {len(df_mapping)}
- **Weeks analyzed**: 7
- **Average concepts per week**: {df_coverage['N_Concepts_Taught'].mean():.1f} (SD={df_coverage['N_Concepts_Taught'].std():.1f})
- **Total instructional time**: {df_coverage['Instructional_Time_Min'].sum()} minutes ({df_coverage['Instructional_Time_Min'].sum()/60:.1f} hours)

## Concept Repetition

### Most Repeated Concepts (appear in ≥3 weeks):
{df_repetition[df_repetition['N_Weeks_Appearing'] >= 3].to_markdown(index=False)}

### Least Repeated Concepts (appear in 1 week only):
{df_repetition[df_repetition['N_Weeks_Appearing'] == 1].to_markdown(index=False)}

## Assessment Alignment

### By Week:
{week_summary_final[['Week', 'N_Concepts', 'N_Assessed', 'Pct_Assessed']].to_markdown(index=False)}

**Overall**: {df_detailed['Has_Assessment'].sum()} of {len(df_detailed)} concepts ({df_detailed['Has_Assessment'].sum()/len(df_detailed)*100:.1f}%) have direct assessment items

## Concreteness Analysis

{concreteness_summary.to_markdown(index=False)}

**Interpretation**:
- Level 5 (Physical embodiment): Building robot, manipulating physical components
- Level 4 (Interactive application): Programming, using tools
- Level 3 (Hands-on demonstration): Activities, games, experiments
- Level 2 (Conceptual): Definitions, explanations, theoretical content

**Average concreteness**: {df_detailed['Concreteness_Level'].mean():.2f} (SD={df_detailed['Concreteness_Level'].std():.2f})

## Potential Issues Identified

### Issue 1: Low Assessment Coverage
{len(no_assessment)} concepts ({len(no_assessment)/len(df_detailed)*100:.1f}%) have no direct assessment items.
This may explain why learning gains are difficult to detect—many taught concepts are not measured.

**Examples of unassessed concepts**:
{no_assessment['Concept'].head(10).tolist()}

### Issue 2: Uneven Time Distribution
- Week with most concepts: Week {df_coverage.loc[df_coverage['N_Concepts_Taught'].idxmax(), 'Week']} ({df_coverage['N_Concepts_Taught'].max()} concepts)
- Week with fewest concepts: Week {df_coverage.loc[df_coverage['N_Concepts_Taught'].idxmin(), 'Week']} ({df_coverage['N_Concepts_Taught'].min()} concepts)
- Time per concept ranges from {df_coverage['Minutes_Per_Concept'].min():.1f} to {df_coverage['Minutes_Per_Concept'].max():.1f} minutes

**Implication**: Some concepts may have insufficient time for deep learning (cognitive load concerns).

### Issue 3: Concept Repetition Inconsistency
- High repetition concepts (≥3 weeks): {len(df_repetition[df_repetition['N_Weeks_Appearing'] >= 3])} concepts
- Single-exposure concepts (1 week): {len(df_repetition[df_repetition['N_Weeks_Appearing'] == 1])} concepts

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
"""

report_path = OUTPUT_DIR / "curriculum_mapping_report.md"
with open(report_path, 'w') as f:
    f.write(report)
print(f"✓ Saved: {report_path}")

# ============================================================================
# COMPLETION
# ============================================================================
print("\n" + "="*80)
print("✓ ANALYSIS COMPLETE")
print("="*80)
print(f"\nGenerated {3} CSV files and 1 report in:")
print(f"  {OUTPUT_DIR}")
print("\nNext: Review the mapping CSV and run learning analysis!")
