def d(n):
    p_d = []
    for k in range(1, n + 1):
        if k < n and n % k == 0:
            p_d.append(k)

    sum = 0
    for k in p_d:
        sum += k
    return sum


def eval_am_d():
    sum = 0
    for k in range(0, 10000):
        res = d(k)
        comp = d(res)

        if comp == k and res != comp:
            sum += k
    return sum

print(eval_am_d())
