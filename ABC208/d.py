N, M = map(int, input().split())
dp = [[1e18 for _ in range(N)] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = c
    dp[a][a] = 0
    dp[b][b] = 0

ans = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            if 1e18 != dp[i][j]:
                ans += dp[i][j]

print(ans)
