from mpyc import statistics
from mpyc.runtime import mpc
import pandas as pd

async def main(dataset_x, dataset_y):

    secnum = mpc.SecFxp() # secnum = "secure number", using SecFxp() to create a secure number
    dataset_x_secfxp = list(map(secnum, dataset_x)) # mapping the secure number to the python list -> makes a list of secure numbers

    secnum1 = mpc.SecFxp()
    dataset_y_secfxp = list(map(secnum1, dataset_y))


    # compute the correlation coefficient using mpyc's correlation function 
    correlation_coefficient = statistics.correlation(dataset_x_secfxp, dataset_y_secfxp)

    # reveal the result
    correlation_coefficient = await mpc.output(correlation_coefficient)
    print("Correlation Coefficient:", correlation_coefficient) 

# Run the MPC protocol
if __name__ == '__main__':

    df = pd.read_csv('sampledata.csv')

    bin_col = ['Sex', 'Age', 'Patient Type', 'Fever', 'Coughing', 'Loss of Taste', 'Diabetes'] 
    for col in bin_col:
        df[col] = pd.to_numeric(df[col]).astype(int)

    var1 = df['Diabetes'].tolist()
    var2 = df['Fever'].tolist()

    mpc.run(main(var1, var2))
