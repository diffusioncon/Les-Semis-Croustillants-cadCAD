from numpy import exp


def scaled_gaussian(mu, var, x):
    return exp(-(x-mu)**2/2/var)
