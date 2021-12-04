from itertools import product

N, M = map(int, input().split())

XY = [set() for _ in range(N+1)]
# print(XY)

for i in range(M):
    x, y = map(int, input().split())
    XY[x].add(y)
    XY[y].add(x)

# print(XY)
ans = 0

for b in product(range(2), repeat=N):
    isOK = True
    values = [v+1 for v in range(N) if b[v]]
    # print(values)
    for v1 in values:
        for v2 in values:
            # print(v1, v2)
            if v1 == v2:
                continue
            if v2 not in XY[v1]:
                isOK = False
    if isOK:
        # print(values)
        ans = max(ans, len(values))
print(ans)
