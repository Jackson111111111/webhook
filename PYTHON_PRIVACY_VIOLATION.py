
# <no> <report>
cfg.StrOpt('password', help='Password of the host.', secret=True)
# <yes> <report> PYTHON_PRIVACY_VIOLATION jh4e33
cfg.StrOpt('password', help='Password of the host.', secret=False)
# <yes> <report> PYTHON_PRIVACY_VIOLATION jh4e33
cfg.StrOpt('password', help='Password of the host.')

MIDDLEWARE_CLASSES = (
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.middleware.gzip.GZipMiddleware')
# https://docs.djangoproject.com/en/dev/ref/middleware/#module-django.middleware.gzip
# <yes> <report> PYTHON_PRIVACY_VIOLATION hp15dd
from django.middleware.gzip import GZipMiddleware