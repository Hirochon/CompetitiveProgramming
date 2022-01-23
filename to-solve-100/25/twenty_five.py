from collections import deque

ans = deque([])

w = 1
h = 1
while w != 0 or h != 0:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    c = []
    c_score = [[-1 for _ in range(w)] for _ in range(h)]
    # print()
    # print("c_score", c_score)
    # print()
    score = 1
    keiro = deque([])
    for i in range(h):
        ci = list(map(int, input().split()))
        c.append(ci)
        for j in range(w):
            keiro.append((j, i))

    while len(keiro) > 0:
        (x, y) = keiro.popleft()
        # print()
        # print("x, y", x, y)
        # print()
        # print(x, y, c_score[x][y])
        if c_score[y][x] != -1:
            continue

        if c[y][x] == 0:
            score += 1
            c_score[y][x] = 0
            continue
        # print(c)
        c_score[y][x] = score
        # print()
        # print("c", c)
        # print()
        if x+1 < w:
            if c[y][x+1] == 1:
                keiro.appendleft((x+1, y))
        if y+1 < h:
            if c[y+1][x] == 1:
                keiro.appendleft((x, y+1))
        if x+1 < w and y+1 < h:
            if c[y+1][x+1] == 1:
                keiro.appendleft((x+1, y+1))
        if x+1 < w and y-1 >= 0:
            if c[y-1][x+1] == 1:
                keiro.appendleft((x+1, y-1))
        if y-1 >= 0:
            if c[y-1][x] == 1:
                keiro.appendleft((x, y-1))
        if x-1 >= 0 and y-1 >= 0:
            if c[y-1][x-1] == 1:
                keiro.appendleft((x-1, y-1))
        if x-1 >= 0:
            if c[y][x-1] == 1:
                keiro.appendleft((x-1, y))
        if x-1 >= 0 and y+1 < h:
            if c[y+1][x-1] == 1:
                keiro.appendleft((x-1, y+1))
    anSet = set()
    for css in c_score:
        for cs in css:
            anSet.add(cs)
    # print()
    # print(anSet)
    # print()
    ans.append(len(anSet)-1)

for a in ans:
    print(a)
