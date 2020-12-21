# Possible BERserk attack: https://www.cvedetails.com/cve/CVE-2016-1494/
# The verify function in the RSA package for Python (Python-RSA) before 3.3 
# allows attackers to spoof signatures with a small public exponent via 
# crafted signature padding, aka a BERserk attack. 
# https://stuvel.eu/rsa

import rsa
# <yes> <report> PYTHON_CRYPTO_BAD_IMPLEMENTATION 69a440
rsa.verify(message, signature, pubkey)