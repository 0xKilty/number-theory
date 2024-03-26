import numbertheory as nt
import time
import random


def regular_exp(a: int, b: int):
    res = a
    for _ in range(b - 1):
        res *= a
    return res


def python_exp(a: int, b: int):
    return a ** b


def measure_time(func, iterations):
    start_time = time.perf_counter()
    for _ in range(iterations):
        func(random.randint(1000, 10000), random.randint(1000, 10000))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time

regular_exp_time = measure_time(nt.fast_exp, 10000)
print("Regular Exp Time:", regular_exp_time)

python_exp_time = measure_time(python_exp, 10000)
print("Python Exp Time:", python_exp_time)
