# <yes> <report> PYTHON_OBSOLETE se4ebf
import imp
# <no> <report>
import sys

def __import__(name, globals=None, locals=None, fromlist=None):
    try:
        return sys.modules[name]
# <yes> <report> PYTHON_ERROR_HANDLING_EMPTY_CATCH b0eb34
    except KeyError:
        pass

    fp, pathname, description = imp.find_module(name)

    try:
        return imp.load_module(name, fp, pathname, description)
    finally:
        if fp:
            fp.close()

from Cookie import SerialCookie
import sys
 
c_value = sys.stdin.readline () [: - 1]
# <yes> <report> PYTHON_OBSOLETE wqte90
cks = SerialCookie()
cks['foo'] = c_value
