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

import ssl
import sys
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ef0a72
import urllib2
 
context = ssl.create_default_context ()
# <yes> <report> PYTHON_CRYPTO_BAD_ALGORITHM 741df1
context.set_ciphers ( "TLS_RSA_WITH_RC4_128_SHA: TLS_ECDHE_RSA_WITH_RC4_128_SHA")
# <yes> <report> PYTHON_BACKDOOR_NETWORK_ACTIVITY 6f04ca <yes> <report> PYTHON_INJECTION_RESOURCE as04ea
URL = urllib2.urlopen ( "https://example.org", context=context)
# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 12571b
sys.stdout.write (str (url.read ()))
