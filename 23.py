def c_non_abun_nums(n):
    sum_divs = 1
    for x in range(2, (n // 2 + 1)):
        if n % x == 0:
            sum_divs += x
    return sum_divs > n

def eval_abun_nums():

    abun_nums = [k for k in range(12, 28124) if c_non_abun_nums(k)]

    abun_sums = set([])
    for x in abun_nums:
        for y in abun_nums:
            dxdy = x + y
            if dxdy > 28123:
                break
            else:
                abun_sums.add(dxdy)

    non_abun_sum = [k for k in range(28124) if k not in abun_sums]

    return sum(non_abun_sum)

print(eval_abun_nums())
