from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
# <yes> <report> PYTHON_CRYPTO_BAD_IV jjjykp
cipher = AESCipher(key, MODE_CBC, IV=key)
