N = int(input())
C = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(N)]
# dp[0][0] = 1
dp[1][C[0]] = 1

for i in range(1, N-1):
    c = C[i]
    for j in range(21):
        if dp[i][j] != 0:
            if j - c >= 0:
                dp[i+1][j - c] += dp[i][j]
            if j + c <= 20:
                dp[i+1][j + c] += dp[i][j]

# for i in range(21):
#     for j in range(N):
#         print(dp[j][i], end=" ")
#     print()
print(dp[N-1][C[-1]])
