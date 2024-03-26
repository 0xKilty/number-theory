import numbertheory as nt

def regular_exp(a: int, b: int):
    res = a
    for _ in range(b - 1):
        res *= a
    return res

print(nt.fast_exp(31, 2))
print(regular_exp(31, 2))