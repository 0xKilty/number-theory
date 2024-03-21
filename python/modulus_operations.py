from common_functions import extended_euclidean

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
    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        raise ValueError("The modular inverse does not exist.")
    else:
        return (x % m + m) % m

a = 5
m = 11
inverse = mod_inverse(a, m)
print(f"The modular inverse of {a} modulo {m} is {inverse}")