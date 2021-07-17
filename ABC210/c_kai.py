from collections import defaultdict

N, K = map(int, input().split())

c = [v for v in map(int, input().split())]

dd = defaultdict(int)

ans = 0

for i in range(N):
    dd[c[i]] += 1
    if i > K-1:
        dd[c[i-K]] -= 1
        if dd[c[i-K]] == 0:
            del dd[c[i-K]]
    ans = max(ans, len(dd))

print(ans)