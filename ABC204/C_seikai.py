import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

p = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    p[a].append(b)


def dfs(s):
    if g[s]:
        return
    g[s] = True
    for ss in p[s]:
        dfs(ss)


ans = 0

for s in range(1, N + 1):
    g = [False for _ in range(N + 1)]
    dfs(s)
    ans += sum(g)

print(ans)
