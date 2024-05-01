import pandas as pd
import numpy as np

df = pd.read_csv('sampledata2.csv')

bin_col = ['Sex', 'Fever', 'Coughing', 'Loss of Taste', 'Diabetes'] # changing values to int

for col in bin_col:
    df[col] = pd.to_numeric(df[col]).astype(int)

sex_values = df['Age'].tolist()

fever_values = df['Fever'].tolist()

print(sex_array)
print(fever_array)

print(df.dtypes)