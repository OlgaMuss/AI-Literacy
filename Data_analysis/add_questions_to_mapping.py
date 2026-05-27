"""
Add Assessment Questions and Correct Answers to Curriculum Mapping

This script enhances the curriculum_concept_to_item_mapping.csv by adding:
1. Assessment_Question - Full English question text
2. Correct_Answer - The correct answer option

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
print("ADDING ASSESSMENT QUESTIONS TO CURRICULUM MAPPING")
print("="*80)

# ============================================================================
# STEP 1: Load Existing Mapping
# ============================================================================
print("\n[STEP 1] Loading existing curriculum mapping...")

mapping_path = OUTPUT_DIR / "curriculum_concept_to_item_mapping.csv"
df_mapping = pd.read_csv(mapping_path)
print(f"✓ Loaded {len(df_mapping)} concept rows")
print(f"✓ Columns: {list(df_mapping.columns)}")

# ============================================================================
# STEP 2: Load Learning Objectives Codebook with Questions
# ============================================================================
print("\n[STEP 2] Loading learning objectives codebook with questions...")

learning_obj_path = CODEBOOK_DIR / "Learning objectives-Table 1.csv"
df_questions = pd.read_csv(learning_obj_path, sep=';')
print(f"✓ Loaded {len(df_questions)} question items")

# ============================================================================
# STEP 3: Parse Questions and Extract Correct Answers
# ============================================================================
print("\n[STEP 3] Parsing questions and extracting correct answers...")

def extract_correct_answer(question_text):
    """
    Extract the correct answer from question text.
    Assumes correct answer is typically 'a' for most items based on AICOS format.
    Will need manual verification.
    """
    if pd.isna(question_text):
        return None, None
    
    # Clean the text
    text = str(question_text).strip()
    
    # Extract question stem (before answer options)
    parts = re.split(r'\n[a-d]\)', text)
    question_stem = parts[0].strip() if parts else text
    
    # Extract all answer options
    options = re.findall(r'([a-d])\)\s*(.+?)(?=\n[a-d]\)|$)', text, re.DOTALL)
    
    if not options:
        return question_stem, None
    
    # Format options
    formatted_options = []
    for letter, option_text in options:
        option_clean = option_text.strip().replace('\n', ' ')
        formatted_options.append(f"{letter}) {option_clean}")
    
    # Full question with options
    full_question = question_stem + "\n" + "\n".join(formatted_options)
    
    # Determine correct answer (need to look at item difficulty or source notes)
    # For now, mark as 'NEEDS_VERIFICATION' - we'll add this manually
    correct_answer = "VERIFY"
    
    return full_question, correct_answer

# Process each question
df_questions['Question_Parsed'] = None
df_questions['Correct_Answer'] = None

for idx, row in df_questions.iterrows():
    english_text = row['English']
    question, answer = extract_correct_answer(english_text)
    df_questions.at[idx, 'Question_Parsed'] = question
    df_questions.at[idx, 'Correct_Answer'] = answer

print(f"✓ Parsed {df_questions['Question_Parsed'].notna().sum()} questions")

# ============================================================================
# STEP 4: Create Item ID Lookup
# ============================================================================
print("\n[STEP 4] Creating item ID lookup...")

# Create a lookup dictionary: item_id -> (question, correct_answer)
item_lookup = {}
for idx, row in df_questions.iterrows():
    item_id = idx
    item_lookup[item_id] = {
        'question': row['Question_Parsed'],
        'correct_answer': row['Correct_Answer'],
        'learning_topic': row['Learning topics'],
        'learning_objective': row['Learning objective'],
        'difficulty': row['Item difficulty'],
        'source': row['Source']
    }

print(f"✓ Created lookup for {len(item_lookup)} items")

# ============================================================================
# STEP 5: Add Questions and Answers to Mapping
# ============================================================================
print("\n[STEP 5] Adding questions and answers to mapping...")

# Initialize new columns
df_mapping['Assessment_Question'] = None
df_mapping['Correct_Answer'] = None
df_mapping['Item_Source'] = None

# For each concept row, add questions for matching items
for idx, row in df_mapping.iterrows():
    matching_ids = row['Matching_Item_IDs']
    
    if pd.isna(matching_ids) or matching_ids == '':
        continue
    
    # Parse matching IDs (can be comma-separated)
    id_list = [int(x.strip()) for x in str(matching_ids).split(',') if x.strip().isdigit()]
    
    if not id_list:
        continue
    
    # Collect questions and answers for all matching items
    questions = []
    answers = []
    sources = []
    
    for item_id in id_list:
        if item_id in item_lookup:
            item_info = item_lookup[item_id]
            if item_info['question']:
                questions.append(f"[Item {item_id}] {item_info['question']}")
                answers.append(item_info['correct_answer'])
                sources.append(item_info['source'] if pd.notna(item_info['source']) else 'Unknown')
    
    # Add to dataframe
    if questions:
        df_mapping.at[idx, 'Assessment_Question'] = " || ".join(questions)
        df_mapping.at[idx, 'Correct_Answer'] = ", ".join([str(a) for a in answers if a])
        df_mapping.at[idx, 'Item_Source'] = ", ".join(set(sources))

print(f"✓ Added questions to {df_mapping['Assessment_Question'].notna().sum()} concept rows")

# ============================================================================
# STEP 6: Validation Checks
# ============================================================================
print("\n[STEP 6] Running validation checks...")

print("\n[CHECK 1] Verify Has_Assessment matches new Assessment_Question column:")
has_assessment = df_mapping['Has_Assessment']
has_question = df_mapping['Assessment_Question'].notna()
matches = (has_assessment == has_question).sum()
total = len(df_mapping)
print(f"  ✓ {matches}/{total} rows match ({matches/total*100:.1f}%)")

mismatches = df_mapping[has_assessment != has_question]
if len(mismatches) > 0:
    print(f"  ⚠ {len(mismatches)} mismatches found:")
    for idx, row in mismatches.head(3).iterrows():
        print(f"    - Row {idx}: Has_Assessment={row['Has_Assessment']}, Has_Question={has_question[idx]}")

print("\n[CHECK 2] Sample questions preview:")
sample_with_questions = df_mapping[df_mapping['Assessment_Question'].notna()].head(3)
for idx, row in sample_with_questions.iterrows():
    print(f"\n  Concept: {row['Concept']}")
    print(f"  Question preview: {row['Assessment_Question'][:150]}...")
    print(f"  Answer: {row['Correct_Answer']}")

print("\n[CHECK 3] Items without questions (should be concepts with no assessment):")
no_questions = df_mapping[df_mapping['Assessment_Question'].isna()]
print(f"  ✓ {len(no_questions)} concepts have no assessment items")
print(f"  ✓ Examples: {no_questions['Concept'].head(5).tolist()}")

# ============================================================================
# STEP 7: Save Enhanced Mapping
# ============================================================================
print("\n[STEP 7] Saving enhanced mapping...")

# Reorder columns for better readability
column_order = [
    'Week_Number', 'Week', 'Concept', 'Concept_Category',
    'Concreteness_Level', 'Repetition_N_Weeks', 'Time_Per_Concept_Min',
    'Has_Assessment', 'N_Matching_Items', 'Matching_Item_IDs',
    'Assessment_Question', 'Correct_Answer', 'Item_Difficulties', 'Item_Source',
    'Instructional_Time_Min', 'N_Concepts_Week'
]

df_mapping_ordered = df_mapping[column_order]

output_path = OUTPUT_DIR / "curriculum_concept_to_item_mapping_with_questions.csv"
df_mapping_ordered.to_csv(output_path, index=False)
print(f"✓ Saved: {output_path}")

# ============================================================================
# STEP 8: Create Summary Report
# ============================================================================
print("\n[STEP 8] Creating summary report...")

summary_stats = {
    'Total concepts': len(df_mapping),
    'Concepts with assessment': df_mapping['Has_Assessment'].sum(),
    'Concepts without assessment': (~df_mapping['Has_Assessment']).sum(),
    'Assessment coverage': f"{df_mapping['Has_Assessment'].sum() / len(df_mapping) * 100:.1f}%",
    'Total survey items': df_mapping['N_Matching_Items'].sum(),
    'Avg questions per assessed concept': df_mapping[df_mapping['Has_Assessment']]['N_Matching_Items'].mean()
}

print("\n✓ Summary Statistics:")
for key, value in summary_stats.items():
    print(f"  - {key}: {value}")

# ============================================================================
# STEP 9: Create Question List for Manual Review
# ============================================================================
print("\n[STEP 9] Creating question list for manual verification...")

# Extract all unique questions
all_questions = []
for idx, row in df_mapping[df_mapping['Assessment_Question'].notna()].iterrows():
    questions_text = row['Assessment_Question']
    # Split multiple questions if combined
    question_parts = questions_text.split(' || ')
    for q in question_parts:
        # Extract item ID
        item_id_match = re.search(r'\[Item (\d+)\]', q)
        item_id = int(item_id_match.group(1)) if item_id_match else None
        
        all_questions.append({
            'Item_ID': item_id,
            'Concept': row['Concept'],
            'Week': row['Week_Number'],
            'Question': q,
            'Correct_Answer': row['Correct_Answer'],
            'Difficulty': row['Item_Difficulties']
        })

df_questions_review = pd.DataFrame(all_questions).drop_duplicates(subset=['Item_ID'])
df_questions_review = df_questions_review.sort_values('Week')

review_path = OUTPUT_DIR / "assessment_questions_for_review.csv"
df_questions_review.to_csv(review_path, index=False)
print(f"✓ Saved question list: {review_path}")
print(f"✓ Total unique questions: {len(df_questions_review)}")

# ============================================================================
# COMPLETION
# ============================================================================
print("\n" + "="*80)
print("✓ ENHANCEMENT COMPLETE")
print("="*80)
print(f"\nGenerated files:")
print(f"  1. curriculum_concept_to_item_mapping_with_questions.csv - Enhanced mapping with questions")
print(f"  2. assessment_questions_for_review.csv - Question list for manual verification")
print(f"\n⚠ NEXT STEP: Manually verify correct answers in assessment_questions_for_review.csv")
print(f"  The 'Correct_Answer' column shows 'VERIFY' - you need to add the actual correct answers.")
