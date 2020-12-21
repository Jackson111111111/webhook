from WebKit.HTTPResponse import HTTPResponse

response = HTTPResponse()
# <yes> <report> PYTHON_HTML5_CORS ea7d3b
response.setHeader('Access-Control-Allow-Origin', '*')
# <no> <report>
response.setHeader('headerName', 'headerValue')
# <no> <report>
notAResponse.setHeader('Access-Control-Allow-Origin', '*')
