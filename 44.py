def gen_pent_nums (n):
    seq = []

    for k in range(1, n - 1):
        pn = k * (3 * k - 1) / 2;
        seq.append(pn)
    return seq

def find_pair_pent (n):
    pn = set(gen_pent_nums(n))
    for k1 in pn:
        for k2 in pn:
            if k1 + k2 in pn and abs(k1 - k2) in pn:
                return k1, k2

p1, p2 = find_pair_pent(10000)

print(abs(p1 - p2))
