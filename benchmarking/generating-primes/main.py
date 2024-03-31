import numbertheory as nt
from timeit import timeit
from memory_profiler import profile, memory_usage

@profile
def main():
    time_function_1 = timeit(lambda: nt.sieve_of_eratosthenes(10000), number=100)
    time_function_2 = timeit(lambda: nt.trial_division(10000), number=100)
    print("Time taken by function 1:", time_function_1)
    print("Time taken by function 2:", time_function_2)

    mem_usage_function_1 = memory_usage((nt.sieve_of_eratosthenes, (10000000,), {}), interval=0.5)
    mem_usage_function_2 = memory_usage((nt.trial_division, (10000000,), {}), interval=0.5)
    print("Memory usage of function 1:", max(mem_usage_function_1), "MB")
    print("Memory usage of function 2:", max(mem_usage_function_2), "MB")

if __name__ == "__main__":
    main()
