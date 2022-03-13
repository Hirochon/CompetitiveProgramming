from collections import defaultdict

N = int(input())
X = []
Y = []
dd = defaultdict(list)
for i in range(N):
    x, y = map(int, input().split())
    dd[y].append(x)
    X.append(x)
    Y.append(y)

S = input()
dd2 = defaultdict(list)

for i, s in enumerate(S):
    y = Y[i]
    dd2[y].append(s)

setY = set(Y)

for y in setY:
    xList = dd[y]
    sList = dd2[y]
    xsDict = {}
    for x, s in zip(xList, sList):
        xsDict[x] = s
    sortedXList = sorted(xList)
    flag1 = False
    for x in sortedXList:
        if xsDict[x] == 'R':
            flag1 = True
        if xsDict[x] == 'L':
            if flag1:
                print('Yes')
                exit()
print('No')
