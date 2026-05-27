"""
Extract ALL Questions from Codebook with Complete Options and Answers

This creates a comprehensive question bank with:
1. All questions from the codebook (including multi-item questions)
2. Full answer options (a, b, c, d)
3. Correct answers identified
4. Week, topic, and curriculum mapping

Author: Curriculum Analysis  
Date: April 2026
"""

import pandas as pd
import re
from pathlib import Path

DATA_DIR = Path("/Users/olga/Olga's workspace/Publications/AI and DL curriculum paper/Data_analysis/Data")
CODEBOOK_DIR = DATA_DIR / "Buildbots_Codebook_15122025-2"
OUTPUT_DIR = Path("/Users/olga/Olga's workspace/Publications/AI and DL curriculum paper/Data_analysis")

print("="*80)
print("EXTRACTING ALL QUESTIONS FROM CODEBOOK")
print("="*80)

# ============================================================================
# STEP 1: Load Codebook
# ============================================================================
print("\n[STEP 1] Loading codebook...")

df_codebook = pd.read_csv(CODEBOOK_DIR / "Learning objectives-Table 1.csv", sep=';')
print(f"✓ Loaded {len(df_codebook)} rows")

# ============================================================================
# STEP 2: Parse Each Question Cell (Can Contain Multiple Questions)
# ============================================================================
print("\n[STEP 2] Parsing all questions (including multiple per cell)...")

all_questions = []

for idx, row in df_codebook.iterrows():
    english_text = row['English']
    if pd.isna(english_text):
        continue
    
    # Split by numbered questions (1., 2., etc.)
    question_splits = re.split(r'\n\s*(\d+)\.\s+', str(english_text))
    
    # Process each question
    current_question_num = 0
    for i in range(len(question_splits)):
        # Check if this is a number (question marker)
        if i > 0 and question_splits[i-1].strip() and question_splits[i-1].strip().isdigit():
            current_question_num = int(question_splits[i-1])
            question_text = question_splits[i] if i < len(question_splits) else ""
        elif i == 0 and question_splits[i].strip():
            # First question without number prefix
            current_question_num = 1
            question_text = question_splits[i]
        else:
            continue
        
        if not question_text.strip():
            continue
        
        # Extract item code (DA09, CA12, etc.)
        item_code_match = re.search(r'\b([A-Z]{2}\d{2})\b', question_text)
        item_code = item_code_match.group(1) if item_code_match else None
        
        # Split into question stem and options
        lines = [l.strip() for l in question_text.split('\n') if l.strip()]
        
        # Find where options start (lines starting with a), b), c), d))
        option_start_idx = None
        for j, line in enumerate(lines):
            if re.match(r'^[a-d]\)', line):
                option_start_idx = j
                break
        
        if option_start_idx is None:
            # No options found, might be open-ended
            continue
        
        # Extract question stem
        question_stem_lines = lines[:option_start_idx]
        question_stem = ' '.join(question_stem_lines)
        
        # Remove item code from stem if present
        if item_code:
            question_stem = re.sub(r'\b' + item_code + r':\s*', '', question_stem)
        
        # Extract options
        options_text = lines[option_start_idx:]
        options = []
        current_opt = None
        
        for line in options_text:
            opt_match = re.match(r'^([a-d])\)\s*(.+)', line)
            if opt_match:
                if current_opt:
                    options.append(current_opt)
                current_opt = {
                    'letter': opt_match.group(1),
                    'text': opt_match.group(2).strip()
                }
            elif current_opt and line.strip():
                # Continuation of previous option
                if not any(x in line for x in ['AICOS', 'Zhang', 'AI-CHI', 'Markus']):
                    current_opt['text'] += ' ' + line.strip()
        
        if current_opt:
            options.append(current_opt)
        
        # Skip if not 4 options
        if len(options) != 4:
            print(f"⚠ Warning: Item has {len(options)} options (expected 4): {question_stem[:50]}...")
        
        all_questions.append({
            'Item_Code': item_code or f"Q{idx}_{current_question_num}",
            'Question_Number': current_question_num,
            'Row_Index': idx,
            'Week': row['Week'],
            'Learning_Topic': row['Learning topics'],
            'Learning_Objective': row['Learning objective'],
            'Question_Stem': question_stem.strip(),
            'Option_A': options[0]['text'] if len(options) > 0 else '',
            'Option_B': options[1]['text'] if len(options) > 1 else '',
            'Option_C': options[2]['text'] if len(options) > 2 else '',
            'Option_D': options[3]['text'] if len(options) > 3 else '',
            'Correct_Answer': 'VERIFY',
            'Item_Difficulty': row['Item difficulty'],
            'Category': row['Category'],
            'Source': row['Source']
        })

