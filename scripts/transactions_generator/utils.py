import numpy as np
import scipy.stats as stats


def uniform(lower,upper):
    return np.round(np.random.uniform(lower,upper))


def pareto(min,a):
    """Returns a sample from a Pareto distribution"""
    return int(np.round(np.random.pareto(1)))+min


def truncatedNormal(lower,upper,mu,sigma):
    """Returns a sample from a trancated normal distribution"""

    lower, upper = 0, 500
    mu, sigma = 150, 5
    # Defining the random variable
    X = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
    # Drawing a sample
    return int(X.rvs(1))

def gini(arr):
    """Calculated Gini Index"""

    ## first sort
    sorted_arr = arr.copy()
    sorted_arr.sort()
    n = arr.size
    coef_ = 2. / n
    const_ = (n + 1.) / n
    weighted_sum = sum([(i+1)*yi for i, yi in enumerate(sorted_arr)])
    return coef_*weighted_sum/(sorted_arr.sum()) - const_

def lorenz(arr):
    """Draws lorenz curve"""

    ## first sort
    sorted_arr = arr.copy()
    sorted_arr.sort()
    # this divides the prefix sum by the total sum
    # this ensures all the values are between 0 and 1.0
    scaled_prefix_sum = sorted_arr.cumsum() / sorted_arr.sum()
    # this prepends the 0 value (because 0% of all people have 0% of all wealth)
    return np.insert(scaled_prefix_sum, 0, 0)