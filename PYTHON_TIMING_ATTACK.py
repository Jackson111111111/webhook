# <yes> <report> PYTHON_PASSWORD_HARDCODED eed164
password = 'qwerty'
# <yes> <report> PYTHON_KEY_HARDCODED 8c1e87
key = '12345'
hash = 'abcdef'

# <yes> <report> PYTHON_PASSWORD_HARDCODED eed164
right_password = 'qwerte'
# <yes> <report> PYTHON_KEY_HARDCODED 8c1e87
right_key = '12345'
right_hash = 'abcdef'

# <yes> <report> PYTHON_TIMING_ATTACK aab457 <yes> <report> PYTHON_BACKDOOR_SPECIAL_ACCOUNT 1c396f
if password == right_password:
    print ('insecure comparison of password')

# <yes> <report> PYTHON_TIMING_ATTACK aab457
if key != right_key:
    pass
else:
    print ('insecure comparison of key')

# <yes> <report> PYTHON_TIMING_ATTACK aab457
if right_hash == hash:
    print ('insecure comparison of hash')