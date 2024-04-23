from mpyc.runtime import mpc
import numpy as np

async def compute_correlation_coefficient(xshares, yshares):
    # Compute the means of x and y
    mean_x = await mpc.mean(xshares)
    mean_y = await mpc.mean(yshares)

    # Compute the covariance of x and y
    cov_xy = await mpc.mean([(xshares[i] - mean_x) * (yshares[i] - mean_y) for i in range(len(xshares))])

    # Compute the standard deviation of x and y
    std_x = await mpc.sqrt(await mpc.mean([(xshares[i] - mean_x)**2 for i in range(len(xshares))]))
    std_y = await mpc.sqrt(await mpc.mean([(yshares[i] - mean_y)**2 for i in range(len(yshares))]))

    # Compute the correlation coefficient
    correlation_coefficient = cov_xy / (std_x * std_y)

    return correlation_coefficient

async def main(dataset_x, dataset_y):
    # Convert NumPy arrays to Python lists
    dataset_x_list = dataset_x.tolist()
    dataset_y_list = dataset_y.tolist()

    # Convert elements to integers
    dataset_x_list = [int(x) for x in dataset_x_list]
    dataset_y_list = [int(y) for y in dataset_y_list]

    # Each party splits its data into shares
    x_shares = [mpc.input(dataset_x_list[i]) for i in range(len(dataset_x_list))]
    y_shares = [mpc.input(dataset_y_list[i]) for i in range(len(dataset_y_list))]

    # Perform secure computation of the correlation coefficient
    result = await compute_correlation_coefficient(x_shares, y_shares)

    # Reveal the result
    correlation_coefficient = await mpc.output(result)
    print("Correlation Coefficient:", correlation_coefficient)

# Run the MPC protocol
if __name__ == '__main__':
    dataset_x = np.array([1, 2, 3, 4, 5]) # correlation coefficient should be 1.0 (perfect correlation since it has a direct 2x relationship)
    dataset_y = np.array([2, 4, 6, 8, 10])
    mpc.run(main(dataset_x, dataset_y))
