try:
	# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print("Hello, world!")
# <yes> <report> PYTHON_ERROR_HANDLING_EMPTY_CATCH b0eb34
except ZeroDivisionError:
    pass    # empty catch
else:
	# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print("Raising generic Error")
    # <yes> <report> PYTHON_ERROR_HANDLING_BROAD_THROW 7a492c
    raise Exception
finally:
	# <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
    print("In finally block")
    # <no> <report>
    raise NullPointerException

