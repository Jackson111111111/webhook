# (RSA < 2048 bits) AES < 128 bits = 16 bytes

'''
    PyCrypto
'''
from Crypto.Cipher import AES
# <yes> <report> PYTHON_CRYPTO_KEY_SIZE 64a8d6
encryption_suite = AES.new('key123', AES.MODE_CBC, 'This is an IV456')
cipher_text = encryption_suite.encrypt("A really secret message. Not for prying eyes.")
