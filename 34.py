memo = {}
def fac(n):
    if n == 1 or n == 0:
        return 1
    if n >= 2:
        memo[n] = n * fac(n - 1)
        return memo[n]

def dig_curious_facts(n):
    split = [int(k) for k in str(n)]
    sum = 0
    sub_sum = 0

    for k in split:
        sub_sum += fac(k)
        if sub_sum == n:
            sum += sub_sum

    return sum

def eval():
    UPPER = 2540160
    sum = 0
    for k in range (3 , UPPER):
        sum += dig_curious_facts(k)

    return sum
print(eval())
