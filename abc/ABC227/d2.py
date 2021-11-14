N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

minA = 0
maxA = sum(A)+1

while (maxA - minA) > 1:
    mid = (maxA + minA) // 2
    sumA = [min(v, mid) for v in A]
    # print(sumA, mid)
    if sum(sumA) < mid * K:
        maxA = mid
    else:
        minA = mid

print(minA)
