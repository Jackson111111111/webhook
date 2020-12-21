import sys
# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 12571b
sys.stdout.write(text) 
# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 12571b
sys.stderr.write(text)
# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de <yes> <report> PYTHON_INFORMATION_LEAK wedqb9
print(text)
# <yes> <report> PYTHON_INFORMATION_LEAK wedqb9
print(text, file='myfile.txt')
# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT de57de
print("fatal error", file=sys.stderr)