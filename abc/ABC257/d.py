import math
N = int(input())

X = []
Y = []
P = []
for i in range(N):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)

nums = []
ans = 5000000000
for i in range(N):
    max_num = 0
    for j in range(N):
        if i == j:
            continue
        x_num = abs(X[i] - X[j])
        y_num = abs(Y[i] - Y[j])
        max_num = max(max_num, x_num + y_num)
    print("max_num", max_num)
    value = math.ceil(float(max_num) / float(P[i]))
    print("value", value)
    ans = min(ans, value)
print(ans)