m = int(input())

kijun = set()
initX = 0
initY = 0
for mm in range(m):
    x, y = map(int, input().split())
    if not mm:
        initX = x
        initY = y
    kijun.add((x - initX, y - initY))

mLength = len(kijun)
n = int(input())
inputValues = []
for nn in range(n):
    x, y = map(int, input().split())
    inputValues.append((x, y))

ans = (0, 0)
# print(kijun)
for (ix, iy) in inputValues:
    nSum = 0
    for (kix, kiy) in inputValues:
        kix -= ix
        kiy -= iy
        if (kix, kiy) in kijun:
            nSum += 1
    if mLength == nSum:
        # print(ix, iy)
        print(ix - initX, iy - initY)
        exit()
