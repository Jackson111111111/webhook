# <yes> <report> PYTHON_CRYPTO_KEY_NULL 24571b
self.key = None
# <yes> <report> PYTHON_CRYPTO_KEY_NULL 24571b
key = None if not need_key else new_key
# <no> <report>
key = new_key() if key is None else key

# <yes> <report> PYTHON_CRYPTO_KEY_EMPTY 1af1de
key = ""
# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED 8c1e87
key = "7bf651dda432aadd"
# <no> <report>
key = 'key'

k = "not_so_hardcoded"
# <no> <report>
key = k

# <no> <report>
key = bucket.new_key('')

# <no> <report>
full_key = '%s.%s' % (current_prefix, key)

# <no> <report>
newkey = key + '.' + acc + (acc and '.' or '')

from Crypto.Cipher import AES
# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED 126e21
cipher = AES.new("7bf651dda432aadd22", AES.MODE_CBC, "iv")
# <yes> <report> PYTHON_CRYPTO_KEY_EMPTY 126e09 <yes> <report> PYTHON_CRYPTO_BAD_ALGORITHM b36e09
cipher = DES.new("", DES.MODE_CBC, 'iv')
# <yes> <report> PYTHON_CRYPTO_KEY_NULL 126609
cipher = AES.new(None, AES.MODE_CBC, 'iv')

import hmac
# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED 226e21
mac = hmac.new("7bf651dda432aadd22", plaintext).hexdigest()
# <yes> <report> PYTHON_CRYPTO_KEY_EMPTY 226e09
mac = hmac.new("", plaintext).hexdigest()

# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED knte4w
CONSUMER_SECRET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

import stripe
# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED bvte43
stripe.api_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


from Crypto.PublicKey import RSA

key = RSA.generate(2048)
f = open('mykey.pem','w')
# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED mpt77w
f.write(key.exportKey(format='PEM'))
f.close()
# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED uut7ff
privatekey = key.exportKey(passphrase="code", pkcs=8)
















