import math
N = int(input())

X = []
Y = []
P = []
for _ in range(N):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)

XY = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        x = abs(X[i] - X[j])
        y = abs(Y[i] - Y[j])
        XY[i][j] = math.ceil((x + y) / P[i])

# print(XY)

for k in range(N):
    for i in range(N):
        for j in range(N):
            XY[i][j] = min(XY[i][j], max(XY[i][k], XY[k][j]))

# print(XY)

ans = 5000000000
for i in range(N):
    ans = min(ans, max(XY[i]))
print(ans)