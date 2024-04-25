from mpyc import statistics
from mpyc.runtime import mpc
import numpy as np

async def main(dataset_x, dataset_y):
    # convert numpy arrays to python lists
    dataset_x_list = dataset_x.tolist()
    dataset_y_list = dataset_y.tolist()

    secnum = mpc.SecFxp() # secnum = "secure number", using SecFxp() to create a secure number
    print('Using secure FXP (x):', secnum) # test that it is using a secure fixed point number
    dataset_x_secfxp = list(map(secnum, dataset_x_list)) # mapping the secure number to the python list -> makes a list of secure numbers

    secnum1 = mpc.SecFxp()
    print('Using secure FXP (y):', secnum1)
    dataset_y_secfxp = list(map(secnum1, dataset_y_list))


    # compute the correlation coefficient using mpyc's correlation function 
    correlation_coefficient = statistics.correlation(dataset_x_secfxp, dataset_y_secfxp)

    # reveal the result
    correlation_coefficient = await mpc.output(correlation_coefficient)
    print("Correlation Coefficient:", correlation_coefficient) #  example correlation coefficient should be 1.0 (since it has a direct 2x relationship)

# Run the MPC protocol
if __name__ == '__main__':
    dataset_x = np.array([1, 2, 3, 4, 5])  # example
    dataset_y = np.array([2, 4, 6, 8, 10])
    mpc.run(main(dataset_x, dataset_y))
