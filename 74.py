def fac(n, memo = {}):
    if n == 1 or n == 0:
        return 1
    if n >= 2:
        memo[n] = n * fac(n - 1)
        return memo[n]

_count = 0
def chain_facs(n, chain_memo = {}):
    _n = [int(k) for k in str(n)]
    global _count
    sum = 0
    for k in _n:
        sum += fac(k)
    chain_memo[n] = sum
    if chain_memo[n] != list(chain_memo.keys())[0] and chain_memo[n] not in chain_memo:
        chain_memo[n] = chain_facs(sum)
    if len(chain_memo) == 60:
        _count += 1
    return chain_memo[n]
    
