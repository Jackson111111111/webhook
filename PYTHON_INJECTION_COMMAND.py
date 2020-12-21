import os
import subprocess
import commands

command = 'print("system command")'
args = 'arg1'
# <yes> <report> PYTHON_INJECTION_COMMAND 6aae42
os.system(command)
# <no> <report>
os.system('command')
# <yes> <report> PYTHON_INJECTION_COMMAND 6aae42
os.system('command' + args)
# <yes> <report> PYTHON_INJECTION_COMMAND 6aae42
os.system(command + 'args')
# <yes> <report> PYTHON_INJECTION_COMMAND 6aae42
os.popen(command)


# <yes> <report> PYTHON_INJECTION_COMMAND c6f252
subprocess.call("mycmd" + args, shell=False)
# <yes> <report> PYTHON_INJECTION_COMMAND fuf299
subprocess.call("mycmd" + args, shell=True)
# <yes> <report> PYTHON_INJECTION_COMMAND fuf299
subprocess.run("mycmd" + args, shell=True)
# <yes> <report> PYTHON_INJECTION_COMMAND af00c9
pipe = Popen(command, shell=False, bufsize=bufsize, stdout=PIPE).stdout
# <yes> <report> PYTHON_INJECTION_COMMAND kp0tr7
pipe = Popen(command, shell=True, bufsize=bufsize, stdout=PIPE).stdout

# <yes> <report> PYTHON_INJECTION_COMMAND 691790
eval(command)
# <yes> <report> PYTHON_INJECTION_COMMAND 691790
exec(command)
# <yes> <report> PYTHON_INJECTION_COMMAND 691790
pickle(args)
# <yes> <report> PYTHON_INJECTION_COMMAND ret243
pickle.dump(obj, file, protocol=None, fix_imports=True)
# <yes> <report> PYTHON_INJECTION_COMMAND 34877f
popen2.popen3(command)

# <yes> <report> PYTHON_INJECTION_COMMAND 0187fa
commands.getoutput(command)

import sys
# <yes> <report> PYTHON_INJECTION_COMMAND 3fbfda
sys.call_tracing(command)

# <yes> <report> PYTHON_INJECTION_COMMAND cd6f58
input(command)

import sys
 
module_name = sys.stdin.readline () [: - 1]
# <yes> <report> PYTHON_INJECTION_COMMAND fr7f87
module = __import__ (module_name)
module.foo ()
# <yes> <report> PYTHON_INJECTION_COMMAND fr7f87
importlib.find_loader(name, path=None)










