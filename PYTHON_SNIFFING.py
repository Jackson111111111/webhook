# <yes> <report> PYTHON_SNIFFING rtuq44
SECURE_CONTENT_TYPE_NOSNIFF = False

from WebKit.HTTPResponse import HTTPResponse

response = HTTPResponse()
# <yes> <report> PYTHON_SNIFFING edft3b
response['X-Content-Type-Options'] = 'nosniff'