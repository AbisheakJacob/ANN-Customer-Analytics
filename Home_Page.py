import streamlit as st

st.set_page_config(
    page_title="ANN Customer Churn Prediction",
    page_icon="🗒️",
)

st.header("Customer Churn Prediction in Banks using Artificial Neural Networks")

st.sidebar.success("Select a Page from above.")

st.markdown(
    """

The project involves predicting customer churn within the banking industry using deep learning models. The focus centers on harnessing the capabilities of Artificial Neural Networks (ANN) to increase accuracy. K-fold cross-validation and Grid search cross-validation techniques are employed to achieve higher levels of accuracy.

**Accuracy of the Model: 86.85%**
---
### Description of the Data
|Variable |	Description|	Value|
|---|---|---|
|Customer ID	|Unique identifier for the customer holding the account|	Positive real number|
|Age	|Demographic variable	|Customer’s age in years (Min. 18 to Max. 92)|
|Gender|	Demographic variable|	Male, Female|
|Geography|	Demographic variable|	Chennai, Mumbai, Bangalore|
|Credit score	|Credit variable|	Person’s credibility (Min. 350 to Max. 850)|
|Tenure|	Timespan|	Person’s relationship with the bank (Min. 0 to Max. 10)|
|Balance|	Credit variable	|Total revolving balance|
|Number of Products|	Product variable	|Number of products held by customer|
|Has Credit Card|	Product variable|	Has credit card then 1 else 0|
|Is Active Member|	Internal event|	Is active member then 1 else 0|
|Estimated Salary	|Demographic variable	|Annual Income of the account holder (Min. 11.58 Rs. To Max. 199,992.48 Rs.)|
|Exited|	Internal event|	If the account is closed, then 1 else 0|
---

"""
)