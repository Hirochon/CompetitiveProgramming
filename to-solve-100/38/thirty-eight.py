q = int(input())
X = []
Y = []
for _ in range(q):
    x = input()
    y = input()
    X.append(x)
    Y.append(y)

for k in range(q):
    x = X[k]
    y = Y[k]
    x_len = len(x)
    y_len = len(y)
    dp = [[0 for _ in range(y_len+1)] for _ in range(x_len+1)]
    for i in range(x_len):
        for j in range(y_len):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(dp[x_len][y_len])
