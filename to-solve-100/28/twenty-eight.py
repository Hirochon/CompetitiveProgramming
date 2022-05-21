import sys
sys.setrecursionlimit(10**6)

n = int(input())

G = {}
ans = { i:-1 for i in range(1, n+1) }
for i in range(n):
    u, k, *v = map(int, input().split())
    if k:
        G[u] = v
    else:
        G[u] = []

def bfs(d, v_num):
    if ans[v_num] != -1:
        return
    ans[v_num] = d
    print(ans)
    for v in G[v_num]:
        print(d+1, v)
        bfs(d+1, v)
    
bfs(0, 1)

# for i in range(1, n+1):
#     print(i, ans[i])
