from collections import defaultdict
from itertools import combinations

ddM = defaultdict(list)
ddH = defaultdict(list)
N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    ddH[x].append(y)
    ddM[y].append(x)

ans = 0

for hh in ddH:
    h = ddH[hh]
    for ch in combinations(h, 2):
        for mm in ddM:
            m = ddM[mm]
            for cm in combinations(m, 2):
                if ch == cm:
                    ans += 1
print(ans/2)