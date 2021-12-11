from itertools import combinations
from math import sqrt, factorial

N = int(input())

xy = []

for i in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))

ans = 0

for i, (v1, v2) in enumerate(combinations(range(N), 2)):
    v = sqrt((xy[v1][0] - xy[v2][0])**2 + (xy[v1][1] - xy[v2][1])**2)
    # print(v)
    ans = (v-ans) / (i+1) + ans
    # print(v1, v2)
    # print(ans)

print(ans*(N-1))
