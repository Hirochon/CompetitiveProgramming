from sys import flags


H, W = map(int, input().split())
G = []
for i in range(H):
    g = input()
    G.append(g)
current = [0, 0]
flag = True
past = set((1, 1))
while flag:
    xy = G[current[0]][current[1]]
    if xy == "U" and current[0] != 0:
        current[0] -= 1
        if (current[0], current[1]) in past:
            flag = False
            break
        past.add((current[0], current[1]))
    elif xy == "D" and current[0] != H-1:
        current[0] += 1
        if (current[0], current[1]) in past:
            flag = False
            break
        past.add((current[0], current[1]))
    elif xy == "L" and current[1] != 0:
        current[1] -= 1
        if (current[0], current[1]) in past:
            flag = False
            break
        past.add((current[0], current[1]))
    elif xy == "R" and current[1] != W-1:
        current[1] += 1
        if (current[0], current[1]) in past:
            flag = False
            break
        past.add((current[0], current[1]))
    else:
        print(current[0]+1, current[1]+1)
        exit()
print(-1)
