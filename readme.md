# Learning Style Recommender

This is a Streamlit-based machine learning app that recommends a user's preferred learning style based on a short questionnaire inspired by the VARK model (Visual, Auditory, Reading/Writing, Kinesthetic). You can learn a little more about VARK here: https://www.verywellmind.com/vark-learning-styles-2795156 

## Features

- 12-question interactive form
- Predicts learning style using a trained Decision Tree classifier
- Built with realistic synthetic data
- Deployed with Streamlit Cloud 

## Notes

This app uses a simple decision tree model trained on synthetic data.  
Typically, we would optimize this model using techniques like hyperparameter tuning (e.g., depth selection) and cross-validation or test/train splitting.

However, because this is a prototype built with synthetic, highly structured data and is designed for demonstration purposes only at this point, I’ve opted for a simpler model to prioritize clarity, speed, and usability. 


## Try It Out

[Click here to open the app] ..link

## To Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/learning-style-recommender.git
   cd learning-style-recommender

2. Install dependencies using pip:
    ```bash 
    pip install -r requirements.txt

3. Create synthetic data:
    ```bash
    python generate_synthetic_data.py

4. Launch app:
    ```bash
    streamlit run app.py
    
    
# Credits

Author: Mackenzie Bristow as part of a master's project for 
Course Title: Ethics in AI
Course Number: COSC 643
Topic: Ethics in Personalized Education
