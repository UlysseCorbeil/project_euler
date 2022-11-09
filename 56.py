def c_max_digit_sum(a,b):

    l_ab = [int(k) for k in str(a**b)]

    ba_sum = 0
    for k in l_ab:
        ba_sum += k

    return ba_sum

def f_max_sum():
    _max = []
    for a in range(100):
        for b in range(100):
            _max.append(c_max_digit_sum(a,b))
    return max(_max)
print(f_max_sum())
