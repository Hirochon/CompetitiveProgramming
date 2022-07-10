N = int(input())
A = list(map(int, input().split()))
X = int(input())

s = sum(A)
ans = X // s * N
X -= X // s * s
i = 0

while X >= 0:
    X -= A[i]
    i += 1
print(ans + i)
