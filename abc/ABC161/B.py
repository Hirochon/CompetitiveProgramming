N, M = map(int, input().split())
A = list(map(int, input().split()))
total = 0
flag = 0
ans = []
for a in A:
    total += a
to = total / (4 * M)
sort_A = sorted(A)
length = len(sort_A)
for i in range(M):
    ans.append(sort_A[length - i - 1])
for ans_sub in ans:
    if ans_sub < to:
        flag += 1
        break
if flag == 0:
    print("Yes")
else:
    print("No")
