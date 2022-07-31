from collections import defaultdict
N, M = map(int, input().split())

uv_dd = defaultdict(list)
unique_set = set()
for _ in range(M):
    u, v = map(int, input().split())
    uv_dd[u].append(v)
    uv_dd[v].append(u)
    unique_set.add(u)
    unique_set.add(v)

ans_set = set()

while len(unique_set) > 0:
    u = unique_set.pop()
    for v in uv_dd[u]:
        for w in uv_dd[v]:
            if u in uv_dd[w]:
                ans = [u, v, w]
                ans.sort()
                ans_set.add(tuple(ans))

print(len(ans_set))
