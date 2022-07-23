N, M = map(int, input().split())
X = list(map(int, input().split()))
bonus = {}
bonus_set = set()
for i in range(M):
    c, y = map(int, input().split())
    bonus[c] = y
    bonus_set.add(c)

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
# dp[0][0] = -1
counter = 0
for i in range(N):
    for j in range(N):
        if j > i:
            break
        if dp[i][j] == 0 and i != 0 and j != 0:
            continue
        ## 表が出たとき
        if j+1 in bonus_set:
            dp[i+1][j+1] = max(dp[i][j] + X[i] + bonus[j+1], dp[i+1][j+1])
        else:
            dp[i+1][j+1] = max(dp[i][j] + X[i], dp[i+1][j+1])
        ## 裏が出たとき
        dp[i+1][0] = max(dp[i][j], dp[i+1][0])
# print()
# for j in range(N+1):
#     for i in range(N+1):
#         print(dp[i][j], end=" ")
#     print()
print(max(list(map(lambda x: max(x), dp))))
