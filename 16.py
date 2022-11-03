def f_dig_sum(n):

    # exponent
    l_num = 2 ** n

    # break the integer and rep as list
    list = [int(k) for k in str(l_num)]
    sum = 0
    for val in list:
        sum += val
    return sum

print(f_dig_sum(1000000))
