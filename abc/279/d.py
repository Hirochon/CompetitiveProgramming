MAX_NUM = 10 ** 18
MIN_NUM = 0
A, B = map(int, input().split())

def calc(x):
    return B*x + A/(1+x)**0.5

minT = MIN_NUM
maxT = MAX_NUM
t = (minT + maxT) // 2

minV = calc(minT)
maxV = calc(maxT)
v = calc(t)

while minT - maxT != 1 and minT - maxT != 0:
    middleT = (minT + maxT) // 2
    if minV < maxV:
        maxT = middleT
        maxV = calc(maxT)
    else:
        minT = middleT
        minV = calc(minT)
    print(minT, maxT, middleT)

print(minV)
