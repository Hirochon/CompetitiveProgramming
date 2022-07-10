import numpy as np

H, W = map(int, input().split())
A = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)

anp = np.array(A)

for i in range(anp.T.shape[0]):
    for j in range(anp.T.shape[1]):
        print(anp.T[i, j], end=" ")
    print()
