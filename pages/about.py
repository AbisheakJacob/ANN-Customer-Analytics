import sys
sys.path.insert(0, '../eda/profiler.py')

import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from eda.profiler import profile_report

def about():
    # Set page configuration to wide layout
    st.set_page_config(layout="wide")

    st.title("Exploratory Data Analysis")

    # call the profile function to get the profile of the data
    data, profile = profile_report()
    
    st.dataframe(data)

    st_profile_report(profile)


if __name__ == "__main__":
    about()