N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

mae = A[P-1:Q]
ushiro = A[R-1:S]

# print(mae)
# print(ushiro)

ans = []
mae_i = 0
ushiro_i = 0
for i in range(1, N+1):
    if i >= P and i <= Q:
        ans.append(ushiro[mae_i])
        mae_i += 1
    elif i >= R and i <= S:
        ans.append(mae[ushiro_i])
        ushiro_i += 1
    else:
        ans.append(A[i-1])
print(*ans)