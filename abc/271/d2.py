N, S = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0 for _ in range(N)] for _ in range(10000)]

for i in range(N):
    dp[i][A[i]] += A[i]
    dp[i][B[i]] += B[i]
