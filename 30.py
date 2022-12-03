def sum_power_digs(n):
    list = [int(k) for k in str(n)]

    _nums = []
    for k in list:
        _nums.append(k ** 5)

    return sum(_nums)

def eval ():
    nums = []
    for k in range(2, 1000001):
        val = sum_power_digs(k)
        if val == k:
            nums.append(val)
    return sum(nums)

print(eval())
