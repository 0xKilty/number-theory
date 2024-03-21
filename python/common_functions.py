def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    x_prev, x, y_prev, y = 0, 1, 1, 0
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x_prev, x = x - quotient * x_prev, x_prev
        y_prev, y = y - quotient * y_prev, y_prev
    return a, x, y


def is_prime(n: int) -> bool:
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


def is_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def fast_exp(a: int, b: int) -> int:
    res = 1
    while b > 0:
        if b % 2 == 1:
            res *= a
        a *= a
        b //= 2
    return res