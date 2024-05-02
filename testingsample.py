import pandas as pd

df = pd.read_csv('sampledata2.csv')
bin_col = ['Age', 'Sex', 'Fever', 'Coughing', 'Loss of Taste', 'Diabetes']

for col in bin_col:
    df[col] = pd.to_numeric(df[col]).astype(int)

age_values = df['Age'].tolist()

fever_values = df['Fever'].tolist()

print(df.dtypes)