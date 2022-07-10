from collections import deque

N, M = map(int, input().split())
AB = []
for i in range(M):
    ab = list(map(int, input().split()))
    AB.append(ab)
# print(AB)

graph = [[] for _ in range(N)]
for a, b in AB:
    graph[a - 1].append(b)
    graph[b - 1].append(a)
# print(graph) -> [[], [2], [1, 3, 4], [2, 4], [3, 2]]

que = deque([1])
ans = [0 for _ in range(N)]

while que:
    x = deque.popleft(que)
    for i in graph[x - 1]:
        if ans[i - 1] != 0:
            continue
        ans[i - 1] = x
        que.append(i)
for a in ans[1:]:
    if a == 0:
        print('No')
        break
else:
    print('Yes')
    print('\n'.join(map(str, ans[1:])))
