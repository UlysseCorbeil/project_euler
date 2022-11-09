
# e = floor( n + b / d) * c - a
# f = floor( n + b / d) * d - b
def _c_farey_seq():
    L = 12000
    a = 1
    b = 3
    c = 4000
    d = 11999

    res = 0

    while not(c == 1 and d == 2):
        res += 1
        k = (L + b) // d
        e = k * c - a
        f = k * d - b
        a = c
        b = d
        c = e
        d = f
    return res

print(_c_farey_seq())
