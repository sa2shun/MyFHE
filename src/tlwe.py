import numpy as np
from MyFHE.src.utils import modularNormalDistribution, dtot64
from secrets import randbits

mu = 2 ** (-3)  # μ= 1/8


def Encrypt(p, sk):
    '''
    :param p: array of 0 or 1
        plaintextlength

    :param sk:
        sercretkey

    :return: array
        EncryptText
    '''

    plaintextlength = len(p)
    c = np.empty((plaintextlength, sk.params.n + 1), dtype=np.uint32)
    for i in range(plaintextlength):
        assert p[i] == 0 or p[i] == 1, "plaintextlength must be 0 or 1"
        if p[i] == 0:
            c[i] = tlweEncrypt(-mu, sk.params.alpha, sk.key.tlwe)
        elif p[i] == 1:
            c[i] = tlweEncrypt(mu, sk.params.alpha, sk.key.tlwe)
    return c


def Decrypt(c, sk):
    '''
    :param c: array
        ciphertext

    :param sk:
        seacretkey

    :return: array of 0 or 1
        plaintext
    '''

    ciphertextlength = len(c)
    p = np.empty((ciphertextlength, sk.params.n + 1), dtype=np.uint32)
    for i in range(ciphertextlength):
        p[i] = tlweDecrypt(c[i], sk.key.tlwe)

    return p


def tlweEncrypt(p, alpha, key):
    '''
    :param p: int of 0 or 1
        plaintext

    :param alpha: float
        parameter of Modular normal distribution

    :param key:
        searcret key

    :return:
    '''
    a = np.array(dtype=np.uint32)
    for _ in range(len(key)):
        a = np.append(a, randbits(32))
    b = modularNormalDistribution(dtot64(p), alpha, 1)[0] + np.dot(a, key)
    return np.append(a, b)


def tlweDecrypt(c, key):
    '''

    :param c: float
        ciphertext
    :param key:
        seacretkey
    :return: int
        plaintext 0 or 1

    '''
    b_as = np.int32(c[len(key)] - np.dot(c[:len(key)], key))
    return (1 + np.sign(b_as)) / 2
