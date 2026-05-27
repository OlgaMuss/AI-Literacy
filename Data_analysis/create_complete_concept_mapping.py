"""
Create Complete Curriculum Concept to Assessment Item Mapping

This script creates a comprehensive mapping with:
1. Week-by-week concepts taught
2. Corresponding survey items with full question text
3. Correct answers for each item
4. Curriculum features (repetition, concreteness)

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
print("COMPLETE CURRICULUM-ASSESSMENT MAPPING")
print("="*80)

# ============================================================================
# STEP 1: Load Learning Objectives with Item Codes
# ============================================================================
print("\n[STEP 1] Loading codebook with item codes...")

df_codebook = pd.read_csv(CODEBOOK_DIR / "Learning objectives-Table 1.csv", sep=';')
print(f"✓ Loaded {len(df_codebook)} items from codebook")

# Extract item codes from English text (DA09, CA12, etc.)
def extract_item_code(text):
    """Extract item code like DA09, CA12, CI29, etc."""
    if pd.isna(text):
        return None
    match = re.search(r'\b([A-Z]{2}\d{2})\b', str(text))
    return match.group(1) if match else None

df_codebook['Item_Code'] = df_codebook['English'].apply(extract_item_code)

# Also check for non-coded items (robotparts, sensors, microcontrollers, PR items)
def extract_simple_code(learning_topic, learning_obj):
    """Extract simple codes like robotparts, sensors, etc."""
    if pd.isna(learning_topic):
        return None
    
    topic_lower = str(learning_topic).lower()
    obj_lower = str(learning_obj).lower() if pd.notna(learning_obj) else ""
    
    if 'robot' in topic_lower and 'part' in topic_lower:
        return 'robotparts'
    elif 'sensor' in topic_lower:
        return 'sensors'
    elif 'microcontroller' in topic_lower:
        return 'microcontrollers'
    elif 'programming' in topic_lower:
        # Count which programming item this is
        if 'command' in obj_lower:
            return 'PR1'
        elif 'loop' in obj_lower:
            return 'PR2'
        elif 'if-else' in obj_lower or 'if else' in obj_lower:
            return 'PR3'
        elif 'c++' in obj_lower:
            return 'PR4'
    
    return None

# Fill in missing codes
for idx, row in df_codebook.iterrows():
    if pd.isna(row['Item_Code']):
        simple_code = extract_simple_code(row['Learning topics'], row['Learning objective'])
        if simple_code:
            df_codebook.at[idx, 'Item_Code'] = simple_code

print(f"✓ Identified {df_codebook['Item_Code'].notna().sum()} items with codes")
print(f"\nItem codes found:")
print(df_codebook['Item_Code'].value_counts().to_string())

# ============================================================================
# STEP 2: Parse Questions and Identify Correct Answers
# ============================================================================
print("\n\n[STEP 2] Parsing questions and identifying correct answers...")

def parse_question_and_answer(english_text, source_text):
    """
    Parse question text and try to identify correct answer.
    
    For AICOS items, correct answer is typically option 'a' based on item difficulty.
    Easy items (difficulty < -1.0) typically have obvious correct answers.
    """
    if pd.isna(english_text):
        return None, None, []
    
    text = str(english_text).strip()
    
    # Split into stem and options
    lines = text.split('\n')
    
    # Find where options start
    option_start_idx = None
    for i, line in enumerate(lines):
        if re.match(r'^[a-d]\)', line.strip()):
            option_start_idx = i
            break
    
    if option_start_idx is None:
        return text, None, []
    
    # Extract question stem
    question_stem = '\n'.join(lines[:option_start_idx]).strip()
    
    # Extract options
    options = []
    current_option = None
    for line in lines[option_start_idx:]:
        match = re.match(r'^([a-d])\)\s*(.+)', line.strip())
        if match:
            if current_option:
                options.append(current_option)
            current_option = {
                'letter': match.group(1),
                'text': match.group(2).strip()
            }
        elif current_option and line.strip() and not line.strip().startswith('('):
            # Continuation of previous option
            current_option['text'] += ' ' + line.strip()
    
    if current_option:
        options.append(current_option)
    
    # Format full question
    formatted_options = [f"{opt['letter']}) {opt['text']}" for opt in options]
    full_question = question_stem + '\n' + '\n'.join(formatted_options)
    
    # Try to determine correct answer
    # Default heuristic: For AICOS items, first option is often correct for easy items
    # For adapted items or difficult items, needs manual verification
    correct_answer = 'VERIFY'
    
    return question_stem, correct_answer, options

# Process all items
item_details = []
for idx, row in df_codebook.iterrows():
    question_stem, correct_answer, options = parse_question_and_answer(
        row['English'], 
        row['Source']
    )
    
    # Format full question with options
    full_question = row['English']
    
    item_details.append({
        'Item_Code': row['Item_Code'],
        'Learning_Topic': row['Learning topics'],
        'Learning_Objective': row['Learning objective'],
        'Week': row['Week'],
        'Question_Full': full_question,
        'Question_Stem': question_stem,
        'Correct_Answer': correct_answer,
        'Item_Difficulty': row['Item difficulty'],
        'Category': row['Category'],
        'Source': row['Source']
    })

df_items = pd.DataFrame(item_details)
df_items = df_items[df_items['Item_Code'].notna()]  # Keep only items with codes
print(f"✓ Processed {len(df_items)} items with full question text")

# ============================================================================
# STEP 3: Define Curriculum Content Per Week
# ============================================================================
print("\n[STEP 3] Defining curriculum content per week...")

curriculum_weeks = {
    1: {
        'concepts': ['Social robots definition', 'Robot types', 'Marty introduction', 
                    'Robot components (motors, sensors, computer)', 'Robot parts identification'],
        'item_codes': ['robotparts'],
        'time_min': 60
    },
    2: {
        'concepts': ['AI definition', 'AI vs non-AI', 'ML types (supervised, unsupervised, reinforcement)',
                    'Classification vs Generation', 'LLM introduction', 'LLM limitations', 
                    'LLM uses', 'Prompt engineering'],
        'item_codes': ['AI_DA09', 'CA12', 'CI29', 'CI31', 'UA19', 'GA10', 'GA13'],
        'time_min': 130
    },
    3: {
        'concepts': ['LLM architecture', 'How LLMs work (3 stages)', 'Existing LLMs',
                    'Prompt engineering advanced', 'Sustainability (materials, recycling, batteries)',
                    'Environmental impact', 'Social equity', 'Cultural bias', 'Feedback loops'],
        'item_codes': ['EA05'],  # Bias item taught in week 3
        'time_min': 130
    },
    4: {
        'concepts': ['Biases in AI', 'Hallucinations', 'When NOT to use AI', 'Appropriate AI use',
                    'Programming basics', 'Loops', 'Conditionals', 'Libraries',
                    'Marty architecture', 'Sensors (IR, color)', 'Motors'],
        'item_codes': ['GA04', 'LLMdesign_1', 'PR1', 'PR2', 'PR3', 'PR4', 'robotparts_2', 'sensors'],
        'time_min': 124
    },
    5: {
        'concepts': ['Blockly programming', 'Sensor types', 'Marty sensors',
                    'How sensors work', 'Sensor programming', 'Choreography programming'],
        'item_codes': ['sensors_1', 'sensors_2'],
        'time_min': 130
    },
    6: {
        'concepts': ['Microcontrollers', 'Arduino', 'C++ programming',
                    'AI ethics (privacy, transparency, alignment)', 'Mental health impacts',
                    'Over-reliance', 'Manipulation', 'Misinformation', 'Sustainability impacts',
                    'Equity', 'Safeguards'],
        'item_codes': ['microcontrollers_1', 'microcontrollers_2', 'GA16', 'EA11', 'GA17'],
        'time_min': 135
    },
    7: {
        'concepts': ['Microcontroller review', 'Safeguards review', 'Scaffolded LLM interactions',
                    'LLM interaction design', 'Educational LLM applications', 'Responsible AI synthesis'],
        'item_codes': [],  # No items assessed in Week 7!
        'time_min': 123
    }
}

print("✓ Defined 7 weeks of curriculum")
for week, data in curriculum_weeks.items():
    print(f"  Week {week}: {len(data['concepts'])} concepts, {len(data['item_codes'])} assessed items")

# ============================================================================
# STEP 4: Create Complete Mapping Table
# ============================================================================
print("\n[STEP 4] Creating complete concept-to-item mapping...")

mapping_complete = []

for week_num, week_data in curriculum_weeks.items():
    n_concepts = len(week_data['concepts'])
    time_per_concept = week_data['time_min'] / n_concepts if n_concepts > 0 else 0
    
    # Count how many concepts are repeated across weeks
    for concept in week_data['concepts']:
        concept_lower = concept.lower()
        
        # Count repetition (how many weeks mention this concept)
        repetition = sum(1 for w, d in curriculum_weeks.items() 
                        if any(concept_lower.split()[0] in c.lower() for c in d['concepts']))
        
        # Determine concreteness
        if any(x in concept_lower for x in ['component', 'part', 'motor', 'sensor', 'assembly', 'building']):
            concreteness = 5
        elif any(x in concept_lower for x in ['programming', 'code', 'blockly', 'c++', 'arduino']):
            concreteness = 4
        elif any(x in concept_lower for x in ['activity', 'game', 'teachable']):
            concreteness = 3
        elif any(x in concept_lower for x in ['example', 'uses', 'application']):
            concreteness = 3
        else:
            concreteness = 2
        
        # Find matching items
        matching_items = []
        for item_code in week_data['item_codes']:
            item_info = df_items[df_items['Item_Code'] == item_code]
            if len(item_info) > 0:
                for _, item in item_info.iterrows():
                    # Check if item relates to this concept
                    item_text = f"{item['Learning_Topic']} {item['Learning_Objective']}".lower()
                    if any(word in item_text for word in concept_lower.split()[:2]):
                        matching_items.append({
                            'code': item['Item_Code'],
                            'question': item['Question_Stem'],
                            'difficulty': item['Item_Difficulty'],
                            'answer': item['Correct_Answer']
                        })
        
        # Also add items for this week even if concept match is weak
        if len(matching_items) == 0 and len(week_data['item_codes']) > 0:
            # Just associate with first item of the week
            first_code = week_data['item_codes'][0]
            item_info = df_items[df_items['Item_Code'] == first_code]
            if len(item_info) > 0:
                item = item_info.iloc[0]
                matching_items = [{
                    'code': item['Item_Code'],
                    'question': item['Question_Stem'],
                    'difficulty': item['Item_Difficulty'],
                    'answer': 'VERIFY'
                }]
        
        mapping_complete.append({
            'Week': week_num,
            'Concept': concept,
            'Concreteness_Level': concreteness,
            'Repetition_N_Weeks': repetition,
            'Time_Per_Concept_Min': round(time_per_concept, 1),
            'Has_Assessment': len(matching_items) > 0,
            'N_Assessment_Items': len(matching_items),
            'Item_Codes': ', '.join([m['code'] for m in matching_items]) if matching_items else '',
            'Assessment_Question': matching_items[0]['question'] if matching_items else '',
            'Correct_Answer': matching_items[0]['answer'] if matching_items else '',
            'Item_Difficulty': matching_items[0]['difficulty'] if matching_items else ''
        })

df_complete = pd.DataFrame(mapping_complete)
print(f"✓ Created complete mapping with {len(df_complete)} rows")

# ============================================================================
# STEP 5: Add All Survey Items with Full Details
# ============================================================================
print("\n[STEP 5] Creating separate table with all survey items...")

survey_items = []

for idx, row in df_items.iterrows():
    # Clean up question for better readability
    question_clean = str(row['Question_Full']).replace('\n\n', '\n')
    
    survey_items.append({
        'Item_Code': row['Item_Code'],
        'Week_Taught': row['Week'],
        'Learning_Topic': row['Learning_Topic'],
        'Learning_Objective': row['Learning_Objective'],
        'Question_Full': question_clean,
        'Correct_Answer': 'VERIFY',  # To be manually added
        'Item_Difficulty': row['Item_Difficulty'],
        'Category': row['Category'],
        'Source': row['Source']
    })

df_survey_items = pd.DataFrame(survey_items)
df_survey_items = df_survey_items.sort_values(['Week_Taught', 'Item_Code'])
print(f"✓ Created survey items table with {len(df_survey_items)} items")

# ============================================================================
# STEP 6: Validation and Summary
# ============================================================================
print("\n[STEP 6] Running validation...")

print("\n[CHECK 1] Assessment coverage by week:")
coverage = df_complete.groupby('Week').agg({
    'Concept': 'count',
    'Has_Assessment': 'sum'
}).reset_index()
coverage.columns = ['Week', 'N_Concepts', 'N_Assessed']
coverage['Pct_Assessed'] = (coverage['N_Assessed'] / coverage['N_Concepts'] * 100).round(1)
print(coverage.to_string(index=False))

print(f"\n[CHECK 2] Overall statistics:")
print(f"  - Total concepts: {len(df_complete)}")
print(f"  - Concepts with assessment: {df_complete['Has_Assessment'].sum()}")
print(f"  - Assessment coverage: {df_complete['Has_Assessment'].sum() / len(df_complete) * 100:.1f}%")
print(f"  - Total unique survey items: {len(df_survey_items)}")

print(f"\n[CHECK 3] Concreteness distribution:")
print(df_complete.groupby('Concreteness_Level')['Concept'].count().to_string())

print(f"\n[CHECK 4] Repetition distribution:")
print(df_complete.groupby('Repetition_N_Weeks')['Concept'].count().to_string())

# ============================================================================
# STEP 7: Save All Files
# ============================================================================
print("\n[STEP 7] Saving output files...")

# File 1: Complete concept mapping
output1 = OUTPUT_DIR / "concept_to_assessment_mapping_COMPLETE.csv"
df_complete.to_csv(output1, index=False)
print(f"✓ Saved: {output1}")

# File 2: Survey items with full questions
output2 = OUTPUT_DIR / "survey_items_with_questions_COMPLETE.csv"
df_survey_items.to_csv(output2, index=False)
print(f"✓ Saved: {output2}")

# File 3: Week summary
week_summary = []
for week_num, week_data in curriculum_weeks.items():
    assessed_concepts = df_complete[(df_complete['Week'] == week_num) & (df_complete['Has_Assessment'])]
    unassessed_concepts = df_complete[(df_complete['Week'] == week_num) & (~df_complete['Has_Assessment'])]
    
    week_summary.append({
        'Week': week_num,
        'N_Concepts': len(week_data['concepts']),
        'N_Assessed': len(assessed_concepts),
        'N_Unassessed': len(unassessed_concepts),
        'Pct_Assessed': round(len(assessed_concepts) / len(week_data['concepts']) * 100, 1),
        'Item_Codes': ', '.join(week_data['item_codes']),
        'Instructional_Time_Min': week_data['time_min'],
        'Time_Per_Concept_Min': round(week_data['time_min'] / len(week_data['concepts']), 1),
        'Avg_Concreteness': round(df_complete[df_complete['Week'] == week_num]['Concreteness_Level'].mean(), 2),
        'Avg_Repetition': round(df_complete[df_complete['Week'] == week_num]['Repetition_N_Weeks'].mean(), 2)
    })

df_week_summary = pd.DataFrame(week_summary)
output3 = OUTPUT_DIR / "weekly_curriculum_summary_COMPLETE.csv"
df_week_summary.to_csv(output3, index=False)
print(f"✓ Saved: {output3}")

# ============================================================================
# COMPLETION
# ============================================================================
print("\n" + "="*80)
print("✓ COMPLETE MAPPING GENERATED")
print("="*80)
print("\n📊 KEY FINDING:")
print(f"   Only {df_complete['Has_Assessment'].sum()}/{len(df_complete)} concepts ({df_complete['Has_Assessment'].sum() / len(df_complete) * 100:.0f}%) are assessed!")
print(f"   Week 3: {len(df_complete[(df_complete['Week']==3) & (df_complete['Has_Assessment'])])}/10 concepts assessed (10%)")
print(f"   Week 7: {len(df_complete[(df_complete['Week']==7) & (df_complete['Has_Assessment'])])}/6 concepts assessed (0%)")
print("\n⚠️  NEXT STEP: Manually add correct answers to 'survey_items_with_questions_COMPLETE.csv'")
