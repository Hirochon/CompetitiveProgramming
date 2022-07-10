from collections import defaultdict

N, M = map(int, input().split())
H = map(int, input().split())

UV = defaultdict(list)
vis = defaultdict(bool)
for i in range(M):
    u, v = map(int, input().split())
    UV[u].append(v)
    UV[v].append(u)
    vis[u] = False
    vis[v] = False

def dfs(u, visited, parent):
    visited[u] = True
    for v in UV[u]:
        if v == parent:
            continue
        if visited[v]:
            return False
        if not dfs(v, visited, u):
            return False
    return True

dfs(1, vis, -1)
