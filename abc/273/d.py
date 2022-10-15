from collections import defaultdict
H, W, rs, cs = map(int, input().split())
N = int(input())
Y = defaultdict(list)
X = defaultdict(list)
for i in range(N):
    r, c = map(int, input().split())
    Y[r].append(c)
    Y[r].sort()
    X[c].append(r)
    X[c].sort()

Q = int(input())
D = []
L = []
for i in range(Q):
    d, l = map(int, input().split())
    D.append(d)
    L.append(l)

for i in range(Q):
    d, l = D[i], L[i]
    if d == "L":
        drs = rs
        dcs = cs - l
        if dcs < 1:
            cs = 0
            print(rs, cs)
            continue
    elif d == "R":
        drs = rs
        dcs = cs + l
        if dcs > W:
            cs = W
            print(rs, cs)
            continue
    elif d == "U":
        drs = rs - l
        dcs = cs
        if drs < 1:
            rs = 0
            print(rs, cs)
            continue
    elif d == "D":
        drs = rs + l
        dcs = cs
        if drs > H:
            rs = H
            print(rs, cs)
            continue
