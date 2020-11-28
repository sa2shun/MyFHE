from ..src import tlwe, key
import numpy as np

sk = key.SecretKey(500, 2 ** (-9), 1024, 2, 512, 2 ** (-24), 1, 2 ** (-24))
c = tlwe.Encrypt(np.array([0, 1]), sk)
print(tlwe.Decrypt(c, sk))
