N = int(input())

A = [0]*N
B = [0]*N

for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

A.sort()
B.sort()
aStart = A[N//2]
bEnd = B[N//2]

ans = 0
for i in range(N):
    ans += abs(A[i] - aStart)
    # print(1, ans)
    ans += B[i] - A[i]
    # print(2, ans)
    ans += abs(B[i] - bEnd)
    # print(3, ans)

print(ans)
