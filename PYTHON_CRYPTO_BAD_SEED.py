import random
secureSeed = 456
# <yes> <report> PYTHON_CRYPTO_BAD_SEED 22dcc6
random.seed(123)
# <no> <report>
random.seed(secureSeed)