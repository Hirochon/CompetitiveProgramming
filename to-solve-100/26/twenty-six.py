from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())

tree = defaultdict(list)
root = set([1])
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

point = defaultdict(int)
for i in range(Q):
    p, x = map(int, input().split())
    point[p] += x

past = set()
def dfs(node, parent = 0):
    if node in past:
        return
    past.add(node)
    point[node] += point[parent]
    for child in tree[node]:
        dfs(child, node)

dfs(1)

for i in range(1, N+1):
    if i != N:
        print(point[i], end=' ')
        continue
    print(point[i])
