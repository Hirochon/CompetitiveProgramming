from itertools import product
from collections import defaultdict

N, K = map(int, input().split())
S = []

for i in range(N):
    s = input()
    S.append(s)
ans = 0
for p in product(range(2), repeat=N):
    dd = defaultdict(int)
    useS = ""
    for i, pp in enumerate(p):
        if pp:
            useS += S[i]
    for s in useS:
        dd[s] += 1
    i_ans = 0
    for key, value in dd.items():
        if value == K:
            i_ans += 1
    ans = max(ans, i_ans)
print(ans)