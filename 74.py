def fac(n, memo = {}):
    if n == 1 or n == 0:
        return 1
    if n >= 2:
        memo[n] = n * fac(n - 1)
        return memo[n]

_chain_memo = {}
def chain_facs(n, chain_memo = {}):
    _n = [int(k) for k in str(n)]
    global _chain_memo
    sum = 0
    for k in _n:
        sum += fac(k)
    chain_memo[n] = sum
    if chain_memo[n] != list(chain_memo.keys())[0] and chain_memo[n] not in chain_memo:
        chain_memo[n] = chain_facs(sum)
    _chain_memo = chain_memo
    return chain_memo[n]
print(chain_facs(169))
print(_chain_memo)
