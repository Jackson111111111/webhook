from http.cookies import SimpleCookie
from WebKit.HTTPResponse import HTTPResponse

response = HTTPResponse()
cookie = SimpleCookie()
cookie['foo'] = 'bar'

'''
# FIXME: does not detect class in this case:
from http import cookies
cookie = cookies.SimpleCookie()
'''

# <yes> <report> PYTHON_COOKIE_BROAD_DOMAIN 23dd47
cookie['foo']['domain'] = '.example.com'

# <yes> <report> PYTHON_COOKIE_BROAD_PATH b49cc1
cookie['foo']['path'] = '/'

# <yes> <report> PYTHON_COOKIE_NOT_HTTPONLY d6d76e
cookie['foo']['httponly'] = notSoSure
# <no> <report>
cookie['foo']['httponly'] = True

# <yes> <report> PYTHON_COOKIE_NOT_OVER_SSL 2a61c4
cookie['foo']['secure'] = notSoSure
# <no> <report>
cookie['foo']['secure'] = True

# <yes> <report> PYTHON_COOKIE_PERSISTENT d69988
cookie['foo']['max-age'] = 901
# <no> <report>
cookie['foo']['max-age'] = 900
# <no> <report>
cookie['foo']['max-age'] = -1

# <no> <report>
cookie['foo']['field'] = 'value'

# <yes> <report> PYTHON_COOKIE_BROAD_PATH fhy233
response.setCookie(self, name, value, path='/', expires='ONCLOSE', secure=False)

# Содержимое settings.py библиотеки Django
# <yes> <report> PYTHON_COOKIE_NOT_HTTPONLY 2lf1c4
SESSION_COOKIE_HTTPONLY = False

from django.conf import settings
# <yes> <report> PYTHON_COOKIE_NOT_HTTPONLY ler1c4
settings.configure(SESSION_COOKIE_HTTPONLY = False)
# <yes> <report> PYTHON_COOKIE_NOT_HTTPONLY ler1c4
settings.configure(CSRF_COOKIE_HTTPONLY = False)

from django.http.response import HttpResponse
def method2 (request):
  goto = request.GET.get('goto', '')
  response = http.HttpResponseRedirect(goto)
# <yes> <report> PYTHON_COOKIE_NOT_HTTPONLY ler1c5
  response.set_cookie('PIZZA_EDIT', value='ON', max_age=60 * 60 * 24, httponly=False, path='/path')
  return response

# <yes> <report> PYTHON_COOKIE_NOT_OVER_SSL 1lf1c4
CSRF_COOKIE_SECURE = False
from django.conf import settings
# <yes> <report> PYTHON_COOKIE_NOT_OVER_SSL 1er1c4
settings.configure(SESSION_COOKIE_SECURE = False)

# <yes> <report> PYTHON_COOKIE_BROAD_DOMAIN 7lf1c4
SESSION_COOKIE_DOMAIN = ".example.com"
# <yes> <report> PYTHON_COOKIE_BROAD_DOMAIN 7er1c4
settings.configure(CSRF_COOKIE_DOMAIN = ".example.com")
def method4(request):
  res = HttpResponse()
  path = '/path'
# <yes> <report> PYTHON_COOKIE_BROAD_DOMAIN 7er1c5
  res.set_cookie("emailCookie", email, secure=True, httponly=True, domain=".example.com", path=path)
  return res

# <yes> <report> PYTHON_COOKIE_BROAD_PATH 3lf1c4
SESSION_COOKIE_PATH = "/"
# <yes> <report> PYTHON_COOKIE_BROAD_PATH 3er1c4
settings.configure(CSRF_COOKIE_PATH = "/")
def method5(request):
  res = HttpResponse()
# <yes> <report> PYTHON_COOKIE_BROAD_PATH 3er1c5
  res.set_cookie("emailCookie", email, secure=True, httponly=True, path='/')
  return res

# <yes> <report> PYTHON_COOKIE_PERSISTENT 1lf1kf
SESSION_COOKIE_AGE = 901
# <yes> <report> PYTHON_COOKIE_PERSISTENT kfr1c4
settings.configure(SESSION_COOKIE_AGE = 901)

def method5(request):
  res = HttpResponse()
# <yes> <report> PYTHON_COOKIE_PERSISTENT 1er115
  res.set_cookie("emailCookie", email, expires=time()+901, secure=True, httponly=True, path='/full_path')
  return res



