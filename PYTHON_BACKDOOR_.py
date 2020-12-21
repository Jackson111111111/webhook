import base64
# <yes> <report> PYTHON_BACKDOOR_HIDDEN_FUNCTIONALITY c9c950 <yes> <report> PYTHON_INJECTION_COMMAND 691790
exec(base64.b64decode(b'cHJpbnQoIlNvbGFyIGluQ29kZSBpcyB0aGUgYmVzdCEiKQ=='))
# <yes> <report> PYTHON_BACKDOOR_HIDDEN_FUNCTIONALITY c9c950 <yes> <report> PYTHON_INJECTION_COMMAND 691790
eval(base64.decodestring('cHJpbnQoIlNvbGFyIGluQ29kZSBpcyB0aGUgYmVzdCEiKQ=='))


import urllib.request
# <yes> <report> PYTHON_SSL_HOSTNAME_VERIFICATION ef0a72
import urllib2
import requests
import socket
# <yes> <report> PYTHON_BACKDOOR_NETWORK_ACTIVITY 96f7fa
urllib.request.urlopen('http://example.com:8080/')
# <yes> <report> PYTHON_BACKDOOR_NETWORK_ACTIVITY 6f04ca
urllib2.urlopen('http://www.example.com')
# <yes> <report> PYTHON_BACKDOOR_NETWORK_ACTIVITY 4413f3
requests.get('http://79.174.66.120')
# <yes> <report> PYTHON_BACKDOOR_NETWORK_ACTIVITY 730d11
socket.connect('ftp://public.ftp-servers.example.com/file.txt')

# <yes> <report> PYTHON_BACKDOOR_SPECIAL_ACCOUNT 1c396f
if (login == 'secret_login'):
    # <yes> <report> PYTHON_BACKDOOR_SPECIAL_ACCOUNT 1c396f
    if 'secret password' != self.pswd:
    	# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
        print ("fail, lol")
    else:
        do_smth_secret()
# <no> <report>
if user_identifier is not None:
    params['UserIdentifier'] = user_identifier
# <no> <report>
if (check_password == True):
    do_smth_secret()
# <no> <report>
if (check_password == ''):
    do_smth_secret()

from datetime import datetime
dt = datetime(2016, 4, 27)
# <yes> <report> PYTHON_BACKDOOR_TIMEBOMB a25180
if datetime.now() > dt:
	 # <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print ("backdoor activated! hahaha")
    
import time
t = time.strptime("30 Nov 17", "%d %b %y")
# <yes> <report> PYTHON_BACKDOOR_TIMEBOMB 270b18
if t <= time.time():
	# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print ("another backdoor")
