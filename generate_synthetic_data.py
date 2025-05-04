#!/usr/bin/env python3

import numpy as np
import pandas as pd
import os

# Set random seed
np.random.seed(1)

# Learning Styles
styles = ['Visual', 'Auditory', 'Reading/Writing', 'Kinesthetic']

# Number of student responses
num_students = 500

# Function to generate form responses
def generate_responses(learning_style=None):
    responses = {}

    for style in styles:
        for question_number in range(1, 4):
            key = f'{style}_Q{question_number}'
            if learning_style == style:
                # Mostly higher scores with some moderate variation for preferred style
                # 10% chance they'll give a 3 (neutral), 40% chance of a 4, 50% chance of a 5
                # Usually strongly agrees with questions related to their preferred style
                responses[key] = np.random.choice([3, 4, 5], p=[0.1, 0.4, 0.5])
            elif learning_style is None:
                # For mixed-preference students, doesn’t have a strong single preference
                # More moderate or balanced scores across styles, less predictable behavior
                responses[key] = np.random.choice([2, 3, 4], p=[0.3, 0.5, 0.2])
            else:
                # More random variation for non-preferred styles
                # Mostly low agreement (scores of 1 or 2), some light interest (3).
                responses[key] = np.random.choice([1, 2, 3], p=[0.4, 0.4, 0.2])

    # Determine label
    if learning_style is not None:
        responses['Preferred_Style'] = learning_style
    else:
        responses['Preferred_Style'] = 'Mixed'

    return responses

# Create dataset
data = []

# Add clear student results 0.2 * 4 styles = 0.8 (80%)
for style in styles:
    for _ in range(int(num_students * 0.2)):
        data.append(generate_responses(style))

# Add mixed (ambiguous) student results (20%)
for _ in range(int(num_students * 0.2)):
    data.append(generate_responses(learning_style=None))

# Use Pandas to create DataFrame
df_students = pd.DataFrame(data)

# Shuffle rows
df_students = df_students.sample(frac=1, random_state=1).reset_index(drop=True)

output_file = 'synthetic_learning_styles.csv'

# Export dataset to CSV 
df_students.to_csv(output_file, index=False)

# Print success or failure message
if os.path.exists(output_file):
    print(f"File has SUCCESSFULLY been exported '{output_file}'.")
else:
    print(f"File has FAILED to be exported '{output_file}'.")