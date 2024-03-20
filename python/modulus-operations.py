def mod_exp(a: int, b: int, m: int) -> int:
    res = 1
    a %= m
    while b > 0:
        if b & 1:
            res = (res * a) % m
        b >>= 1
        a = (a * a) % m
    return res