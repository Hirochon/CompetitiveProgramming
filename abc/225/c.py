import numpy as np

N, M = map(int, input().split())

B = [[0]*M for _ in range(N)]

for i in range(N):
    b = list(map(int, input().split()))
    for j in range(M):
        B[i][j] = b[j]

start = B[0][0]

ansList = np.arange(7000).reshape(1000, 7) + 1

startN = (start-1) // 7
startM = (start-1) % 7

for ii, i in enumerate(range(startN, startN+N)):
    for jj, j in enumerate(range(startM, startM+M)):
        # print(i, j)
        # print(ansList[i, j])
        if j > 6:
            print("No")
            exit()
        if B[ii][jj] != ansList[i, j]:
            print("No")
            exit()
print("Yes")