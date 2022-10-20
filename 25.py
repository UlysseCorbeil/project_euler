import math

def c_fib(n, memo = {0: 0, 1: 1}):
    if n not in memo:
        memo[n] = c_fib(n - 1, memo) + c_fib(n - 2, memo)
    return memo[n]

def eval_c_fib():
    ind = 0
    for k in range(1, 10000):
        dig = int(math.log10(c_fib(k))) + 1
        if dig == 1000:
            ind = k
            break
    return ind

print(eval_c_fib())
