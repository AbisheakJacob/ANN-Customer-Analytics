import streamlit as st
import pandas as pd
#from streamlit_pandas_profiling import st_profile_report
#from ydata_profiling import ProfileReport


# Set page configuration to wide layout
st.set_page_config(page_title="About", layout="wide")

st.title("Exploratory Data Analysis")

st.subheader("Dataset")

# reading the data
data = pd.read_csv("data/Churn_Modelling.csv")

# drop the unnecessary coloumns
data.drop(columns=['RowNumber', 'CustomerId', 'name'], inplace=True)

# create the profile report of the dataframe
#profile = ProfileReport(data, title="Profiling Report", explorative=True)

st.dataframe(data)

#st_profile_report(profile)
