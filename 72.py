# Eulers totent function
# phi(n) = n * Pi p|n ( 1 - (1/p) )
# phi(n) = p1^k1-1 * (p1 - 1) * p2^k2-1 ... pn^kn-1(pr - 1)
def count_fracts(n):
    phi = list(range(n + 1))
    for k in range(2, n + 1):
        if phi[k] == k:
            for i in range(k, n + 1, k):
                phi[i] = phi[i] // k * (k - 1)
    return sum(phi) - 1
print(count_fracts(1000000))
