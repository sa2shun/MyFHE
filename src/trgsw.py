import numpy as np

from .trlwe import trlweEncrypt
from .utils import dtot32
from MyFHE.src.FFT import PolyMul


def trgswEncrypt(p, alpha, h, key, twist):
    c = c = np.vstack([[trlweEncrypt(np.zeros(len(key)),alpha,key,twist)] for i in range(2*len(h))])
    m = dtot32(np.outer(h, p))
    c[:len(h), 0] += m
    c[len(h):, 1] += m
    return c


def Decomposition(trlwe, params):
    a = np.multiply.outer(params.decb, trlwe + params.offset)
    tmp = np.uint32(np.floor(a) % params.Bg) - params.Bg / 2
    return np.concatenate([tmp[:,0],tmp[:,1]])

def ExternalProduct(g, r, params):
    decvec = Decomposition(r, params)
    return np.array([np.sum([PolyMul(decvec[i], g[i][0], params.twist) for i in range(2 * params.l)], axis=0),
                     np.sum([PolyMul(decvec[i], g[i][1], params.twist) for i in range(2 * params.l)], axis=0)],
                    dtype=np.uint32)

#復号はいらない