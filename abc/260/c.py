N, X, Y = map(int, input().split())

def exe1(rn):
    return rn, X*rn

def exe2(bn):
    return bn, Y*bn

def exe3(hrn, hbn):
    rn11, bn = exe1(hrn)
    rn12, bn1 = exe2(bn + hbn)
    # print(rn11 + rn12, bn1)
    return rn11 + rn12, bn1

rn = 1
bn = 0
for _ in range(N-1):
    rn, bn = exe3(rn, bn)

print(bn)
