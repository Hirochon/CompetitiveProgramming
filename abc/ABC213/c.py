import bisect

H, W, N = map(int, input().split())

A, B = [], []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

xLabel = {x:i+1 for i, x in enumerate(sorted(list(set(A))))}
yLabel = {y:i+1 for i, y in enumerate(sorted(list(set(B))))}

for i in range(N):
    print(xLabel[A[i]], yLabel[B[i]])
