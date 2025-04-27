import pandas as pd

#load the csv file
df = pd.read_csv("movies_cleaned.csv", low_memory=False) #Prevents DtypeWarning

#display the first 5 rows
print(df.columns)
