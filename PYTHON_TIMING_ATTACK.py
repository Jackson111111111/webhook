# <yes> <report> PYTHON_PASSWORD_HARDCODED eed164
password = 'qwerty'
# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED 8c1e87
key = '917bfd5a'
hash = 'abcdef'

# <yes> <report> PYTHON_PASSWORD_HARDCODED eed164
right_password = 'qwerte'
# <yes> <report> PYTHON_CRYPTO_KEY_HARDCODED 8c1e87
right_key = '716544cf'
right_hash = 'abcdef'

# <yes> <report> PYTHON_TIMING_ATTACK aab457 
if password == right_password:
	# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print ('insecure comparison of password')

# <yes> <report> PYTHON_TIMING_ATTACK aab457
if key != right_key:
    pass
else:
	# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print ('insecure comparison of key')
# <no> <report>
if find_macro != -1:
    pass
# <no> <report>
if key != 1:
    pass
    
# <yes> <report> PYTHON_TIMING_ATTACK 88116f
if 'ba7651cd9008761d' == hash:
	# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print ('insecure comparison of hash')
# <no> <report>
if the_key == ' t':
    return tuple(the_value)
# <no> <report>
if len(key) != key_size:
        raise ValueError("Incorrect DES key length (%d bytes)" % len(key))

