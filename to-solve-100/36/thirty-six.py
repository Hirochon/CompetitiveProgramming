N, W = map(int, input().split())
Values = []
Weights = []
for i in range(N):
    v, w = map(int, input().split())
    Values.append(v)
    Weights.append(w)

dp = [[0 for _ in range(N+1)] for _ in range(W+1)]

for i in range(W+1):
    for j in range(N):
        # for k in range(N+1):
        #     for h in range(W+1):
        #         print("{:>2d}".format(dp[h][k]), end=" ")
        #     print()
        # print()
        if Weights[j] <= i:
            dp[i][j+1] = max(dp[i - Weights[j]][j+1] + Values[j], dp[i][j])
        else:
            dp[i][j+1] = dp[i][j]

# for k in range(N+1):
#     for h in range(W+1):
#         print("{:>2d}".format(dp[h][k]), end=" ")
#     print()
print(dp[W][N])
