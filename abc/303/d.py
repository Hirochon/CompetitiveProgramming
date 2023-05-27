
X, Y, Z = map(int, input().split())
S = input()
dp = [[0 for _ in range(len(S) + 1)] for _ in range(2)]
dp[1][0] = Z
for i, s in enumerate(S):
    # print(s)
    if s == "a":
        dp[0][i+1] = min(dp[0][i] + X, dp[1][i] + Y + Z, dp[1][i] + Z + X)
        dp[1][i+1] = min(dp[0][i] + X + Z, dp[1][i] + Y)
    if s == "A":
        dp[0][i+1] = min(dp[1][i] + Z + X, dp[0][i] + Y)
        dp[1][i+1] = min(dp[1][i] + X, dp[0][i] + Z + X, dp[0][i] + Y + Z)
    # print(dp)
print(min(dp[0][len(S)], dp[1][len(S)]))
