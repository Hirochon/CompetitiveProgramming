n, m = map(int, input().split())
C = list(map(int, input().split()))
dp = [i for i in range(n + 1)]

for i in range(n):
    for c in C:
        if i + c <= n:
            dp[i+c] = min(dp[i+c], dp[i] + 1)
print(dp[n])
