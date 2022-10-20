import math

def c_seq(n):
    t_index = 0
    t_nums = []
    for k in range(1, n + 1):
         t_index += k
         t_nums.append(t_index)
    return t_nums

def c_factors(n):
    return sum(2 for x in range(1, round(math.sqrt(n)+1)) if not n % x)

def f_tnum (n):
    tnums = c_seq(n)
    thresh = 500
    for k in tnums:
        if c_factors(k) >= thresh:
            return k

print(f_tnum(100000))

