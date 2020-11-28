import numpy as np
from .utils import modularNormalDistribution, dtot32
from .FFT import PolyMul


def trlweEncrypt(p, alpha, key, twist):
    a = np.array(dtype=np.uint32)
    for _ in range(len(key)):
        a = np.append(a, modularNormalDistribution(32))
    b = modularNormalDistribution(dtot32(p), alpha, len(key))
    b += PolyMul(a, key, twist)
    return np.array([a, b])


def trlweDecrypt(c, key, twist):
    return (1 + np.sign(np.int32(c[1] - PolyMul(c[0], key, twist)))) // 2


def SampleExtractIndex(r, index):
    N = len(r[0])
    return np.concatenate(
        [[r[0][index - i] for i in range(index + 1)], [-r[0][N - 1 - i] for i in range(N - index - 1)], [r[1][index]]])
