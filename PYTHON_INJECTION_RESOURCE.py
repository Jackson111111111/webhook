from MiscUtils.Configurable import Configurable
config = Configurable()
settingName = 'settingName'
# <yes> <report> PYTHON_INJECTION_RESOURCE 36f5ed
config.setSetting(settingName)

import builtins
file = 'path/to/file'
# <yes> <report> PYTHON_INJECTION_RESOURCE 54972e
file(file)
# <yes> <report> PYTHON_INJECTION_RESOURCE 54972e
open(file)

# <yes> <report> PYTHON_INJECTION_RESOURCE 156b64
builtins.open(file)
# <yes> <report> PYTHON_INJECTION_RESOURCE 156b64
builtins.setattr(foo, bar, value)

from django.core.mail import EmailMessage
img_data = 'images/img'
message = EmailMessage('Title', 'Body', 'to@example.org')
# <yes> <report> PYTHON_INJECTION_RESOURCE 0afea5
message.attach('design.png', img_data, 'image/png')

import shelve
# <yes> <report> PYTHON_INJECTION_RESOURCE 55142c
shelve.open(file)


import tarfile
import zipfile
# <yes> <report> PYTHON_INJECTION_RESOURCE 62ec63
tarfile.open(file)
# <yes> <report> PYTHON_INJECTION_RESOURCE c55b0c
zipfile = ZipFile(file)
# <yes> <report> PYTHON_INJECTION_RESOURCE 62ec63
ZipFile.open(file)


# <yes> <report> PYTHON_INJECTION_RESOURCE 7a7f80
importlib.import_module(module)


# <yes> <report> PYTHON_INJECTION_RESOURCE 699fc7
socket.connect(address)
