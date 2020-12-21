from MiscUtils.Configurable import Configurable
config = Configurable()
settingName = 'settingName'
# <yes> <report> PYTHON_INJECTION_RESOURCE 36f5ed
config.setSetting(settingName)
# <yes> <report> PYTHON_INJECTION_RESOURCE 8sf5wd
config.setting(settingName, value)

import builtins
file = 'path/to/file'
# <yes> <report> PYTHON_INJECTION_RESOURCE 726551
file(file)
# <yes> <report> PYTHON_INJECTION_RESOURCE 726551
open(file)

# <yes> <report> PYTHON_INJECTION_RESOURCE 156b64
builtins.open(file)
# <yes> <report> PYTHON_INJECTION_RESOURCE 156b64
builtins.setattr(foo, bar, value)

from django.core.mail import EmailMessage
img_data = 'images/img'
message = EmailMessage('Title', 'Body', 'to@example.org')
# <yes> <report> PYTHON_INJECTION_RESOURCE 0afea5
message.attach('design.png', img_data, 'image/png')

import shelve
# <yes> <report> PYTHON_INJECTION_RESOURCE 55142c
shelve.open(file)


import tarfile
import zipfile
# <yes> <report> PYTHON_INJECTION_RESOURCE 62ec63
tarfile.open(file)
# <yes> <report> PYTHON_INJECTION_RESOURCE c55b0c
zipfile = ZipFile(file)
# <yes> <report> PYTHON_INJECTION_RESOURCE 62ec63
ZipFile.open(file)


# <yes> <report> PYTHON_INJECTION_RESOURCE 7a7f80
importlib.import_module(module)

import socket
# <yes> <report> PYTHON_INJECTION_RESOURCE 598wc1
socket.connect(address)

import sys

address = sys.stdin.readline () [: - 1]
sock = socket.socket ()
# <yes> <report> PYTHON_INJECTION_RESOURCE 599wc1
sock.connect ((address, 1234))
# <no> <report>
s.bind(("::1", 0))

# <yes> <report> PYTHON_INJECTION_RESOURCE 799fc7
sock.connect ((address, port))

import sys
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ef0a72
import urllib
 
url = sys.stdin.readline()[:-1]
# <yes> <report> PYTHON_INJECTION_RESOURCE as04ea
content = urllib.urlopen(url).read()
# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 12571b
sys.stdout.write(content)

# The following example is with httplib, but there is told about urllib2 and urllib in CPython 
# on https://www.cvedetails.com/cve/CVE-2016-5699/

# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ef0a72
import httplib, sys
  
def test_httplib():
    h = httplib.HTTPConnection('127.0.0.1', 80)
    h.set_debuglevel(1)
    h.putrequest('GET', '/')
	# <yes> <report> PYTHON_INJECTION_RESOURCE ds03ef
    h.putheader('Accept', 'text/html')
# <yes> <report> PYTHON_INJECTION_RESOURCE 55ecw1
contents = yaml.load(exploit_file)

# <yes> <report> PYTHON_INJECTION_RESOURCE rtec22
tmp = os.path.join(tempfile.gettempdir(), filename)
# <yes> <report> PYTHON_INJECTION_RESOURCE rtec22 <yes> <report> PYTHON_INJECTION_RESOURCE 726551 
open(tempfile.mktemp(), "w")
