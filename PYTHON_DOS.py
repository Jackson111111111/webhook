import time
# <yes> <report> PYTHON_DOS 7be7e0
time.sleep(delay)
# <no> <report>
time.sleep(10)

'''
    Python before 3.3.4 RC1 allows remote attackers to cause a denial of service (infinite loop and CPU consumption) via a file size value larger than the size of the zip file to the (1) ZipExtFile.read, (2) ZipExtFile.read(n), (3) ZipExtFile.readlines, (4) ZipFile.extract, or (5) ZipFile.extractall function.
    
    https://www.cvedetails.com/cve/CVE-2013-7338/
    http://bugs.python.org/issue20078
    
    The following methods on such an archive all result in an infinite loop:

    ZipExtFile.read
    ZipExtFile.read(n)
    ZipExtFile.readlines
    ZipFile.extract
    ZipFile.extractall

'''

from zipfile import ZipExtFile, ZipFile

with ZipFile('z.zip') as zipfile:
    # <todo> <report> PYTHON_DOS f605ce
    zipfile.extractall(dest_dir)

with ZipExtFile('e.zip') as zipextfile:
    # <todo> <report> PYTHON_DOS e8ea0b
    zipextfile.read(dest_dir)

import marshal
 
f = open ( 'marshal.bin', 'wb')
s = ( "string", 123)
# <yes> <report> PYTHON_DOS w8ea7b 
marshal.dump (s, f)
f.close()
 
inf = open( 'marshal.bin', 'rb')
# <yes> <report> PYTHON_DOS w8ea7b 
obj = marshal.load (inf)
inf.close()

import asyncore, socket
# <yes> <report> PYTHON_DOS g8ed7q 
class HTTPClient(asyncore.dispatcher):

    def __init__(self, host, path):
        # <yes> <report> PYTHON_DOS g8ed7q 
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, 80) )
        self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path

client = HTTPClient('www.python.org', '/')
# <yes> <report> PYTHON_DOS g8ed7q 
asyncore.loop()