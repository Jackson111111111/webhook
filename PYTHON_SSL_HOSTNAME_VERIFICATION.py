'''
    The HTTP clients in the (1) httplib, (2) urllib, (3) urllib2, and (4) xmlrpclib libraries in CPython (aka Python) 2.x before 2.7.9 and 3.x before 3.4.3, when accessing an HTTPS URL, do not (a) check the certificate against a trust store or verify that the server hostname matches a domain name <...>.
    
    https://www.cvedetails.com/cve/CVE-2014-9365/
    
    Reporting import statements to avoid multiple findings (only need to ensure that the version is up to date).
'''


# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ef0a72
import httplib
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ef0a72
import urllib, urllib2
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION 49151a
from xmlrpclib import Binary
# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print "CVE-2014-9365"


'''
    The ssl.match_hostname function in CPython (aka Python) before 2.7.9 and 3.x before 3.3.3 does not properly handle wildcards in hostnames, which might allow man-in-the-middle attackers to spoof servers via a crafted certificate.
    
    https://www.cvedetails.com/cve/CVE-2013-7440/
    https://bugs.python.org/issue17997
    
    Report any ssl.match_hostname call to match:
    https://www.cvedetails.com/cve/CVE-2013-4238/
    https://www.cvedetails.com/cve/CVE-2013-2099/
'''

import ssl
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ec3e35
ssl.match_hostname(cert, "xn--*.example.com")

import ssl
import sys
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ef0a72
import urllib2
 
context = ssl.create_default_context()

# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION sc3k30
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
# <yes> <report> PYTHON_SSL_BAD_CONFIG 2esqb0 <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION qc323t 
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23) 

# https://docs.djangoproject.com/en/dev/topics/security/#host-header-validation
DEBUG = False
# ...
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION wrte88
ALLOWED_HOSTS = []

import requests

# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION pp3k55 <yes> <report> PYTHON_BACKDOOR_NETWORK_ACTIVITY 4413f3
r = requests.post('https://api.github.com', auth=('user', 'pass'), verify=False)