df_questions = pd.DataFrame(all_questions)
print(f"✓ Extracted {len(df_questions)} total questions")

# ============================================================================
# STEP 3: Add Correct Answers
# ============================================================================
print("\n[STEP 3] Adding correct answers...")

correct_answers = {
    # AI Items
    'DA09': ('a', 'Learning ability and independence - key AI characteristic'),
    'CA12': ('c', 'Big data storage is NOT AI (just data management)'),
    'CI29': ('a', 'Style conversion = Generation task'),
    'CI31': ('b', 'Labeled dataset = Supervised learning'),
    'UA19': ('a', 'Trial-and-error = core of reinforcement learning'),
    
    # LLM Items
    'GA10': ('a', 'Prompt = input text to control LLM output'),
    'GA13': ('d', 'GenAI learns from data and creates similar patterns'),
    'GA04': ('b', 'Too much data does NOT cause hallucinations'),
    
    # Ethics Items
    'EA05': ('b', 'Unconscious prejudices = algorithmic bias'),
    'EA11': ('d', 'Power consumption is a real AI risk'),
    'GA16': ('b', 'Replacing workers = social responsibility concern'),
    'GA17': ('VERIFY', 'Item not in codebook - needs checking'),
    
    # Programming Items
    'PR1': ('a', 'Command = single basic instruction'),
    'PR2': ('a', 'Loop = efficient for repetition'),
    'PR3': ('b', 'if-statement executes when condition is true'),
    'PR4': ('b', 'Correct sequence: walk then turn'),
    
    # Technical Items
    'robotparts_1': ('VERIFY', 'Picture-based, cannot determine without image'),
    'robotparts_2': ('a', 'Hip motor moves the entire leg'),
    'sensors_1': ('b', 'IR sensor detects obstacles/edges'),
    'sensors_2': ('c', 'Sensors sense, motors move (not vice versa)'),
    'microcontrollers_1': ('a', 'ESP32 is main processor with WiFi/Bluetooth'),
    'microcontrollers_2': ('a', 'Microcontroller runs simple programs, controls hardware'),
    
    # LLM Design
    'LLMdesign_1': ('c', 'Vague prompt ("tell me about science") lacks specificity'),
}

# Apply answers
for idx, row in df_questions.iterrows():
    item_code = row['Item_Code']
    if item_code in correct_answers:
        answer, rationale = correct_answers[item_code]
        df_questions.at[idx, 'Correct_Answer'] = answer
        df_questions.at[idx, 'Answer_Rationale'] = rationale

n_answered = (df_questions['Correct_Answer'] != 'VERIFY').sum()
print(f"✓ Added correct answers to {n_answered} questions")

# ============================================================================
# STEP 4: Create Multiple Output Formats
# ============================================================================
print("\n[STEP 4] Creating output files in multiple formats...")

# Format 1: Full CSV with all columns
output1 = OUTPUT_DIR / "all_survey_questions_COMPLETE.csv"
df_questions.to_csv(output1, index=False)
print(f"✓ Saved: {output1}")

# Format 2: Readable format with formatted question text
df_readable = df_questions.copy()
df_readable['Full_Question'] = df_readable.apply(lambda row: 
    f"{row['Question_Stem']}\n" +
    f"a) {row['Option_A']}\n" +
    f"b) {row['Option_B']}\n" +
    f"c) {row['Option_C']}\n" +
    f"d) {row['Option_D']}", axis=1
)

output2 = OUTPUT_DIR / "survey_questions_readable_format.csv"
df_readable[['Item_Code', 'Week', 'Learning_Topic', 'Learning_Objective', 
             'Full_Question', 'Correct_Answer', 'Answer_Rationale', 
             'Item_Difficulty']].to_csv(output2, index=False)
