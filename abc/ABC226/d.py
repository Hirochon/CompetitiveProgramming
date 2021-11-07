from itertools import combinations
import math

N = int(input())

XY = [()]*N

for i in range(N):
    x, y = map(int, input().split())
    XY[i] = (x, y)

ans = set()

for xy1, xy2 in combinations(XY, 2):
    dx = xy1[0] - xy2[0]
    dy = xy1[1] - xy2[1]
    sk = math.gcd(dx, dy)
    ans.add((dx//sk, dy//sk))
    ans.add((-dx//sk, -dy//sk))

print(len(ans))
