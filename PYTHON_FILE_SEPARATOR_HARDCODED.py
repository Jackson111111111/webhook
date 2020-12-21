import os

# <yes> <report> PYTHON_FILE_SEPARATOR_HARDCODED 9528cd
os.open("filepath/with/hardcoded/separator")
# <no> <report>
os.open("filepath")
# <yes> <report> PYTHON_FILE_SEPARATOR_HARDCODED 9528cd
os.mkdir("filepath/with/hardcoded/separator")
# <no> <report>
os.mkdir("filepath")
# <yes> <report> PYTHON_FILE_SEPARATOR_HARDCODED 9528cd 
os.remove(re.sub(r'hard\\coded\\path\.py$', '$py.class', full_name))
# <no> <report> 
os.remove(re.sub(r'\.py$', '$py.class', full_name))