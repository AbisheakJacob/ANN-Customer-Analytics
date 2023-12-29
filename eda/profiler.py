# importing the packages
import pandas as pd
from ydata_profiling import ProfileReport
import os

def profile_report():

    current_directory = os.getcwd()

    # reading the data
    data = pd.read_csv(current_directory + "\\data\\Churn_Modelling.csv")

    # drop the unnecessary coloumns
    data.drop(columns=['RowNumber', 'CustomerId', 'name'], inplace=True)

    # create the profile report of the dataframe
    profile = ProfileReport(data, title="Profiling Report", explorative=True)

    return (data, profile)


