from bisect import bisect

N, Q = map(int, input().split())

A = list(map(int, input().split()))

sortedA = sorted(A)
min = min(sortedA)
max = max(sortedA)

X = []

for i in range(Q):
    x = int(input())
    X.append(x)

for x in X:
    if min > x:
        print(N)
    elif max < x:
        print(0)
    else:
        v = bisect(sortedA, x)
        if sortedA[v-1] == x:
            print(N - v + 1)
        else:
            print(N - v)
