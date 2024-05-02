from mpyc import statistics
from mpyc.runtime import mpc
import pandas as pd

async def main(dataset_x, dataset_y):

    secnum = mpc.SecFxp()
    dataset_x_secfxp = list(map(secnum, dataset_x))
    dataset_y_secfxp = list(map(secnum, dataset_y))

    correlation_coefficient = statistics.correlation(dataset_x_secfxp, dataset_y_secfxp)

    correlation_coefficient = await mpc.output(correlation_coefficient)
    print("Correlation Coefficient:", correlation_coefficient) 

if __name__ == '__main__':

    df = pd.read_csv('sampledata.csv')

    bin_col = ['Sex', 'Age', 'Patient Type', 'Fever', 'Coughing', 'Loss of Taste', 'Diabetes'] 
    for col in bin_col:
        df[col] = pd.to_numeric(df[col]).astype(int)

    var1 = df['Diabetes'].tolist()
    var2 = df['Fever'].tolist()

    mpc.run(main(var1, var2))
