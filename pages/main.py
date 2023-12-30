import os

# determing the location of the csv file
filename = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "model", "classifier.joblib")

print(filename)