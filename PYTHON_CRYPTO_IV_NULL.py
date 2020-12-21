from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
# <yes> <report> PYTHON_CRYPTO_IV_NULL hmmmk6
cipher = AES.new(key, AES.MODE_CBC, IV=None)
