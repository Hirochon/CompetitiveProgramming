from collections import deque

S = input()
K = int(input())

xNum = 0
dNum = 0

maxD = 0
train = deque([])
v = "X"

for i in range(len(S)):
    if S[i] == "X":
        xNum += 1
        maxD = max(xNum, maxD)
        train.append("X")
    else:
        train.append(".")
        dNum += 1
        if K < dNum:
            while v == "X":
                v = train.popleft()
                if v == "X":
                    xNum -= 1
                else:
                    dNum -= 1
            v = "X"
    # print(maxD)

print(maxD+dNum)
