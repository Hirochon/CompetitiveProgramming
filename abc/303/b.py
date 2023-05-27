N, M = map(int, input().split())
A = []
for i in range(M):
    a = list(map(int, input().split()))
    A.append(a)
ANS = [[1 if i > j else 0 for i in range(N)] for j in range(N)]

# for a in ANS:
#     print(*a, sep=" ")
# 0 1 1 1
# 0 0 1 1
# 0 0 0 1
# 0 0 0 0

for i in range(M):
    for j in range(len(A[i]) - 1):
        x = A[i][j]
        y = A[i][j + 1]
        xx = max(x, y)
        yy = min(x, y)
        # print(xx, yy)
        ANS[yy - 1][xx - 1] = 0

# for a in ANS:
#     print(*a, sep=" ")

print(sum([sum(a) for a in ANS]))
