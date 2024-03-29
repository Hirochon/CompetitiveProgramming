from collections import deque

n = int(input())
K = 0
G = {}
ans = { i:-1 for i in range(1, n+1) }
for i in range(n):
    u, k, *v = map(int, input().split())
    K += k
    if k:
        G[u] = v
    else:
        G[u] = []

queue = deque([{1:0}])
visited = [False] * (n+1)

while queue.__len__():
    v_dict = queue.pop()
    v_num = list(v_dict.keys())[0]
    if visited[v_num]:
        continue
    visited[v_num] = True
    ans[v_num] = v_dict[v_num]
    for v in G[v_num]:
        queue.appendleft({v:v_dict[v_num]+1})

for i, v in ans.items():
    print(i, v)
