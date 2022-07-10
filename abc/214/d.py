import sys
import heapq
sys.setrecursionlimit(10**6)

N = int(input())
edge = []
heapq.heapify(edge)

for _ in range(N-1):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    heapq.heappush(edge, (w, u, v))

par = [-1 for _ in range(N)]

def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def unite(x, y):
    x = root(x)
    y = root(y)
    par[x] += par[y]
    par[y] = x

def size(x):
    x = root(x)
    return -par[x]

ans = 0
while edge:
    w, u, v = heapq.heappop(edge)
    ans += w * size(u) * size(v)
    unite(u, v)

print(ans)