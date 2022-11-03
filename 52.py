def check_dig(n):
    d = n * 2
    t = n * 3
    q = n * 4
    c = n * 5
    s = n * 6

    n_b = [int(k) for k in str(n)]
    d_b = [int(k) for k in str(d)]
    t_b = [int(k) for k in str(t)]
    q_b = [int(k) for k in str(q)]
    c_b = [int(k) for k in str(c)]
    s_b = [int(k) for k in str(s)]

    chosen = 0
    if (set(n_b) == set(d_b) and
        set(d_b) == set(t_b) and
        set(t_b) == set(q_b) and
        set(q_b) == set(c_b) and
        set(c_b) == set(s_b)):
            chosen = n
    return chosen

def test():
    sml = []
    for k in range(1, 1000000):
        c = check_dig(k)
        if c != 0:
            sml.append(c)
    return sml

print(test())
