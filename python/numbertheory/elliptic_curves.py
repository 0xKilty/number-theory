from modulus_operations import mod_exp

def point_addition(p, q, a, p_mod):
    if p is None:
        return q
    elif q is None:
        return p
    elif p[0] == q[0] and (p[1] + q[1]) % p_mod == 0:
        return None
    else:
        if p != q:
            s = ((q[1] - p[1]) * pow(q[0] - p[0], -1, p_mod)) % p_mod
        else:
            s = ((3 * pow(p[0], 2) + a) * pow(2 * p[1], -1, p_mod)) % p_mod
        x_r = (pow(s, 2) - p[0] - q[0]) % p_mod
        y_r = (s * (p[0] - x_r) - p[1]) % p_mod
        return x_r, y_r

def point_doubling(p, a, p_mod):
    if p is None:
        return None
    elif p[1] == 0:
        return None
    else:
        s = ((3 * pow(p[0], 2) + a) * pow(2 * p[1], -1, p_mod)) % p_mod
        x_r = (pow(s, 2) - 2 * p[0]) % p_mod
        y_r = (s * (p[0] - x_r) - p[1]) % p_mod
        return x_r, y_r