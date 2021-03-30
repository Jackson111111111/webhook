if False:
    # <yes> <report> PYTHON_BACKDOOR_DEAD_CODE e4c420
    print ("dead code!")
else:
    pass
    
if True:
    pass
else:
    # <yes> <report> PYTHON_BACKDOOR_DEAD_CODE ac3bfc
    print ("dead code too!")
    for i in range(0,4):
        print(i)