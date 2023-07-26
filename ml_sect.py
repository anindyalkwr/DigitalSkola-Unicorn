import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Function to preprocess the data and encode categorical variables
def preprocess_data(data):
    data["Gender"] = data["Gender"].replace({'Male': 0, 'Female': 1, 'Other': 2}).astype(int)
    data["work_interfere"] = data["work_interfere"].replace({'Never': 0, 'Rarely': 1, 'Sometimes': 2, 'Often': 3}).astype(int)
    data["family_history"] = data["family_history"].replace({'Yes': 1, 'No': 0}).astype(int)
    data["remote_work"] = data["remote_work"].replace({'Yes': 1, 'No': 0}).astype(int)
    data["tech_company"] = data["tech_company"].replace({'Yes': 1, 'No': 0}).astype(int)
    return data

# Load the pre-trained machine learning model
model = joblib.load('dt_classifier.pkl')

def ml_section():
    st.title("Machine Learning Section")
    # Add your machine learning content here
    st.title('Mental Health Treatment Prediction')
    st.write('Enter the following information:')
    
    # Input fields
    age = st.number_input('Age', min_value=18, max_value=100, value=30)
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    family_history = st.selectbox('Family History of Mental Illness', ['Yes', 'No'])
    work_interfere = st.selectbox('Mental Illness Interferes with Work', ['Never', 'Rarely', 'Sometimes', 'Often'])
    remote_work = st.selectbox('Remote Work', ['Yes', 'No'])
    tech_company = st.selectbox('Tech Company', ['Yes', 'No'])
    
    # Convert input to a DataFrame
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'family_history': [family_history],
        'work_interfere': [work_interfere],
        'remote_work': [remote_work],
        'tech_company': [tech_company]
    })
    
    # Preprocess the input data
    input_data_encoded = preprocess_data(input_data)
    
    # Make predictions
    prediction = model.predict(input_data_encoded)
    prediction_text = "Mental health treatment is needed." if prediction[0] == 1 else "Mental health treatment is not needed."
    
    # Display the prediction
    st.subheader('Prediction:')
    st.write(prediction_text)


if __name__ == "__main__":
    ml_section()