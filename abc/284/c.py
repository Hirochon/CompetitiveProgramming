from collections import defaultdict, deque
N, M = map(int, input().split())
UV = []

n_map = {i: 0 for i in range(1, N+1)}
# print(n_map)

relation = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    UV.append((u, v))
    relation[u].append(v)
    relation[v].append(u)

passed = set()
for i in range(1, N+1):
    if i in passed:
        continue
    passed.add(i)
    n_map[i] = i
    tansaku = deque(relation[i].copy())
    while tansaku:
        t = tansaku.popleft()
        if t in passed:
            continue
        passed.add(t)
        n_map[t] = i
        for r in relation[t]:
            if r in passed:
                continue
            tansaku.append(r)

print(len(set(n_map.values())))
