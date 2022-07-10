from itertools import combinations

N = int(input())

X, Y = map(int, input().split())

tupleList = [(2, 3)]*N
indexList = [i for i in range(N)]

maxA = 0
maxB = 0

for i in range(N):
    A, B = map(int, input().split())
    maxA += A
    maxB += B
    tupleList[i] = (A, B)

if maxA < X or maxB < Y:
    print(-1)
    exit()

for i in range(1, N+1):
    for aList in combinations(indexList, i):
        sumA = 0
        sumB = 0
        for a in aList:
            sumA += tupleList[a][0]
            sumB += tupleList[a][1]
        if sumA >= X and sumB >= Y:
            print(i)
            exit()
print(-1)