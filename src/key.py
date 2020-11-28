import numpy as np
from secrets import randbits
from .FFT import TwistGen
from .tlwe import tlweEncrypt
from .trgsw import trgswEncrypt


# TODO とりあえずコピペなので後で変える。

class lweKey:
    def __init__(self, n: int, N: int):
        self.tlwe = np.array([randbits(1) for i in range(n)], dtype=np.uint32)
        self.trlwe = np.array([randbits(1) for i in range(N)], dtype=np.uint32)


class lweParams:
    def __init__(self, n: int, alpha: float, N: int, l: int, Bgbit: int, bkalpha: float, t: int, basebit: int,
                 ksalpha: float):
        self.n = n
        self.alpha = alpha
        self.N = N
        self.l = l
        self.Bg = 1 << Bgbit
        self.Bgbit = Bgbit
        self.bkalpha = bkalpha
        self.h = np.array([self.Bg ** (-(i + 1)) for i in range(l)], dtype=np.double)
        self.offset = np.uint32(self.Bg / 2 * np.sum(2 ** 32 * self.h))
        self.decb = np.array([(2 ** (-32)) * (self.Bg ** (i + 1)) for i in range(l)], dtype=np.double)
        self.twist = TwistGen(N)
        self.t = t
        self.basebit = basebit
        self.ksalpha = ksalpha


class SecretKey:
    def __init__(self, n: int, alpha: float, N: int, l: int, Bgbit: int, bkalpha: float, t: int, basebit: int,
                 ksalpha: float):  # Modify this to change parameter
        self.params = lweParams(n, alpha, N, l, Bgbit, bkalpha, t, basebit, ksalpha)
        self.key = lweKey(n, N)
