import numpy as np

r, c = map(int, input().split())

C = [list(map(int, input().split())) for _ in range(r)]
npC = np.array(C)

kijun = npC[0].sum()
for i in range(1, r):
    if (npC[0] * npC[i]).sum() < kijun:
        npC[i] *= -1
        npC[i] += 1

# print(npC)

for i in range(c):
    kr = r / 2
    if npC[:,i].sum() < kr:
        npC[:, i] *= -1
        npC[:, i] += 1

# print(npC)
print(npC.sum())
