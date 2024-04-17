from mpyc.runtime import mpc
import numpy as np

async def compute_correlation_coefficient(x_shares, y_shares):
    # Compute the means of x and y
    mean_x = await mpc.mean(x_shares)
    mean_y = await mpc.mean(y_shares)

    # Compute the covariance of x and y
    cov_xy = await mpc.mean([(x_shares[i] - mean_x) * (y_shares[i] - mean_y) for i in range(len(x_shares))])

    # Compute the standard deviation of x and y
    std_x = await mpc.sqrt(await mpc.mean([(x_shares[i] - mean_x)**2 for i in range(len(x_shares))]))
    std_y = await mpc.sqrt(await mpc.mean([(y_shares[i] - mean_y)**2 for i in range(len(y_shares))]))

    # Compute the correlation coefficient
    correlation_coefficient = cov_xy / (std_x * std_y)

    return correlation_coefficient

async def main():
    # Simulated data - each party has its own dataset
    party_data_x = np.random.rand(100)
    party_data_y = np.random.rand(100)

    # Each party splits its data into shares
    x_shares = [mpc.input(party_data_x[i]) for i in range(len(party_data_x))]
    y_shares = [mpc.input(party_data_y[i]) for i in range(len(party_data_y))]

    # Perform secure computation of the correlation coefficient
    result = await compute_correlation_coefficient(x_shares, y_shares)

    # Reveal the result
    correlation_coefficient = await mpc.output(result)
    print("Correlation Coefficient:", correlation_coefficient)

# Run the MPC protocol
mpc.run(main())
