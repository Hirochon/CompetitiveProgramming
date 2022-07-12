N, W = map(int, input().split())
values = []
weights = []
dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
for i in range(N):
    v, w = map(int, input().split())
    values.append(v)
    weights.append(w)

for w in range(W+1):
    for i in range(N):
        # for h in range(N):
        #     for k in range(W):
        #         print(dp[h][k], end=" ")
        #     print()
        # print()
        if weights[i] <= w:
            dp[i+1][w] = max(dp[i][w - weights[i]] + values[i], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
# for h in range(N+1):
#     for k in range(W+1):
#         print(dp[h][k], end=" ")
#     print()
print(dp[N][W])
