import math

N = int(input())

ans = 0
NList = []
for i in range(N):
    x, y = map(int, input().split())
    NList.append((x, y))

for i in range(N):
    for j in range(N):
        if i <= j:
            continue
        x1, y1 = NList[i]
        x2, y2 = NList[j]
        ans_n = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        if ans < ans_n:
            ans = ans_n

print(ans)
