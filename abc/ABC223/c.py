N = int(input())

sumS = 0

A = [0]*N
B = [0]*N

for i in range(N):
    a, b = map(int, input().split())
    sumS += a / b
    A[i] = a
    B[i] = b

sumS /= 2
ans = 0

for i in range(N):
    if sumS > A[i] / B[i]:
        sumS -= A[i] / B[i]
        ans += A[i]
    else:
        ans += sumS * B[i]
        break

print(ans)