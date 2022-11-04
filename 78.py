# def gen_part_index(n):
#     return sum([[k * (3 * k - 1) // 2, k * (3 * k - 1) // 2 + k] for k in range(1, n + 1)], [])

# def p(n):
#     ind = []
#     for k in range(1, n + 1):
#         ind.append(gen_part_index(k))
#     return ind[len(ind) - 1]

# def gen_seq (n):
#     k = 0
#     ind = 0
#     flag = True
#     while p(n) > 0:
#         coeff = p(n)
#         while coeff[ind] <= k:
#             ind += 1


# print(gen_seq(1000000))

# list of generalized pentagonal numbers for generating function
k = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])

p, sgn, n, m  = [1], [1, 1, -1, -1], 0, 1e6

while p[n]>0:
    n += 1
    px, i = 0, 0
    while k[i] <= n:
        px += p[int(n - k[i])] * sgn[i%4]
        i += 1
    p.append(px % m)


print(n)
