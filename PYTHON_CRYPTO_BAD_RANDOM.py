import random
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.random())
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.uniform(0,100))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.randint(0,100))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.randrange(100))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.getrandbits(10))

items = [1,2,3,4,5]
k = 1
low = 0
high = 1
mode = 0.5
alpha = 0.2
beta = 0.8
mu = 1
sigma = 0.5
kappa = 0.1
lambd = 0.4
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.choice(items))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.shuffle(items))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.sample(items, k))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.triangular(low, high, mode))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.betavariate(alpha, beta))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.expovariate(lambd))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.gammavariate(alpha, beta))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.gauss(mu, sigma))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.lognormvariate(mu, sigma))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.normalvariate(mu, sigma))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.vonmisesvariate(mu, kappa))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.paretovariate(alpha))
# <yes> <report> PYTHON_CRYPTO_BAD_RANDOM a49606 <yes> <report> PYTHON_INFORMATION_LEAK wedqb9 <yes> <report> PYTHON_LOGGING_SYSTEM_OUTPUT 1257de
print (random.weibullvariate(alpha, beta))
