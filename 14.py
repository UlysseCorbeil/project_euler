memo = {}
def c_cz_num(n):
    if not n in memo:
        if n == 1:
            memo[n] = 1
        elif n % 2 == 0:
            memo[n] = c_cz_num(n // 2) + 1
        else:
            memo[n] = c_cz_num(3*n + 1) + 1
    return memo[n]

def t_top ():
    thresh = 1000000
    res = 0
    cand = 0
    for k in range(1, thresh + 1):
        p_gtop = c_cz_num(k)
        if p_gtop > cand:
            res = k
            cand = p_gtop
    return res

print(t_top())

