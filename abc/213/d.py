import bisect
import sys
sys.setrecursionlimit(300000)


N = int(input())
dfsList = [[] for _ in range(N+1)]
ans = []

for i in range(N-1):
    A, B = map(int, input().split())
    dfsList[A].append(B)
    dfsList[B].append(A)

[dfsList[i].sort() for i in range(N+1)]

def dfs(next, prev):
    ans.append(next)
    for v in dfsList[next]:
        if v != prev:
            dfs(v, next)
            ans.append(next)

dfs(1, -1)

print(*ans)