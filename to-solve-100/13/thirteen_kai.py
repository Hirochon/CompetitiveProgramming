import numpy as np
R, C = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(R)])
ans = 0
for i in range(2**R):
    bit = np.array([[i>>j&1 for j in range(R)]]).T
    black = (A^bit).sum(axis=0)
    ans = max(ans, np.fmax(R-black, black).sum())
print(ans)