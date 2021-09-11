from itertools import combinations

N = int(input())
setXY = set()

for i in range(N):
    x, y = map(int, input().split())
    setXY.add((x, y))

ans = 0

for (x1, y1), (x2, y2) in combinations(setXY, 2):
    if x1 == x2 or y1 == y2:
        continue
    if (x1, y2) in setXY and (x2, y1) in setXY:
        ans += 1

print(ans//2)