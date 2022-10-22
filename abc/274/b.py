H, W = map(int, input().split())
C = [0 for _ in range(W)]
for i in range(H):
    c = input()
    for i, cc in enumerate(c):
        if cc == '#':
            C[i] += 1
print(*C)