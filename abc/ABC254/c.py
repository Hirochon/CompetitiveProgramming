import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
sorted_A = sorted(A)
ans = [1 for _ in range(N)]

for i, a in enumerate(A):
    # print("a", a)
    target = bisect.bisect_left(sorted_A, a)
    flag = True
    while True:
        if (target - i) % K == 0 and ans[target] == 1:
            ans[target] = 0
            break
        elif len(sorted_A)-1 > target and sorted_A[target] == sorted_A[target+1]:
            target += 1
        else:
            flag = False
            break
    if not flag:
        print("No")
        exit()
print("Yes")
