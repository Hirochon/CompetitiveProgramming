N, M = map(int, input().split())
ps = set([1])
ms = [1] * (M+1)
ms[0] = 0

def primer(num):
    flag = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            ps.add(i)
            flag = False
            w = num // i
            if w > 1:
                ps.add(w)
    if flag:
        ps.add(num)

def primeFactorizer(pris):
    for pr in pris:
        if pr == 1:
            continue
        v = pr
        while v <= M:
            ms[v] = 0
            v += pr

for a in map(int, input().split()):
    primer(a)

primeFactorizer(ps)

print(sum(ms))
for i, m in enumerate(ms):
    if m == 1:
        print(i)