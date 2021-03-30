import base64
# <yes> <report> PYTHON_BACKDOOR_HIDDEN_FUNCTIONALITY c9c950 <yes> <report> PYTHON_INJECTION_COMMAND 691790
exec(base64.b64decode(b'cHJpbnQoIlNvbGFyIGluQ29kZSBpcyB0aGUgYmVzdCEiKQ=='))
# <yes> <report> PYTHON_BACKDOOR_HIDDEN_FUNCTIONALITY c9c950 <yes> <report> PYTHON_INJECTION_COMMAND 691790
eval(base64.decodestring('cHJpbnQoIlNvbGFyIGluQ29kZSBpcyB0aGUgYmVzdCEiKQ=='))


import urllib.request
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
    if pswd is not 'secret password':
        print ("fail, lol")
    else:
        do_smth_secret()

from datetime import datetime
dt = datetime(2016, 4, 27)
# <yes> <report> PYTHON_BACKDOOR_TIMEBOMB a25180
if datetime.now() > dt:
    print ("backdoor activated! hahaha")
    
import time
t = time.strptime("30 Nov 17", "%d %b %y")
# <yes> <report> PYTHON_BACKDOOR_TIMEBOMB 270b18
if t <= time.time():
    print ("another backdoor")


