from collections import defaultdict
import heapq

N, M = map(int, input().split())

dd = defaultdict(set)
c = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    if not b in dd[a]:
        dd[a].add(b)
        c[b] += 1

q = []
heapq.heapify(q)

for i in range(1, N+1):
    if c[i] == 0:
        heapq.heappush(q, i)

s = []
while q:
    x = heapq.heappop(q)
    s.append(x)
    print(s, q, x, dd)
    for v in dd[x]:
        if c[v] == 0:
            continue
        c[v] -= 1
        if c[v] == 0:
            heapq.heappush(q, v)

if sum(c) == 0:
    print(s)
else:
    print(-1)