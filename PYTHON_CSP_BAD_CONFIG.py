MIDDLEWARE_CLASSES = (
    'csp.middleware.CSPMiddleware',
)
# <yes> <report> PYTHON_CSP_BAD_CONFIG nftfp9
CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'", 'cdn.example.net')

response = HTTPResponse()
# <yes> <report> PYTHON_CSP_BAD_CONFIG yyf55k
response['X-Content-Security-Policy'] = 'unsafe-inline'
# <yes> <report> PYTHON_CSP_BAD_CONFIG fff557
response['X-Content-Security-Policy'] = 'script-src'
# <yes> <report> PYTHON_CSP_BAD_CONFIG ddf533
response['X-Content-Security-Policy'] = 'script-src' 'frame-src' 'nonce'
# <yes> <report> PYTHON_CSP_BAD_CONFIG ddf533
response['X-Content-Security-Policy'] = 'frame-src'
# <no> <report> PYTHON_CSP_BAD_CONFIG ddf533
response['X-Content-Security-Policy'] = 'frame-src' 'sandbox'
# <no> <report> PYTHON_CSP_BAD_CONFIG ddf533
response['X-Content-Security-Policy'] = 'sandbox' 'frame-src'