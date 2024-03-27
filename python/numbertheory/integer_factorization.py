from common_functions import gcd, mod_exp


def brute_force_factorization(n: int) -> list[int]:
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors


def fermat_factorization(n: int) -> tuple[int, int]:
    a = int(n ** 0.5) + 1
    b2 = a * a - n
    while not int(b2 ** 0.5) ** 2 == b2:
        a += 1
        b2 = a * a - n
    b = int(b2 ** 0.5)
    p = a + b
    q = a - b
    return p, q


def pollards_p_minus_one_factorization(n: int, b: int) -> tuple[int, int]:
    a = 2
    for j in range(2, b + 1):
        a = mod_exp(a, j, n)
    p = gcd(a - 1, n)
    return p
