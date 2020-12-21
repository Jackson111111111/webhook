
if False:
    # <yes> <report> PYTHON_BACKDOOR_DEAD_CODE e4c420 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print ("dead code!")
else:
    pass
    
if True:
    pass
else:
    # <yes> <report> PYTHON_BACKDOOR_DEAD_CODE ac3bfc <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print ("dead code too!")
    for i in range(0,4):
        # <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
        print(i)
       
if foo.bar is True:
    # <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print('not dead')
    # <no> <report> 
elif foo.bar2 is False:
    # <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print('not dead')