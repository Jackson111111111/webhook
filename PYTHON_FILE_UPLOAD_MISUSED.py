# https://docs.djangoproject.com/en/1.8/ref/settings/#media-root
# <yes> <report> PYTHON_FILE_UPLOAD_MISUSED ttte80
MEDIA_ROOT = '/path/to/my/static/files'
STATIC_ROOT = '/path/to/my/static/files'
# <no> <report> 
STATIC_ROOT = '/path/to/my/static/files'
MEDIA_ROOT = '/path/to/my/media/files'

# https://docs.quantifiedcode.com/python-anti-patterns/django/all/security/same_value_for_media_url_and_static_url.html
# https://docs.djangoproject.com/en/1.8/ref/settings/#media-url
STATIC_URL = 'http://www.mysite.com/static'
# <yes> <report> PYTHON_FILE_UPLOAD_MISUSED hjte45
MEDIA_URL = 'http://www.mysite.com/static'
# <no> <report> 
STATIC_URL = 'http://www.mysite.com/static'
MEDIA_URL = 'http://www.mysite.com/media'