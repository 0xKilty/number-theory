from .common_functions import extended_euclidean

def mod_exp(a: int, b: int, m: int) -> int:
    res = 1
    a %= m
    while b > 0:
        if b & 1:
            res = (res * a) % m
        b >>= 1
        a = (a * a) % m
    return res


def mod_inverse(a: int, m: int) -> int:
    x, _, gcd = extended_euclidean(a, m)
    if gcd != 1:
        raise ValueError("The modular inverse does not exist.")
    return x % m if x >= 0 else x + m

def chinese_remainder_theorem(moduli: list[int], remainders: list[int]) -> list[int]:
    sum = 0
    prod = 1
    for n_i in moduli:
        prod *= n_i
    for n_i, a_i in zip(moduli, remainders):
        p = prod // n_i
        sum += a_i * mod_inverse(p, n_i) * p
    return sum % prod