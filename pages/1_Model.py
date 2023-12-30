import streamlit as st 
import pandas as pd
import numpy as np
import joblib
import os

from warnings import filterwarnings
filterwarnings("ignore")
    
# set the page name and other configurations
st.set_page_config(
    page_title='Home Page',
    initial_sidebar_state='expanded'
)

st.title("Churn Rate Prediction Using ANN")

st.markdown('''
            The model uses Artificial Neural Network to predict the churn rate 
            of customers in banks.
            ### Model Parameters
            - **epochs:** 500
            - **optimizer:** rmsprop
            - **loss:** binary_crossentropy
            - **batch size:** 25
            ---
            ### Model Metrics
            ##### **Accuracy:** 86.85 %
            ---
            ''')

# input the features to predict
#cust_id = st.text_input("Enter the Id of the Customer: (optional) ")
#name = st.text_input("Enter the Name of the Customer: (optional) ")
cred = st.number_input("Enter the Credit Score of the Customer: ", min_value=0, value=None, step=1)
geo = st.selectbox("Enter the City of the Customer: ", ['Chennai', 'Bangalore', 'Mumbai'], index=None)
geo = {'Chennai': [1, 0], 'Bangalore': [0, 0]}.get(geo, [0,1])
gender = st.selectbox("Enter the Gender of the Customer: ", ['Male', 'Female'], index=None)
gender = {'Male': 1, 'Female': 0}.get(gender, 0)
age = st.number_input("Enter the Age of the Customer: ", min_value=15, max_value=80, value=None, step=1)
tenure = st.number_input("Enter the Tenure of the Customer: ", min_value=0, max_value=10, value=None, step=1)
bal = st.number_input("Enter the Account Balance of the Customer: ", min_value=0, value=None, step=1)
num_products = st.number_input("Enter the Number of Products the Customer had subscribed: ", min_value=0, max_value=10, value=None, step=1)
cred_card = st.selectbox("Does the Customer have a Credit Card? ", ['Yes', 'No'], index=None)
cred_card = {'Yes': 1, 'No': 0}.get(cred_card, 0)
active_mem = st.selectbox("Is the customer an Active Member? ", ['Yes', 'No'], index=None)
active_mem = {'Yes': 1, 'No': 0}.get(active_mem, 0)
est_salary = st.number_input("What is the estimated salary of the Customer: ", min_value=0, value=None, step=1)

#personal_info = [cust_id, name]
stat_info = geo + [cred, gender, age, tenure, bal, num_products, cred_card, active_mem, est_salary]

# get absolute filepath
#file_path_s = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "model", "scaler_instance.joblib")
#file_path_c = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "model", "classifier.joblib")


# parent_dir = os.path.dirname(current_dir)
scaler = joblib.load("scaler_instance.joblib")
classifier = joblib.load("classifier.joblib")

pred = classifier.predict(scaler.transform(np.array([stat_info])))
new_pred = round(float(pred[0][0] * 100), 2)

button  = st.button("Predict")
if button:
    if new_pred < 50:
        st.success(f"The chances of the customer leaving is {new_pred} %")
    else:
        st.error(f"The chances of the customer leaving is {new_pred} %")


