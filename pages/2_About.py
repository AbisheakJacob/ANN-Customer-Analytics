import streamlit as st
from streamlit.components.v1 import html
import pandas as pd


# Set page configuration to wide layout
st.set_page_config(page_title="About", layout="wide")

st.title("Exploratory Data Analysis")

st.subheader("Dataset")

# reading the data
data = pd.read_csv("data/Churn_Modelling.csv")

# drop the unnecessary coloumns
data.drop(columns=['RowNumber', 'CustomerId', 'name'], inplace=True)

st.dataframe(data)

# Display the HTML file in the Streamlit app
with open("profile_report.html", "r", encoding="utf-8") as file:
    report_html = file.read()

st.subheader("Profile Report")
st.write("This profile report was created using ydata profiling.")
html(report_html, width=1000, height=800, scrolling=True)