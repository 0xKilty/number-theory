from common_functions import extended_euclidean, mod_exp


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

def order_of_number(a: int, m: int) -> int:
    for i in range(1, m):
        if mod_exp(a, i, m) == 1:
            return i
    return m - 1

a = 3
modulus = 7
print("Order of", a, "modulo", modulus, "is:", order_of_number(a, modulus))