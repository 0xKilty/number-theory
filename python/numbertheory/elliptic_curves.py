from modulus_operations import mod_exp

def point_addition(P: tuple[int, int], Q: tuple[int, int], a: int, b: int) -> tuple[float, float]:
    if P is None: return Q
    if Q is None: return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 == -y2:
        return None

    if x1 == x2 and y1 == y2:
        m = (3 * x1 ** 2 + a) / (2 * y1)
    else:
        m = (y2 - y1) / (x2 - x1)

    x3 = m ** 2 - x1 - x2
    y3 = m * (x1 - x3) - y1

    return (x3, y3)

def point_multiplication(P: tuple[int, int], k: int, a: int, b: int) -> tuple[float, float]:
    Q = None
    R = P

    while k > 0:
        if k % 2 == 1:
            Q = point_addition(Q, R, a, b)
        R = point_addition(R, R, a, b)
        k //= 2

    return Q

def point_addition_mod(P: tuple[int, int], Q: tuple[int, int], a: int, b: int, mod: int) -> tuple[int, int]:
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 == (-y2 % mod):
        return None

    if x1 == x2:
        m = ((3 * x1 * x1 + a) * mod_exp(2 * y1, mod - 2, mod)) % mod
    else:
        m = ((y2 - y1) * mod_exp(x2 - x1, mod - 2, mod)) % mod

    x3 = (m * m - x1 - x2) % mod
    y3 = (m * (x1 - x3) - y1) % mod

    return (x3, y3)

def point_multiplication_mod(P: tuple[int, int], k: int, a: int, b: int, mod: int) -> tuple[int, int]:
    Q = None
    R = P

    while k > 0:
        if k & 1:
            Q = point_addition_mod(Q, R, a, b, mod)
        R = point_addition_mod(R, R, a, b, mod)
        k = k >> 1

    return Q
