from mpyc import statistics
from mpyc.runtime import mpc
import numpy as np

async def main(dataset_x, dataset_y):
    # Convert NumPy arrays to Python lists
    dataset_x_list = dataset_x.tolist()
    dataset_y_list = dataset_y.tolist()

    # Convert elements to secure integers
    dataset_x_secint = [mpc.SecInt(x) for x in dataset_x_list]
    dataset_y_secint = [mpc.SecInt(y) for y in dataset_y_list]

    # Compute the correlation coefficient using mpyc's correlation function (passing secure arrays directly into correlation)
    correlation_coefficient = await mpc.correlation(dataset_x_secint, dataset_y_secint)

    # Reveal the result
    correlation_coefficient = await mpc.output(correlation_coefficient)
    print("Correlation Coefficient:", correlation_coefficient)

# Run the MPC protocol
if __name__ == '__main__':
    dataset_x = np.array([1, 2, 3, 4, 5]) # correlation coefficient should be 1.0 (perfect correlation since it has a direct 2x relationship)
    dataset_y = np.array([2, 4, 6, 8, 10])
    mpc.run(main(dataset_x, dataset_y))
