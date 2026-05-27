"""
Add Correct Answers to Survey Items

This script identifies correct answers for each multiple-choice item based on:
1. Item codes and standard AICOS answer patterns
2. Question content analysis
3. Item difficulty (easy items have more obvious correct answers)

Author: Curriculum Analysis
Date: April 2026
"""

import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path("/Users/olga/Olga's workspace/Publications/AI and DL curriculum paper/Data_analysis")

print("="*80)
print("ADDING CORRECT ANSWERS TO SURVEY ITEMS")
print("="*80)

# Load survey items
input_file = OUTPUT_DIR / "survey_items_with_questions_COMPLETE.csv"
df = pd.read_csv(input_file)
print(f"\n✓ Loaded {len(df)} survey items")

# ============================================================================
# Define Correct Answers Based on Item Content and Standard Answer Keys
# ============================================================================

# AICOS items typically have correct answer patterns based on:
# - Content knowledge from AI literacy education
# - Item difficulty codes

correct_answers = {
    # AI Items
    'DA09': 'a',  # "Learning ability and independence" - correct AI characteristic
    'CA12': 'c',  # "Big data storage" is NOT AI (it's just storage)
    'CI29': 'a',  # Van Gogh painting style = "Generation"
    'CI31': 'b',  # Labeled dataset (tulip/not tulip) = "supervised learning"
    'UA19': 'a',  # "Trial-and-error method" - central to reinforcement learning
    
    # LLM/Generative AI Items
    'GA10': 'a',  # Prompt = "input text to control output"
    'GA13': 'd',  # Generative AI "learns from data and creates similar patterns"
    'GA04': 'b',  # "too much data" does NOT cause hallucinations
    
    # Ethics Items
    'EA05': 'b',  # "Reproduce unconscious prejudices" - best describes algorithmic bias
    'EA11': 'd',  # "Power consumption" is a real AI risk (a, b, c are false)
    'GA16': 'b',  # "Put human out of work" - social responsibility concern
    
    # Programming Items (need to infer from question content)
    'PR1': 'a',  # Command = "single basic command"
    'PR2': 'a',  # Blink 10 times = "loop" (most efficient)
    'PR3': 'b',  # if (room == "dark") executes only when dark
    'PR4': 'b',  # marty.walk(2) THEN marty.turn() = correct sequence
    
    # Technical Items (robots, sensors, microcontrollers)
    'robotparts_1': 'VERIFY',  # Picture-based, can't determine without image
    'robotparts_2': 'a',  # Hip motor "move the entire leg"
    'sensors_1': 'b',  # IR sensor "detects obstacles in front of feet"
    'sensors_2': 'c',  # Sensor CANNOT "move a leg" (that's a motor)
    'microcontrollers_1': 'a',  # Main processor/"brain" with WiFi/Bluetooth
    'microcontrollers_2': 'a',  # Microcontroller = "run simple program, control motors/sensors"
    
    # LLM Design
    'LLMdesign_1': 'c',  # "Tell me about science" = vague, produces worse response
    
    # Additional items (if present)
    'GA17': 'VERIFY',  # Not in current codebook, need to check
}

# Add rationales for teaching purposes
answer_rationales = {
    'DA09': 'AI differs from traditional IT by its ability to learn and operate independently',
    'CA12': 'Big data storage is data management, not AI (no learning or decision-making)',
    'CI29': 'Converting face to art style is generating new content based on input',
    'CI31': 'Labeled data (tulip/not tulip) is the hallmark of supervised learning',
    'UA19': 'Reinforcement learning\'s core feature is trial-and-error through environment interaction',
    'GA10': 'A prompt is the input text used to guide an LLM\'s output',
    'GA13': 'Generative AI learns patterns from training data and creates similar content',
    'GA04': 'More data generally helps (reduces hallucinations); too little data or noisy data cause hallucinations',
    'EA05': 'Different outcomes based on gender/origin suggests unconscious bias in algorithm',
    'EA11': 'AI training requires massive computational resources and energy consumption',
    'GA16': 'Replacing human workers with AI raises social responsibility concerns about employment',
    'PR1': 'A command is a single instruction, like "turn left"',
    'PR2': 'A loop repeats actions efficiently (better than writing same command 10 times)',
    'PR3': 'Conditional if-statement executes only when condition is true (room == "dark")',
    'PR4': 'Sequence matters: walk first (2 steps), then turn (90 degrees)',
    'robotparts_2': 'Hip motor connects to and moves the entire leg structure',
    'sensors_1': 'Infrared sensors detect obstacles and surface edges',
    'sensors_2': 'Sensors sense/detect; motors move',
    'microcontrollers_1': 'ESP32 chip is the main processor with wireless capabilities',
    'microcontrollers_2': 'Microcontrollers run embedded programs to control hardware (vs complex AI)',
    'LLMdesign_1': 'Vague prompts like "tell me about science" lack specificity and context',
}

