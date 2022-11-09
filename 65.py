def c_max_digit_sum(n):

    l_n = [int(k) for k in str(n)]

    bn_sum = 0
    for k in l_n:
        bn_sum += k

    return bn_sum

# nk = ak * nk-1 + nk-2
def exp_frac_conv():
    d = 1
    n = 2
    for k in range(2, 101):
        temp = d
        ak = 0
        if k % 3 == 0:
            ak = 2 * (k // 3)
        else:
            ak = 1
        d = n
        n = ak * d + temp
    return c_max_digit_sum(n)

print(exp_frac_conv())
