import math

N = int(input())

A = list(map(int, input().split()))

flag = True

ans = 0
diff = []

while flag:
    for i in range(math.ceil(N / 2)):
        if A[i] != A[-(i + 1)]:
            diff.append(i)
        else:
            diff.remove(i)
    flag = False
