from modulus_operations import mod_exp

def point_addition(P, Q, a, b):
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

def point_multiplication(P, k, a, b):
    Q = None
    R = P

    while k > 0:
        if k % 2 == 1:
            Q = point_addition(Q, R, a, b)
        R = point_addition(R, R, a, b)
        k //= 2

    return Q
