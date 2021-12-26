import bisect

N = int(input())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for b in B:
    numA = bisect.bisect_left(A, b)
    numC = N - bisect.bisect_right(C, b)
    ans += numA * numC

print(ans)
