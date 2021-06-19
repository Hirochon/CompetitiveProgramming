from collections import defaultdict

dd = defaultdict(int)

N = int(input())

A = list(map(int, input().split()))

sou = len(A)

for i in range(N):
    dd[A[i]] += 1

ans = 0

for key, value in dd.items():
    sou -= value
    ans += sou * value

print(ans)
