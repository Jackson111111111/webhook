import md5
import sha
import hashlib
# <yes> <report> PYTHON_CRYPTO_BAD_HASH d6506c
m = md5.new()
# <yes> <report> PYTHON_CRYPTO_BAD_HASH d6506c
s = sha.new()
# <yes> <report> PYTHON_CRYPTO_BAD_HASH 69a425
h = hashlib.sha1()
# <yes> <report> PYTHON_CRYPTO_BAD_HASH d97750
h2 = hashlib.new("MD4")
# <no> <report>
h256 = hashlib.new("SHA256")

'''
    pycrypto
'''
from Crypto.Hash import SHA
# <yes> <report> PYTHON_CRYPTO_BAD_HASH 291e54
badHash1 = SHA1Hash.new('abc')
from Crypto.Hash import MD5
# <yes> <report> PYTHON_CRYPTO_BAD_HASH f389ba
badHash2 = MD5Hash()

'''
    passlib
'''
from passlib.hash import md5_crypt
# <yes> <report> PYTHON_CRYPTO_BAD_HASH d7a90c
hash = md5_crypt.encrypt("password")
from passlib.context import CryptContext
# <yes> <report> PYTHON_CRYPTO_BAD_HASH 71a292
pwd_context = CryptContext(schemes=["md5_crypt", "des_crypt"])
# <yes> <report> PYTHON_CRYPTO_BAD_HASH 007d46
hash2 = pwd_context.encrypt("letmein", scheme="crypt16")
# <no> <report>
hashSecure = pwd_context.encrypt(scheme="sha256_crypt")

