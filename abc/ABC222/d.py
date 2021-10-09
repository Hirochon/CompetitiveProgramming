mod = 998244353
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = 3000
dp = [1] * (M + 1)
for i in range(N):
  nx = [0] * (M + 1)
  for j in range(A[i], B[i] + 1):
    nx[j] = dp[j]
  dp = nx
  for i in range(M):
    dp[i + 1] += dp[i]
    dp[i + 1] %= mod
print(dp[M])