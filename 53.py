import math
fac = math.factorial

def bin_coef(n, k):
    return fac(n) // (fac(k) * fac(n - k))

def find_nums():
    count = 0
    for n in range(23, 101):
        for k in range(4, n - 3):
            val = bin_coef(n, k)
            if val > 1000000:
                count += 1
    return count

print(find_nums())
