from collections import defaultdict

N, M = map(int, input().split())

dd = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    dd[a].append(b)
    dd[b].append(a)

points = set()
setted = set()

for i, lis in dd.items():
    if len(lis) > 2:
        print("No")
        exit()
    if len(lis) == 1:
        points.add(i)

passed = set()

def dfs(v, prev):
    for d in dd[v]:
        if d == prev:
            continue
        if d in passed:
            print("No")
            exit()
        passed.add(d)
        if len(dd[d]) > 1:
            dfs(d, v)

for p in points:
    if p in passed:
        continue
    passed.add(p)
    dfs(p, 0)

print("Yes")
