import random
import timeit

timeit.timeit('random.randint(1000, 10000)**random.randint(1000, 10000)', number=10000)
