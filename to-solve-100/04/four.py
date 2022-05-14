from itertools import combinations

N, M = map(int, input().split())

mm = [m for m in range(M)]

A = []

for i in range(N):
    a = [aa for aa in map(int, input().split())]
    A.append(a)

ans = 0

for (m1, m2) in combinations(mm, 2):
    mMax = 0
    for i in range(N):
        mMax += max(A[i][m1], A[i][m2])
    if ans < mMax:
        ans = mMax
print(ans)
