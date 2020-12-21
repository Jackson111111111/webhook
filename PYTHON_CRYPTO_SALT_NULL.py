import hashlib, binascii
# <yes> <report> PYTHON_CRYPTO_SALT_NULL jjca4y
hashlib.pbkdf2_hmac('sha256', password, None, 100000)
salt = b'not hardcoded ;)'
# <no> <report>
hashlib.pbkdf2_hmac('sha256', password, salt, 100000)


'''
    pycrypto
'''
from Crypto.Protocol import KDF
# <yes> <report> PYTHON_CRYPTO_SALT_NULL hce700
PBKDF1(password, None, dkLen=16, count=1000, hashAlgo=None)


'''
    passlib
'''
from passlib.hash import pbkdf2_sha256
# <yes> <report> PYTHON_CRYPTO_SALT_NULL er6e8f
pbkdf2_sha256.encrypt(password, salt=None)

'''
    cryptography
'''
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
backend = default_backend()
# <yes> <report> PYTHON_CRYPTO_SALT_NULL tg0qae
kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=None,
     iterations=100000,
     backend=backend
)
k_e_y = kdf.derive(b"my great password")

from django.contrib.auth.hashers import make_password
# <yes> <report> PYTHON_CRYPTO_SALT_NULL mn096e
make_password(password, salt=None)

from django.utils.crypto import salted_hmac
# <yes> <report> PYTHON_CRYPTO_SALT_NULL bb0q6e
hmac = salted_hmac(value, None).hexdigest()