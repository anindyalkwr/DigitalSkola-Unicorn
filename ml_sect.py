import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Function to preprocess the data and encode categorical variables
def preprocess_data(data):
    data["Gender"] = data["Gender"].replace({'Male': 0, 'Female': 1, 'Other': 2}).astype(int)
    data["self_employed"] = data["self_employed"].replace({'Yes': 1, 'No': 0}).astype(int)
    data["family_history"] = data["family_history"].replace({'Yes': 1, 'No': 0}).astype(int)
    data["work_interfere"] = data["work_interfere"].replace({'Never': 0, 'Rarely': 1, 'Sometimes': 2, 'Often': 3}).astype(int)
    data["remote_work"] = data["remote_work"].replace({'Yes': 1, 'No': 0}).astype(int)
    return data

# Load the pre-trained machine learning model
def load_model(ml_model):
    if ml_model == 'Linear Regression':
        return joblib.load('lr_classifier')
    elif ml_model == 'Decision Tree':
        return joblib.load('dt_classifier')
    else:
        return joblib.load('rf_classifier')

def ml_section():
    st.header("Machine Learning Section")
    # Add your machine learning content here

    with st.expander("Modeling and Evaluation"):
        st.write(
            "In this section, we will briefly explain the modeling process and evaluation for our machine learning model.\n"
            "We used a Linear Regression classifier to predict whether mental health treatment is needed or not based on the input data.\n"
            "Linear Regression is a simple and interpretable model that works well when the relationship between the target variable\n"
            "and the features is approximately linear. It helps us understand how each input feature contributes to the prediction.\n"
            "For this particular problem, it allows us to make a binary prediction, indicating whether treatment is required or not.\n"
            "After training the model on a labeled dataset, we evaluated its performance using metrics such as accuracy, precision,\n"
            "recall, and F1-score to ensure its effectiveness in making predictions."
        )

    st.subheader('Mental Health Treatment Prediction')
    st.write('Enter the following information:')
    
    # Input fields
    age = st.number_input('Age', min_value=18, max_value=100, value=30)
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
    family_history = st.selectbox('Family History of Mental Illness', ['Yes', 'No'])
    work_interfere = st.selectbox('Mental Illness Interferes with Work', ['Never', 'Rarely', 'Sometimes', 'Often'])
    remote_work = st.selectbox('Remote Work', ['Yes', 'No'])
    ml_model = st.selectbox('Machine Learning Model', ['Linear Regression', 'Decision Tree', 'Random Forest'])
    
    # Convert input to a DataFrame
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'self_employed': [self_employed],
        'family_history': [family_history],
        'work_interfere': [work_interfere],
        'remote_work': [remote_work]
    })
    
    # Preprocess the input data
    input_data_encoded = preprocess_data(input_data)

    model = load_model(ml_model)
    
    # Make predictions
    prediction = model.predict(input_data_encoded)
    prediction_proba = model.predict_proba(input_data_encoded)[:, 1]  # Probability of positive class (treatment needed)
    prediction_text = "Mental health treatment is needed." if prediction[0] == 1 else "Mental health treatment is not needed."

    # Display the prediction
    st.subheader('Prediction:')
    st.write(prediction_text)

    # Improve prediction_proba text
    st.subheader('Prediction Probability:')
    if prediction[0] == 1:
        st.write(f"There is a {prediction_proba[0]*100:.2f}% probability that mental health treatment is needed.")
    else:
        st.write(f"There is a {prediction_proba[0]*100:.2f}% probability that mental health treatment is not needed.")


if __name__ == "__main__":
    ml_section()