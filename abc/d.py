import math
N = int(input())
A = list(map(int, input().split()))
sortedA = sorted(A)
cnt = [0 for _ in range(2*10**5+1)]
for i in range(N):
    cnt[A[i]] += 1
ans = 0
for i in range(1, math.ceil(2*10**5+1)):
    for j in range(i, (2*10**5) // i + 1):
        if i == j == i * j:
            ans += cnt[i] ** 3
        elif i == j:
            ans += cnt[i] * cnt[j] * cnt[i * j]
        elif j == i * j:
            ans += cnt[i] * cnt[j] * cnt[j] * 2
        else:
            ans += cnt[i] * cnt[j] * cnt[i * j] * 2
print(ans)