# <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print(system_info)

import logging

LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
# <yes> <report> PYTHON_INFORMATION_LEAK 8eeebv
logging.debug("This message should go to the log file")

import logging.Logger
logger = logging.getLogger('tcpserver')
# <yes> <report> PYTHON_INFORMATION_LEAK he7ebk
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

import warnings
# <yes> <report> PYTHON_INFORMATION_LEAK je7ebq
warnings.warn("deprecated", DeprecationWarning)

import cgitb
 
# <yes> <report> PYTHON_INFORMATION_LEAK dete9q
cgitb.enable ()
# <yes> <report> PYTHON_INFORMATION_LEAK rrte55
cgitb.enable (display=1)

from django.conf import settings
# <yes> <report> PYTHON_INFORMATION_LEAK lkte9q
settings.configure(DEBUG=True)
# <yes> <report> PYTHON_INFORMATION_LEAK lkte21
settings.DEBUG = True   # Don't do this! (c)DjangoDoc

# Содержимое settings.py библиотеки Django
# <yes> <report> PYTHON_INFORMATION_LEAK 12te21
DEBUG = True

