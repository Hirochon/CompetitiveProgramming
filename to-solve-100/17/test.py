import numpy as np
ans = [[0 for _ in range(8)] for _ in range(8)]

values = [1, 4, 2, 6, 5, 3, 7, 0]
ansC = np.array(ans.copy())
flag = True
# print(values)
for i in range(8):
    print(values[i], i)
    if ansC[values[i], i] == 1:
        flag = False
        break
    ansC[:, i] = 1
    ansC[values[i], :] = 1
    x = values[i]
    y = i
    for j in range(8):
        jx = j + x
        jy = j + y
        jjx = x - j
        if jx < 8 and jy < 8:
            # print(ix, iy)
            ansC[jx, jy] = 1
        if 0 <= jjx and jjx < 8 and jy < 8:
            # print(iix, iy)
            ansC[jjx, jy] = 1
    print(ansC)
print(values)
print(ansC)
