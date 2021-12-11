from itertools import permutations
from collections import deque

k = int(input())
C = deque([])
kTF = [True]*8

for i in range(k):
    r, c = map(int, input().split())
    kTF[r] = False
    C.append(c)


# print(C)
# print(C.popleft())
# print(C)
j = 0
for v in permutations(range(8), 8-k):
    listV = deque(v)
    # print(listV)
    # print(C)
    copiedC = C.copy()
    values = [listV.popleft() if kTF[i] else copiedC.popleft() for i in range(8)]
    ansC = [[0]*8 for _ in range(8)]
    flag = True
    # print(values)
    for i in range(8):
        # print(values[i], i)
        if ansC[values[i]][i] == 1:
            flag = False
            break
        for w in range(8):
            ansC[w][i] = 1
            ansC[values[i]][w] = 1
        # ansC[values[i]] = [1,1,1,1,1,1,1,1]
        x = values[i]
        y = i
        for j in range(8):
            jx = j + x
            jy = j + y
            jjx = x - j
            if jx < 8 and jy < 8:
                # print(ix, iy)
                ansC[jx][jy] = 1
            if 0 <= jjx and jjx < 8 and jy < 8:
                # print(iix, iy)
                ansC[jjx][jy] = 1
    if flag:
        # print(ansC)
        break
    # j += 1
    # if j == 2:
    #     break

# print(values)
for i in range(8):
    for j in range(8):
        if values[i] == j:
            print('Q', end="")
        else:
            print('.', end="")
    print()
