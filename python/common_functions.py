def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    x_prev, x, y_prev, y = 0, 1, 1, 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        x_prev, x = x - q * x_prev, x_prev
        y_prev, y = y - q * y_prev, y_prev
    return a, x, y
