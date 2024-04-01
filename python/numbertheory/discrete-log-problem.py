from common_functions import mod_exp
from modulus_operations import mod_inverse, chinese_remainder_theorem
from integer_factorization import brute_force_factorization

def baby_step_giant_step(p: int, g: int, h: int, N: int):
    n = int((N ** 0.5)) + 1
    list_ = [mod_exp(g, i, p) for i in range(n + 1)]
    u = mod_inverse(mod_exp(g, n, p), p)
    x = h
    for i in range(n + 1):
        if x in list_:
            return list_.index(x) + i * n
        x = (x * u) % p


def pohlig_hellman(p, g, h, N = -1):
    if N == -1:
        N = p - 1
    factor_list = brute_force_factorization(N)
    if len(factor_list) > 1:
        moduli = []
        remainders = []
        for factor, exponent in factor_list.items():
            e = N // (factor ** exponent)
            g_i = mod_exp(g, e, p)
            h_i = mod_exp(h, e, p)
            y_i = pohlig_hellman(p, g_i, h_i, factor ** exponent)
            remainders.append(y_i)
            moduli.append(factor ** exponent)
        return chinese_remainder_theorem(moduli, remainders)
    elif len(factor_list) == 1:
        q, e = next(iter(factor_list.items()))
        x = 0
        u_i = 1
        g_i = mod_exp(g, q ** (e - 1), p)
        for i in range(e):
            h_i = mod_exp(h * u_i, q ** (e - 1 - i), p)
            x_i = baby_step_giant_step(p, g_i, h_i, q)            
            x += x_i * (q ** i)
            u_i *= mod_inverse(mod_exp(g, x_i * (q ** i), p), p)
        return x
