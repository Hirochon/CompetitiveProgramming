from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

C = []
for i in range(r):
    row = input()
    C.append(row)

set_past = set()
queue = deque([(0, sy-1, sx-1)])
past = [[-1 for _ in range(c)] for _ in range(r)]
now_d = 0
while queue.__len__():
    d, y, x = queue.popleft()
    past[y][x] = d
    if past[gy-1][gx-1] != -1:
        break
    vectors = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    for vec in vectors:
        if vec[0] < 0 or vec[1] < 0 or vec[0] >= r or vec[1] >= c:
            continue
        if C[vec[0]][vec[1]] == "#":
            continue
        if past[vec[0]][vec[1]] == -1:
            if (d + 1, vec[0], vec[1]) not in set_past:
                queue.append((d + 1, vec[0], vec[1]))
                set_past.add((d+1, vec[0], vec[1]))
print(past[gy-1][gx-1])
