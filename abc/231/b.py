from collections import defaultdict

N = int(input())

dd = defaultdict(int)

for i in range(N):
    s = input()
    dd[s] += 1

l = []

for v, i in dd.items():
    l.append((i, v))

print(sorted(l)[-1][1])
