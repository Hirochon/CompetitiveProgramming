H, W = map(int, input().split())

C = []

for i in range(H):
    c = input()
    C.append(c)

Cp = [[0 for _ in range(W)] for _ in range(H)]

Cp[0][0] = 1

for i in range(H):
    for j in range(W):
        if Cp[i][j] == 0:
            continue
        if (j+1) < W and C[i][j+1] != "#":
            Cp[i][j+1] = Cp[i][j]+1
        if (i+1) < H and C[i+1][j] != "#":
            Cp[i+1][j] = Cp[i][j]+1

ans = 0

for i in range(H):
    for j in range(W):
        ans = max(Cp[i][j], ans)

print(ans)
