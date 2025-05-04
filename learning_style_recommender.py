#!/usr/bin/env python3

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score



# Load the generated dataset
df_learning_styles = pd.read_csv("synthetic_learning_styles.csv")

# Split data
X = df_learning_styles.drop("Preferred_Style", axis=1)
y = df_learning_styles["Preferred_Style"]

# Encode target
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=1)


# Initialize and Train classifier
clf = DecisionTreeClassifier(random_state=1)
clf.fit(X_train, y_train)


# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\n\nClassification Report:\n", classification_report(y_test, y_pred, target_names=encoder.classes_))
print("\n\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))


# Questionnaire structure
styles = ['Visual', 'Auditory', 'Reading/Writing', 'Kinesthetic']
questions = {
    "Visual": [
        "I understand topics better when there are diagrams or visual aids.",
        "Videos and visual demonstrations help me remember information.",
        "I prefer to use colored pens or highlighters when studying notes."
    ],
    "Auditory": [
        "I learn effectively from lectures or spoken explanations.",
        "I prefer listening to recorded material rather than reading.",
        "Discussing topics aloud helps me process new information."
    ],
    "Reading/Writing": [
        "I remember information best when I rewrite my notes.",
        "I prefer textbooks and written handouts over videos or audio.",
        "Writing summaries helps me understand complex topics better."
    ],
    "Kinesthetic": [
        "Hands-on activities help me grasp concepts quickly.",
        "I prefer demonstrations and practical examples over theoretical explanations.",
        "I often walk around or physically engage with materials when I study."
    ]
}

st.title("Learning Style Recommender")
st.markdown("Rate each statement from **1 (Strongly Disagree)** to **5 (Strongly Agree)**.")

user_input = {}

# Collect user input
for style in styles:
    st.subheader(style)
    for i, question in enumerate(questions[style], 1):
        key = f"{style}_Q{i}"
        user_input[key] = st.slider(question, 1, 5, 3)

# Predict on submit
if st.button("Submit"):
    user_df = pd.DataFrame([user_input])
    prediction = clf.predict(user_df)
    predicted_style = encoder.inverse_transform(prediction)[0]
    st.success(f"Your predicted learning style is: **{predicted_style}**")

# Citation
st.markdown("---", unsafe_allow_html=True)

st.markdown(
    "<div style='font-size: 0.85em; color: gray;'>"
    "This questionnaire is inspired by the VARK model of learning preferences.<br>"
    "Fleming, N. D. (2023). <i>The VARK questionnaire: How do I learn best?</i> VARK Learn Limited. "
    "<a href='https://vark-learn.com/the-vark-questionnaire/' target='_blank'>vark-learn.com</a>"
    "</div>",
    unsafe_allow_html=True
)

