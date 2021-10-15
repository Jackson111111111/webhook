try:
    print("Hello, world!")
# <yes> <report> PYTHON_ERROR_HANDLING_EMPTY_CATCH b0eb34
except ZeroDivisionError:
    pass    # empty catch
else:
    print("Raising generic Error")
    # <yes> <report> PYTHON_ERROR_HANDLING_BROAD_THROW 7a492c
    raise Exception
finally:
    print("In finally block")
    # <no> <report>
    raise NullPointerException