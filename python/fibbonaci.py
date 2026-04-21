"""
Złożoność czasowa:
    iter: O(n), omega(n), theta(n)
    rek: 0(n^2), omega(n^2), theta(n^2)
    rek_mem: 0(n), omega(n), theta(n^2)

Złożoność pamięciowa:
    iter: theta(1)
    rek: theta(n)
    rek_mem: theta(n) (ale gorszy niż rek)
"""
def fib_iter(n):
    a0 = 1
    a1 = 1
    i = 2
    while i < n:
        global iter
        iter +=1
        a0, a1 = a1, a0 + a1
        i+=1
    return a1

def fib_rek(n):
    global iter
    iter +=1
    if n <=2:
        return 1
    return fib_rek(n-1) + fib_rek(n-2)

def _fib_rek_mem(n, mem):
    global iter
    iter +=1
    if n <3:
        mem[n] = 1
    if mem[n] != 0:
        return mem[n]
    mem[n] = _fib_rek_mem(n-1, mem) + _fib_rek_mem(n-2, mem)
    return mem[n]

def fib_rek_mem(n):
    mem = [0 for _ in range(n+1)]
    return _fib_rek_mem(n, mem)

iter = 0
print(fib_iter(6), iter)
iter = 0
print(fib_rek(6), iter)
iter = 0
print(fib_rek_mem(6), iter)

