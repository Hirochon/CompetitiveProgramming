from collections import deque

H, W, N = map(int, input().split())
HW = []
S = []
for i in range(H):
    hw = input()
    hw.find("S")
    HW.append(hw)
    if hw.find("S") != -1:
        S.append(i)
        S.append(hw.find("S"))

# print(S)
# print(HW[S[0]][S[1]])

past = set()
# (x, y, 時間, 体力)
queue = deque([(S[1], S[0], 0, 1)])
goals = set()

while queue.__len__():
    x, y, t, hp = queue.popleft()
    past.add((x, y, hp))
    next_xy = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for nx, ny in next_xy:
        if 0 <= nx < W and 0 <= ny < H:
            if HW[ny][nx] == "." and (nx, ny, hp) not in past:
                queue.append((nx, ny, t + 1, hp))
                continue
            elif HW[ny][nx] == "S" and (nx, ny, hp) not in past:
                queue.append((nx, ny, t + 1, hp))
                continue
            elif HW[ny][nx] == "X":
                continue
            elif "0" <= HW[ny][nx] <= "9" and (nx, ny, hp) not in past:
                if HW[ny][nx] <= str(hp) and (nx, ny) not in goals:
                    queue.append((nx, ny, t + 1, hp + 1))
                    goals.add((nx, ny))
                    if goals.__len__() == N:
                        print(t + 1)
                        exit()
                else:
                    queue.append((nx, ny, t + 1, hp))
        