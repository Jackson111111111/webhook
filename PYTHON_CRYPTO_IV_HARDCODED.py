from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
# <yes> <report> PYTHON_CRYPTO_IV_HARDCODED hj6kk6
cipher = AES.new(key, AES.MODE_CBC, IV="key")
# <yes> <report> PYTHON_CRYPTO_IV_HARDCODED hrtyk6
cipher = AESCipher(key, MODE_CBC, IV="key")
