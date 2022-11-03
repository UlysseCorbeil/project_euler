def c_self_pw (n):
    sum = 0
    for k in range(1, n+1):
        sum += k ** k
    return sum

print(c_self_pw(10001487))
