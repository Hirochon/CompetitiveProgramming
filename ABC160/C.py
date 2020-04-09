K, N = map(int, input().split())
A = list(map(int, input().split()))
A.append(K - A[-1] + A[0])
sa_max = A[-1]
for i in range(N - 1):
    sa = A[i + 1] - A[i]
    if sa_max < sa:
        sa_max = sa
print((A[-2] - A[0]) + A[-1] - sa_max)
