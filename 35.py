import math

def is_prime(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def gen_rots(n):
    rots_n = set()
    c_set = set()
    _p_rots = {}
    set_elems = {}
    for k in range (len(str(n))):
        rot = int(str(n)[k:] + str(n)[:k])
        rots_n.add(rot)
        _p_rots[n] = rots_n
    for k in _p_rots:
        set_elems = dict.fromkeys(_p_rots[k], k)
    for elem in set_elems:
        print(set_elems)
        if is_prime(elem) and is_prime(set_elems[elem]):
            c_set.add(elem)
    return c_set

def eval_p_circ():
    S = []
    _S = set()
    for k in range(2, 101):
        if is_prime(k):
            S.append(gen_rots(k))

    _S = set().union(*S)
    print(sorted(_S))
    return len(_S)

print(eval_p_circ())
