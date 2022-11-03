def gen_pent_nums (n):
    seq = []

    for k in range(1, n - 1):
        pn = k * (3 * k - 1) / 2;
        seq.append(int(pn))
    return seq

def gen_t_nums (n):
    seq = []
    for k in range(1, n - 1):
        tn = k * (k + 1) / 2;
        seq.append(int(tn))
    return seq

def gen_hexa_nums (n):
    seq = []
    for k in range(1, n - 1):
        hn = k * (2 * k - 1);
        seq.append(hn)
    return seq

def find_t_pent (n):
    pn = set(gen_pent_nums(n))
    tn = set(gen_t_nums(n))
    hn = set(gen_hexa_nums(n))

    u = pn & tn & hn

    return sorted(u)

print(find_t_pent(1000000))
