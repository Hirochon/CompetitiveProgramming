N = int(input())
X, Y = map(int, input().split())

dp = [[N+1]*(Y+1) for _ in range(X+1)]
dp[0][0] = 0

AB = [()]*N

for i in range(N):
    A, B = map(int, input().split())
    AB[i] = (A, B)

for (A, B) in AB:
    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            h = min(A+i, X)
            w = min(B+j, Y)
            dp[h][w] = min(dp[h][w], dp[i][j]+1)

ans = dp[X][Y]
if ans >= N+1:
    print(-1)
else:
    print(ans)