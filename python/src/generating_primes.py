def trial_division(n: int) -> list[int]:
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def sieve_of_eratosthenes(n: int) -> list[int]:
    is_prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes
