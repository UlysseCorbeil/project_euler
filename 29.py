def c_seq(a, b):

    ic_set = set()
    for x in range(a, b + 1):
        for k in range(a, b + 1):
            ic_set.add(x ** k)
    return len(ic_set)

print(c_seq(2,100))
