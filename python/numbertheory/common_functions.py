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
    return x, y, a


def euler_totient(n: int) -> int:
    if n <= 0:
        return 0
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count


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
