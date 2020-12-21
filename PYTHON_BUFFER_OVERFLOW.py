'''
    Buffer overflow in the socket.recvfrom_into function in Modules/socketmodule.c in Python 2.5 before 2.7.7, 3.x before 3.3.4, and 3.4.x before 3.4rc1 allows remote attackers to execute arbitrary code via a crafted string.
    
    https://www.cvedetails.com/cve/CVE-2014-1912/
    http://bugs.python.org/issue20246
'''

import socket
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# <yes> <report> PYTHON_BUFFER_OVERFLOW 53eeb3
s.recvfrom_into(bytearray(), 1024)

'''
	Integer overflow in the get_data function in zipimport.c 
	in CPython (aka Python) before 2.7.12, 3.x before 3.4.5, 
	and 3.5.x before 3.5.2 allows remote attackers to have unspecified impact 
	via a negative data size value, which triggers a heap-based buffer overflow.	
'''
import zipimport
import _memimporter
  
DEBUG_ZIPIMPORT = False
  
class ZipExtensionImporter(zipimport.zipimporter):

	def locate_dll_image(self, name):
	        if name in self._files:
				# <yes> <report> PYTHON_BUFFER_OVERFLOW 67eer0
	            return self.get_data(name)
	        return None