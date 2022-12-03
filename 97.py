def f_non_mers_prime(a, b, c, m):

    return (c * pow(a, b, m) + 1) % m

print(f_non_mers_prime(2, 7830457, 28433, 10**10))
