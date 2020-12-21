import ssl
# <yes> <report> PYTHON_SSL_BAD_CONFIG 2esqb0
ssl.PROTOCOL_TLSv1_2
# <yes> <report> PYTHON_SSL_BAD_CONFIG revqb8
ssl_version = ssl.PROTOCOL_SSLv23
# <yes> <report> PYTHON_SSL_BAD_CONFIG revqb8
s = ssl.wrap_socket(sock, do_handshake_on_connect=True,
                    server_side=True, certfile=self.certificate,
                    keyfile=self.private_key, ssl_version=ssl.PROTOCOL_TLSv1_2)

import ssl
import sys
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ef0a72
import urllib2
 
context = ssl.create_default_context()

# <yes> <report> PYTHON_SSL_BAD_CONFIG 0eswb4
context.options &= ~ssl.OP_NO_SSLv2
# <yes> <report> PYTHON_SSL_BAD_CONFIG 0eswb4
context.options &= ~ssl.OP_NO_SSLv3
 
# <yes> <report> PYTHON_BACKDOOR_NETWORK_ACTIVITY 6f04ca <yes> <report> PYTHON_INJECTION_RESOURCE as04ea
url = urllib2.urlopen("https://example.org", context=context)
# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 12571b
sys.stdout.write(str(url.read()))

import requests
# <yes> <report> PYTHON_BACKDOOR_NETWORK_ACTIVITY 4413f3
requests.get('https://www.openstack.org/', verify=True)

# https://www.quantifiedcode.com/knowledge-base/security/%60SECURE_PROXY_SSL_HEADER%60%20set/70VXf68D
# <yes> <report> PYTHON_SSL_BAD_CONFIG ruuq99
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# <no> <report>
SECURE_PROXY_SSL_HEADER = None
