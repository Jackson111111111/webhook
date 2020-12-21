MIDDLEWARE_CLASSES = (
    'csp.middleware.CSPMiddleware',
)
# <yes> <report> PYTHON_OVERLY_PERMISSIVE_CSP kk0fp9
CSP_DEFAULT_SRC = ("'self'", '*')
# <yes> <report> PYTHON_OVERLY_PERMISSIVE_CSP ttdf88
CSP_SANDBOX = ("'self'", 'allow-*')