import os

# <yes> <report> PYTHON_FILE_SEPARATOR_HARDCODED 9528cd
os.open("filepath/with/hardcoded/separator")
# <no> <report>
os.open("filepath")
# <yes> <report> PYTHON_FILE_SEPARATOR_HARDCODED 9528cd
os.mkdir("filepath/with/hardcoded/separator")
# <no> <report>
os.mkdir("filepath")