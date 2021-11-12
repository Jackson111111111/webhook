from WebKit.HTTPResponse import HTTPResponse

response = HTTPResponse()
headerName = 'tainted header name'
headerName = 'tainted header value'
# <yes> <report> PYTHON_HEADER_MANIPULATION c504e9
response.setHeader(headerName, headerValue)
# <yes> <report> PYTHON_HEADER_MANIPULATION c504e9
response.setHeader('safeHeaderName', headerValue)
response.setHeader('safeHeaderName', 'safeHeaderValue')

code = 200
msg = 'OK'
# <yes> <report> PYTHON_HEADER_MANIPULATION c504e9
response.setStatus(code, msg)
