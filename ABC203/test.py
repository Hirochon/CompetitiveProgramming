from collections import defaultdict

N, K = map(int, input().split())

dd = defaultdict(int)

for i in range(N):
    a, b = map(int, input().split())
    dd[a] += b

for i, v in sorted(dd.items()):
    if i <= K:
        K += v

    else:
        break

print(K)
