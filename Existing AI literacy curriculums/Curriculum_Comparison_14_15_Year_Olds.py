import pandas as pd
import numpy as np

# Create a comprehensive dataframe comparing AI literacy curriculums for 14/15 year olds
data = {
    'Curriculum': [
        'AI in My Life (15-16 year olds)',
        'Common Sense Media (Grades 6-12)',
        'Georgia AI4GA (High School)',
        'Berlin KI-Aufträge (Secondary School)',
        'ENARIS (Secondary Education)',
        'aiEDU (Grades 6-12)',
        'AI4K12 (K-12)',
        'MIT AI Ethics (Advanced High School)',
        'Duke Learning Innovation (Higher Ed)',
        'AI Pedagogy Project (Higher Ed)',
        'AI Adapt (General Public)'
    ],
    
    'Target_Age_Range': [
        '15-16 years',
        '11-18 years (Grades 6-12)',
        '14-18 years (High School)',
        '14-18 years (Secondary)',
        '14-18 years (Secondary)',
        '11-18 years (Grades 6-12)',
        '5-18 years (K-12)',
        '16-18 years (Advanced HS)',
        '18+ years (Higher Ed)',
        '18+ years (Higher Ed)',
        'All ages'
    ],
    
    'Suitability_14_15': [
        'Excellent',
        'Good',
        'Excellent',
        'Excellent',
        'Excellent',
        'Good',
        'Moderate',
        'Limited',
        'Not Suitable',
        'Not Suitable',
        'Moderate'
    ],
    
    'Duration_Hours': [
        'Workshop format (2-4 hours)',
        '1-2 hours per lesson',
        'Full semester course',
        'Mission-based (flexible)',
        'Modular (flexible)',
        'Flexible modules',
        'Age-appropriate segments',
        'Full semester',
        'Full semester',
        'Flexible',
        'Modular'
    ],
    
    'Format': [
        'Workshop',
        'Lesson slides',
        'Comprehensive curriculum',
        'Interactive missions',
        'Web platform + exercises',
        'Project-based modules',
        'Educational materials',
        'Ethics curriculum',
        'Critical analysis',
        'Pedagogical resources',
        'Modular themes'
    ],
    
    'Key_Topics': [
        'AI Ethics, Privacy, Real-world applications',
        'What is AI, Digital literacy',
        '5 Big Ideas, Autonomous systems, Language processing, Decision making',
        'AI tool exploration, Character conversations, Practical testing',
        'AI Basics, Computer Vision, NLP, Ethics, Neural Networks',
        'AI readiness, Project-based learning, Deepfakes, ChatGPT',
        '5 Big Ideas, Intelligent assistants',
        'Algorithmic bias, Ethics matrices, Machine learning',
        'Critical questions about AI impact',
        'Socratic questioning, AI journalism',
        'AI and careers, Ethics, Future of work'
    ],
    
    'Hands_On_Activities': [
        'Yes - Workshop activities',
        'Limited - Discussion based',
        'Yes - Extensive projects',
        'Yes - Tool exploration',
        'Yes - Interactive exercises',
        'Yes - Project dashboards',
        'Yes - Activity guides',
        'Yes - Ethical analysis',
        'No - Discussion based',
        'Yes - Interactive questioning',
        'Yes - Practical applications'
    ],
    
    'Ethics_Focus': [
        'High',
        'Medium',
        'Medium',
        'Low',
        'High',
        'High',
        'Low',
        'Very High',
        'Very High',
        'High',
        'High'
    ],
    
    'Technical_Depth': [
        'Medium',
        'Low',
        'High',
        'Medium',
        'High',
        'Medium',
        'Low-Medium',
        'High',
        'Medium',
        'Low',
        'Medium'
    ],
    
    'Language_Options': [
        'English',
        'English',
        'English',
        'German (English translation)',
        'German, English, Hungarian',
        'English',
        'English',
        'English',
        'English',
        'English',
        'English'
    ],
    
    'Assessment_Methods': [
        'Workshop evaluation',
        'Discussion participation',
        'Projects, case studies',
        'Mission completion',
        'Exercise completion',
        'Project evaluation',
        'Activity completion',
        'Ethical analysis',
        'Critical analysis',
        'Discussion participation',
        'Module completion'
    ],
    
    'Teacher_Support': [
        'Workshop materials',
        'Lesson plans',
        'Comprehensive guides',
        'Mission instructions',
        'Teacher resources',
        'Flex plans, guides',
        'Educational materials',
        'Curriculum materials',
        'Instructor guides',
        'Pedagogical resources',
        'Resource materials'
    ],
    
    'Real_World_Applications': [
        'High',
        'Medium',
        'High',
        'High',
        'High',
        'High',
        'Medium',
        'Medium',
        'High',
        'Medium',
        'High'
    ],
    
    'Student_Engagement': [
        'High',
        'Medium',
        'High',
        'Very High',
        'High',
        'High',
        'Medium',
        'Medium',
        'Low',
        'Medium',
        'Medium'
    ],
    
    'Accessibility': [
        'Medium',
        'High',
        'Medium',
        'High',
        'High',
        'High',
        'High',
        'Low',
        'Low',
        'Medium',
        'High'
    ],
    
    'Cost': [
        'Unknown',
        'Free',
        'Free',
        'Free',
        'Free',
        'Free',
        'Free',
        'Free',
        'Free',
        'Free',
        'Unknown'
    ],
    
    'Strengths': [
        'Age-specific, ethics focus, practical',
        'Simple, accessible, media literacy',
        'Comprehensive, hands-on, structured',
        'Interactive, engaging, practical',
        'Technical depth, multilingual, modular',
        'Project-based, comprehensive, flexible',
        'Age-appropriate, foundational',
        'Ethics focus, critical thinking',
        'Critical analysis, questioning',
        'Pedagogical approach, questioning',
        'Career-focused, practical'
    ],
    
    'Weaknesses': [
        'Limited scope, single workshop',
        'Basic level, limited depth',
        'Complex, requires technical background',
        'German-focused, limited English',
        'Technical complexity',
        'May be overwhelming',
        'Too basic for 14-15 year olds',
        'Too advanced for most 14-15 year olds',
        'Not age-appropriate',
        'Not age-appropriate',
        'Not age-specific'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)


# Filter for curriculums most suitable for 14-15 year olds
suitable_curriculums = df[df['Suitability_14_15'].isin(['Excellent', 'Good'])].copy()

# Add a suitability score for ranking
suitability_scores = {'Excellent': 5, 'Good': 4, 'Moderate': 3, 'Limited': 2, 'Not Suitable': 1}
df['Suitability_Score'] = df['Suitability_14_15'].map(suitability_scores)

# Sort by suitability score
#df_sorted = df.sort_values('Suitability_Score', ascending=False)

print("=== AI LITERACY CURRICULUMS COMPARISON FOR 14-15 YEAR OLDS ===\n")
print(f"Total curriculums analyzed: {len(df)}")
print(f"Most suitable for 14-15 year olds: {len(suitable_curriculums)}")
print("\n" + "="*80)

# Display the most suitable curriculums
print("\nTOP CURRICULUMS FOR 14-15 YEAR OLDS:")
print("="*50)
for idx, row in suitable_curriculums.iterrows():
    print(f"\n{row['Curriculum']}")
    print(f"  Suitability: {row['Suitability_14_15']}")
    print(f"  Format: {row['Format']}")
    print(f"  Key Topics: {row['Key_Topics']}")
    print(f"  Strengths: {row['Strengths']}")

# Create summary statistics
print("\n" + "="*80)
print("SUMMARY STATISTICS")
print("="*80)

# Count by suitability
suitability_counts = df['Suitability_14_15'].value_counts()
print(f"\nSuitability Distribution:")
for level, count in suitability_counts.items():
    print(f"  {level}: {count}")

# Count by format
format_counts = df['Format'].value_counts()
print(f"\nFormat Distribution:")
for format_type, count in format_counts.items():
    print(f"  {format_type}: {count}")

# Count by ethics focus
ethics_counts = df['Ethics_Focus'].value_counts()
print(f"\nEthics Focus Distribution:")
for level, count in ethics_counts.items():
    print(f"  {level}: {count}")

# Count by hands-on activities
hands_on_counts = df['Hands_On_Activities'].value_counts()
print(f"\nHands-on Activities:")
for level, count in hands_on_counts.items():
    print(f"  {level}: {count}")

# Language diversity
language_counts = df['Language_Options'].value_counts()
print(f"\nLanguage Options:")
for lang, count in language_counts.items():
    print(f"  {lang}: {count}")

# Save to CSV
df.to_csv('/Users/olga/Olga\'s workspace/ETHZ SBS/Marty project/Existing AI literacy curriculums/Curriculum_Comparison_14_15_Year_Olds.csv', index=False)
print(f"\nDataFrame saved to CSV file.")

# Display the full dataframe
print("\n" + "="*80)
print("FULL CURRICULUM COMPARISON DATAFRAME")
print("="*80)
print(df[['Curriculum', 'Target_Age_Range', 'Suitability_14_15', 'Format', 'Key_Topics', 'Hands_On_Activities', 'Ethics_Focus']].to_string(index=False))

df.to_markdown('Curriculum_Comparison_14_15_Year_Olds.md')