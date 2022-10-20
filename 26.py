def c_dec(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def eval_c_dec(n):

    if n < 8: return 3
    for d in c_dec(n)[::-1]:
        k = d//2
        while pow(10, k, d) != 1: k+= 1
        if d-1 == k: return d

print(eval_c_dec(1001))
