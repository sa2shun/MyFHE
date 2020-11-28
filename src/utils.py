import numpy as np

def dtot32(d: np.float):
    '''
    Real number to Torus
    int((d mod1) * 2^(ω)
    :param d: Real number
    :return: torus
    '''
    return np.uint32(np.round((d%1)*(2**32)))

def dtot64(d:np.float):
    '''

    :param d:
    :return:
    '''

    return np.uint64(np.round((d%1)*(2.0**63)))

def modularNormalDistribution(mu,alpha:float,size = 1):
    return dtot32(np.random.normal(0,alpha,size))  + np.uint32(mu)