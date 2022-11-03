import enum


def f_fact_dig_sum(n):

    # get real factorial
    fact = 1
    for k in range(1, n + 1):
        fact *= k

    # split factorial into array
    split_fact = [int(k) for k in str(fact)]

    # sum of terms
    sum = 0
    for k in split_fact:
        sum += k

    return sum

print(f_fact_dig_sum(100))
