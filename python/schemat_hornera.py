"""
Złożoność obliczeniowa:
    o(n) - while wykona się n razy, gdzie n to długość wsp, omega(n), theta(n)
Złożoność pamięciowa:
    o(1), omega(1), theta(1) - same stałe liczby pamięci
"""


def horner(x, wsp):
    y = 0
    i = len(wsp) - 1
    operations = 0
    while i>=0:
        operations += 2
        y = wsp[i] + x*y
        i = i-1
    return y, operations

def noob_way(x, wsp):
    y = 0
    operations = 0
    for id, a in enumerate(wsp):
        operations += id + 1
        y += pow(x,id) * a
    return y, operations

print(horner(2, [1, 2, 3, 1]))
print(noob_way(2, [1, 2, 3, 1]))
