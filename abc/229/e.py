N, M = map(int, input().split())

relation = {v+1: {0} for v in range(N)}

print(relation)

for i in range(M):
    a, b = map(int, input().split())
    relation[a].add(b)
    relation[b].add(a)

ans = 0

for i in range(1, N+1):
    if len(relation[i]) == 1:
        ans += 1
