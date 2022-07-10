import sys

sys.setrecursionlimit(2000000)

N, M = map(int, input().split())

dd = [list() for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    dd[a].append(b)
    dd[b].append(a)

for lis in dd:
    if len(lis) > 2:
        print("No")
        exit()

passedB = [False]*(N+1)

def dfs(v, prev):
    flag = True
    for d in dd[v]:
        if d == prev:
            continue
        if passedB[d]:
            return False
        passedB[d] = True
        if len(dd[d]) > 1:
            flag = dfs(d, v)
            if not flag:
                return flag
    return flag

for k in range(1, N+1):
    if passedB[k]:
        continue
    passedB[k] = True
    flag = dfs(k, 0)
    if not flag:
        print("No")
        exit()

print("Yes")
