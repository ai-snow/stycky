# Import relevant packages
import numpy as np
import math
import statistics

##
# Function: simulate
#
# Simulates a stock price using the foundational binomial tree model.
# S_0   = current stock price
# T     = Number of time steps to project stock price
# p     = Probability of the stock going up at each time step
# delta = Force of interest per time step
#
# Returns: The projected stock price at time T, S_T
##
def simulate(S_0, T, p, delta):
    S_t = S_0
    for t in range(1, T + 1):
        # B_t is either 1 (stock price went up) or 0 (stock price went down)
        B_t = np.random.binomial(1, p)
        
        # delta_t is either delta (stock price went up) or -delta (stock price went down)
        delta_t = delta * (2 * B_t - 1)
        
        # Use force of interest model to move the stock price to the next time step
        S_t = S_t * math.exp(delta_t)
    
    return S_t

# Simulate 1000 stock prices.  Current stock price is 100, number of time steps is 12 (monthly),
# probability of stock moving up is .5, and the force of interest over 1 month is 1% (0.01)
simulated_prices = [simulate(100, 12, .5, .01) for _ in range(1001)]

##
# Function: statistics_display
#
# Prints various statistics of a data set.
# data = a list of data
def statistics_display(data):
    print("Mean: {0}".format(statistics.mean(data)))
    print("Median: {0}".format(statistics.median(data)))
    print("Std. Dev.: {0}".format(statistics.stdev(data)))

# Print statistics about the simulated stock prices
statistics_display(simulated_prices)
