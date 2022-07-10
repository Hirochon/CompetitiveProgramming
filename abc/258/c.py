N, Q = map(int, input().split())
s = input()
S = []
for ss in s:
    S.append(ss)
queue = []
for i in range(Q):
    t, x = map(int, input().split())
    queue.append((t, x))

rotate = 0
for t, x in queue:
    if t == 1:
        rotate -= x
        rotate %= N
    else:
        print(S[(x + rotate - 1) % N])
