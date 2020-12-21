from Cookie import SimpleCookie
import sys
 
CKS = SimpleCookie ()
c_key = sys.stdin.readline () [: - 1]
c_value = sys.stdin.readline () [: - 1]
# <yes> <report> PYTHON_HEADER_MANIPULATION_COOKIES f5r4e2 
CKS [c_key] = c_value
