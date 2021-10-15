import hashlib, binascii
# <yes> <report> PYTHON_CRYPTO_SALT_HARDCODED 29ca45
hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
salt = b'not hardcoded ;)'
# <no> <report>
hashlib.pbkdf2_hmac('sha256', b'password', salt, 100000)


'''
    pycrypto
'''
from Crypto.Protocol import KDF
# <yes> <report> PYTHON_CRYPTO_SALT_HARDCODED 87e746
PBKDF1('password', 'salt', dkLen=16, count=1000, hashAlgo=None)


'''
    passlib
'''
from passlib.hash import pbkdf2_sha256
# <yes> <report> PYTHON_CRYPTO_SALT_HARDCODED 8b6e3f
pbkdf2_sha256.encrypt('password', salt='salt')

'''
    cryptography
'''
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
backend = default_backend()
# <yes> <report> PYTHON_CRYPTO_SALT_HARDCODED 7c09ae
kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=b'salt',
     iterations=100000,
     backend=backend
)
k_e_y = kdf.derive(b"my great password")
