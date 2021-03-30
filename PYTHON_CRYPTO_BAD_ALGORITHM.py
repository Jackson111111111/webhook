'''
    cryptography
'''
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
# <yes> <report> PYTHON_CRYPTO_BAD_ALGORITHM 14b8d3
cipher = Cipher(algorithm=algorithms.ARC4(key), mode=modes.ECB, backend=default_backend())
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message")


'''
    PyCrypto
'''
from Crypto.Cipher import DES

# <yes> <report> PYTHON_CRYPTO_BAD_ALGORITHM b36e09
encryption_suite = DES.new('This is a key123', DES.MODE_CBC, 'This is an IV456')
cipher_text = encryption_suite.encrypt("A really secret message. Not for prying eyes.")