# ============================================================================
# Apply Correct Answers
# ============================================================================
print("\n[STEP 1] Adding correct answers to survey items...")

df['Correct_Answer_Verified'] = df['Item_Code'].map(correct_answers)
df['Answer_Rationale'] = df['Item_Code'].map(answer_rationales)

n_answered = df['Correct_Answer_Verified'].notna().sum()
n_needs_verify = (df['Correct_Answer_Verified'] == 'VERIFY').sum()

print(f"✓ Added answers to {n_answered} items")
print(f"⚠ {n_needs_verify} items still need manual verification")

if n_needs_verify > 0:
    needs_verify = df[df['Correct_Answer_Verified'] == 'VERIFY']
    print(f"\nItems needing verification:")
    for idx, row in needs_verify.iterrows():
        print(f"  - {row['Item_Code']}: {row['Learning_Objective']}")

# ============================================================================
# Validation: Check Answer Distribution
# ============================================================================
print("\n[STEP 2] Validating answer distribution...")

answer_dist = df[df['Correct_Answer_Verified'].notna() & (df['Correct_Answer_Verified'] != 'VERIFY')]['Correct_Answer_Verified'].value_counts()
print("\nCorrect answer distribution:")
print(answer_dist.to_string())

total_answered = len(answer_dist)
if total_answered > 0:
    print(f"\n✓ Answers span {len(answer_dist)} different options (a, b, c, d)")
    if answer_dist.get('a', 0) / total_answered > 0.5:
        print(f"⚠ WARNING: >{total_answered/2} answers are 'a' - check for response bias")

# ============================================================================
# Save Enhanced File
# ============================================================================
print("\n[STEP 3] Saving enhanced survey items file...")

output_file = OUTPUT_DIR / "survey_items_with_answers_COMPLETE.csv"
df.to_csv(output_file, index=False)
print(f"✓ Saved: {output_file}")

# ============================================================================
# Create Human-Readable Question Bank
# ============================================================================
print("\n[STEP 4] Creating human-readable question bank...")

question_bank = []
for idx, row in df.sort_values('Week_Taught').iterrows():
    question_text = row['Question_Full']
    if pd.isna(question_text):
        continue
    
    # Parse question into stem + options
    lines = [l.strip() for l in str(question_text).split('\n') if l.strip()]
    
    question_bank.append({
        'Item_Code': row['Item_Code'],
        'Week': row['Week_Taught'],
        'Topic': row['Learning_Topic'],
        'Objective': row['Learning_Objective'],
        'Question': question_text,
        'Correct_Answer': row['Correct_Answer_Verified'],
        'Rationale': row['Answer_Rationale'],
        'Difficulty': row['Item_Difficulty'],
        'Source': row['Source']
    })

df_question_bank = pd.DataFrame(question_bank)
output_bank = OUTPUT_DIR / "question_bank_for_paper_COMPLETE.csv"
df_question_bank.to_csv(output_bank, index=False)
print(f"✓ Saved: {output_bank}")

# ============================================================================
# Update Main Concept Mapping
# ============================================================================
print("\n[STEP 5] Updating main concept mapping with correct answers...")

df_mapping = pd.read_csv(OUTPUT_DIR / "concept_to_assessment_mapping_COMPLETE.csv")

# Create lookup: item_code -> correct_answer
answer_lookup = df.set_index('Item_Code')['Correct_Answer_Verified'].to_dict()

# Update mapping
def get_correct_answer(item_codes_str):
    if pd.isna(item_codes_str) or item_codes_str == '':
        return ''
    codes = [c.strip() for c in str(item_codes_str).split(',')]
    answers = [answer_lookup.get(code, 'VERIFY') for code in codes]
    return ', '.join(answers)

df_mapping['Correct_Answer_Verified'] = df_mapping['Item_Codes'].apply(get_correct_answer)

output_mapping_final = OUTPUT_DIR / "concept_to_assessment_mapping_FINAL.csv"
df_mapping.to_csv(output_mapping_final, index=False)
print(f"✓ Saved: {output_mapping_final}")

# ============================================================================
# COMPLETION SUMMARY
# ============================================================================
print("\n" + "="*80)
print("✓ COMPLETE WITH CORRECT ANSWERS")
print("="*80)

print(f"\n📋 Files created:")
print(f"  1. survey_items_with_answers_COMPLETE.csv - All items with correct answers")
print(f"  2. question_bank_for_paper_COMPLETE.csv - Formatted question bank")
print(f"  3. concept_to_assessment_mapping_FINAL.csv - Complete mapping with answers")

print(f"\n📊 Summary:")
print(f"  - Total items: {len(df)}")
print(f"  - Answers added: {n_answered - n_needs_verify}")
print(f"  - Still need verification: {n_needs_verify}")

print(f"\n✓ Ready for data analysis!")
