N = int(input())
A = list(map(int, input().split()))

same = 0
same2 = 0
for i in range(N):
    if i+1 == A[i]:
        same += 1
    elif i+1 < A[i] and A[A[i]-1] == i+1:
        same2 += 1
# print(same, same2)
ans = same2 + same * (same - 1) // 2

print(ans)
