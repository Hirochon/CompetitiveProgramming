from collections import deque
N, M = map(int, input().split())

NN = [[-1 for _ in range(N)] for _ in range(N)]
NN[0][0] = 0
# if (N - 1)**2*2 < M:
#     for i in range(N):
#         print(*NN[i])
queue = deque([(0, 0, 1)])

bectors = []
for i in range(N):
    for j in range(N):
        if (i**2 + j**2) == M:
            bectors.append((i, j))
            bectors.append((-i, -j))
            bectors.append((i, -j))
            bectors.append((-i, j))

while queue:
    (qx, qy, n) = queue.popleft()
    for i, j in bectors:
        x = qx + i
        y = qy + j
        if 0 <= x < N and 0 <= y < N and NN[x][y] == -1:
            NN[x][y] = n
            queue.append((x, y, n+1))

for i in range(N):
    print(*NN[i])
