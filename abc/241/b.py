from collections import defaultdict
dd = defaultdict(int)
N, M = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

for a in A:
    dd[a] += 1

for b in B:
    dd[b] -= 1
    if dd[b] < 0:
        print('No')
        exit()
print('Yes')
