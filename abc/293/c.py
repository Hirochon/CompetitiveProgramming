H, W = map(int, input().split())
A = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)

dp = [[[] for _ in range(W)] for _ in range(H)]
dp[0][0].append(set([A[0][0]]))

for i in range(H):
    for j in range(W):
        if i+1 < H and j+1 < W:
            for k in range(len(dp[i][j])):
                cp_dp_k_for_i = dp[i][j][k].copy()
                cp_dp_k_for_i.add(A[i+1][j])
                cp_dp_k_for_j = dp[i][j][k].copy()
                cp_dp_k_for_j.add(A[i][j+1])
                dp[i+1][j].append(cp_dp_k_for_i)
                dp[i][j+1].append(cp_dp_k_for_j)
        elif i+1 < H:
            for k in range(len(dp[i][j])):
                cp_dp_k_for_j = dp[i][j][k].copy()
                cp_dp_k_for_j.add(A[i+1][j])
                dp[i+1][j].append(cp_dp_k_for_j)
        elif j+1 < W:
            for k in range(len(dp[i][j])):
                cp_dp_k_for_i = dp[i][j][k].copy()
                cp_dp_k_for_i.add(A[i][j+1])
                dp[i][j+1].append(cp_dp_k_for_i)
        # print(dp)
ans = 0
for s in dp[H-1][W-1]:
    if len(s) == H+W-1:
        ans += 1
print(ans)
