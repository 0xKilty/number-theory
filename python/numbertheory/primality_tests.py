import random
from .modulus_operations import mod_exp

def is_prime_brute_force(n: int) -> bool:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_prime_fermat(n: int, iterations: int = 5) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True

    for _ in range(iterations):
        a = random.randint(2, n - 1)
        if mod_exp(a, n, n) != a:
            return False
    return True


def is_prime_rabin_miller(n: int, k: int = 5) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True
