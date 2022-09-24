import numpy as np
import scipy.stats as stats


def uniform(lower,upper):
    return np.round(np.random.uniform(lower,upper))


def pareto(min):
    """Returns a sample from a Pareto distribution"""
    return int(np.round((np.random.pareto(1)+1)*min))


def truncatedNormal(lower,upper,mu,sigma):
    """Returns a sample from a trancated normal distribution"""

    lower, upper = lower, upper
    mu, sigma = mu, sigma
    # Defining the random variable
    X = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
    # Drawing a sample
    return int(X.rvs(1))

def distributionController(config):
    """ Gets as an input the configuration of a distribution and returns a sample"""

    if config['name'] == 'Pareto':
        return pareto(config['min'])
    elif config['name'] == 'Normal':
        return truncatedNormal(config['min'],config['max'],config['mu'],config['sigma'])
    elif config['name'] == 'Uniform':
        return uniform(config['min'],config['max'])
    elif config['name'] == 'None':
        return config['min']
    else:
        print('Not a valid distribution name is given!')




        
