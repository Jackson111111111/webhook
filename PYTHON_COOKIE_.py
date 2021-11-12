from http.cookies import SimpleCookie
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