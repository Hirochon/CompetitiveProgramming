from collections import defaultdict
dd = defaultdict(list)
N, Q = map(int, input().split())

for i, a in enumerate(map(int, input().split())):
    dd[a].append(i+1)

XK = []
for i in range(Q):
    x, k = map(int, input().split())
    XK.append((x,k))

for x, k in XK:
    if len(dd[x]) == 0 or len(dd[x]) < k:
        print(-1)
        continue
    print(dd[x][k-1])
