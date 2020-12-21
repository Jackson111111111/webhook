import md5
import sha
import hashlib
# https://vulncat.hpefod.com/en/weakness?codelang=Python&po=13
# <yes> <report> PYTHON_CRYPTO_BAD_ITERATION_COUNT swca22
dk = pbkdf2_hmac('sha256', password, salt, 50)
# <yes> <report> PYTHON_CRYPTO_SALT_HARDCODED 87e746 <yes> <report> PYTHON_CRYPTO_BAD_ITERATION_COUNT rmca29
PBKDF1(password, 'salt', dkLen=16, count=100, hashAlgo=None)
# <yes> <report> PYTHON_CRYPTO_BAD_ITERATION_COUNT rmca29
kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=salt,
     iterations=100,
     backend=backend
)