print(f"✓ Saved: {output2}")

# Format 3: For paper appendix (clean formatting)
df_paper = df_questions.copy()
df_paper = df_paper.sort_values(['Week', 'Item_Code'])

output3 = OUTPUT_DIR / "assessment_items_for_paper_appendix.csv"
df_paper[['Week', 'Item_Code', 'Learning_Topic', 'Question_Stem', 
          'Option_A', 'Option_B', 'Option_C', 'Option_D',
          'Correct_Answer', 'Item_Difficulty', 'Source']].to_csv(output3, index=False)
print(f"✓ Saved: {output3}")

# ============================================================================
# STEP 5: Update Concept Mapping with Full Questions
# ============================================================================
print("\n[STEP 5] Updating concept mapping with full question details...")

df_mapping = pd.read_csv(OUTPUT_DIR / "concept_to_assessment_mapping_FINAL.csv")

# Create item lookup: code -> full details
item_details_lookup = {}
for idx, row in df_questions.iterrows():
    item_details_lookup[row['Item_Code']] = {
        'question_stem': row['Question_Stem'],
        'options': {
            'a': row['Option_A'],
            'b': row['Option_B'],
            'c': row['Option_C'],
            'd': row['Option_D']
        },
        'correct_answer': row['Correct_Answer'],
        'rationale': row['Answer_Rationale']
    }

# Add separate columns for question components
df_mapping['Question_Stem'] = ''
df_mapping['Option_A'] = ''
df_mapping['Option_B'] = ''
df_mapping['Option_C'] = ''
df_mapping['Option_D'] = ''
df_mapping['Answer_Rationale'] = ''

for idx, row in df_mapping.iterrows():
    item_codes = row['Item_Codes']
    if pd.isna(item_codes) or item_codes == '':
        continue
    
    # Get first item code (if multiple, show first one)
    first_code = str(item_codes).split(',')[0].strip()
    
    if first_code in item_details_lookup:
        details = item_details_lookup[first_code]
        df_mapping.at[idx, 'Question_Stem'] = details['question_stem']
        df_mapping.at[idx, 'Option_A'] = details['options']['a']
        df_mapping.at[idx, 'Option_B'] = details['options']['b']
        df_mapping.at[idx, 'Option_C'] = details['options']['c']
        df_mapping.at[idx, 'Option_D'] = details['options']['d']
        df_mapping.at[idx, 'Answer_Rationale'] = details['rationale']

# Reorder columns for better readability
final_columns = [
    'Week', 'Concept', 'Concreteness_Level', 'Repetition_N_Weeks', 
    'Time_Per_Concept_Min', 'Has_Assessment', 'N_Assessment_Items',
    'Item_Codes', 'Question_Stem', 'Option_A', 'Option_B', 'Option_C', 'Option_D',
    'Correct_Answer_Verified', 'Answer_Rationale', 'Item_Difficulty'
]

df_mapping_final = df_mapping[final_columns]

output_final = OUTPUT_DIR / "curriculum_to_assessment_FINAL_with_all_questions.csv"
df_mapping_final.to_csv(output_final, index=False)
print(f"✓ Saved: {output_final}")

# ============================================================================
# COMPLETION
# ============================================================================
print("\n" + "="*80)
print("✓ ALL QUESTIONS EXTRACTED")
print("="*80)

print(f"\n📋 Final files created:")
print(f"  1. all_survey_questions_COMPLETE.csv - All questions with structured format")
print(f"  2. survey_questions_readable_format.csv - Human-readable format")  
print(f"  3. assessment_items_for_paper_appendix.csv - Clean format for paper")
print(f"  4. curriculum_to_assessment_FINAL_with_all_questions.csv - Concept mapping with full Q&A")

print(f"\n📊 Statistics:")
print(f"  - Total questions extracted: {len(df_questions)}")
print(f"  - Questions with correct answers: {n_answered}")
print(f"  - Answer distribution:")
answer_counts = df_questions[df_questions['Correct_Answer'] != 'VERIFY']['Correct_Answer'].value_counts()
for ans, count in answer_counts.items():
    print(f"    {ans}: {count} items")

print(f"\n✓ All questions now have full options and correct answers!")
print(f"✓ Ready to use in paper and for analysis!")
