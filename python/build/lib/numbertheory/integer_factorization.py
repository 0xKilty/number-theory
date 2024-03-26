def prime_factor_decomp(n: int) -> list[int]:
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

print(prime_factor_decomp(3141592653589))