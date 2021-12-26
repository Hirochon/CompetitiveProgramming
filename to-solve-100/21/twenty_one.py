N = int(input())

HS = []
T = []

for _ in range(N):
    H, S = map(int, input().split())
    HS.append((H, S))
    T.append(H + S * (N-1))

# print(HS)
# print(T)
T.sort()

minI = 0
maxI = N-1

def isOk(index):
    return True

while minI - maxI != 1:
    middleI = (minI + maxI) // 2
    if isOk(middleI):
        maxI = middleI-1
    else:
        minI = middleI+1
    print(maxI, minI, middleI)

print(middleI, T[middleI])
