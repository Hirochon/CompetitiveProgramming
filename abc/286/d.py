N, X = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[False] * (X+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(B[i]+1):
        if A[i]*j < X+1:
            dp[i+1][A[i]*j] = True

# for i in range(N+1):
#     print(*dp[i])
#     print()

for i in range(1, N):
    for j in range(X+1):
        if dp[i][j]:
            for k in range(B[i]+1):
                if j + k*A[i] < X+1:
                    dp[i+1][j + k*A[i]] = True

# for i in range(N+1):
#     print(*dp[i])
#     print()

for i in range(1, N+1):
    if dp[i][X]:
        print("Yes")
        exit()
print("No")
