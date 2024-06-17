import pandas as pd

data = pd.read_csv("udemy/pandas/data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())