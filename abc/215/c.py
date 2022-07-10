from itertools import permutations

S, K = input().split()
KInt = int(K)

SList = sorted(S)

ansSet = set()
i = 0

for s in permutations(SList):
    if s not in ansSet:
        ansSet.add(s)
        if i+1 == KInt:
            print(*s, sep="")
            break
        i += 1
