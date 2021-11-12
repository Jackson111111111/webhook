'''
    PyCrypto
'''

from Crypto.PublicKey.RSA import _RSAobj
# <yes> <report> PYTHON_CRYPTO_BAD_PADDING 03a2e1
textbookRSA = _RSAobj()

'''
    cryptography
'''
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# <yes> <report> PYTHON_CRYPTO_BAD_PADDING bab4de
ciphertext = public_key.encrypt(
    message,
    padding.PKCS1v15(
        mgf=padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
    )
)