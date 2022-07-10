from collections import deque

N, X = map(int, input().split())
S = input()

newS = deque([])

flag = False
for s in S:
    if s == 'R' or s == 'L':
        flag = True
        newS.append(s)
    else:
        if flag:
            newS.pop()
            if newS:
                if newS[-1] == 'U':
                    flag = False
            else:
                flag = False
        else:
            newS.append(s)
# print(newS)

for s in newS:
    if s == 'U':
        if X % 2 == 0:
            X //= 2
        else:
            X -= 1
            X //= 2
    elif s == 'R':
        X *= 2
        X += 1
    else:
        X *= 2

print(X)
