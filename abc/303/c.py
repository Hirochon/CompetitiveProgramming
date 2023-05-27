N, M, H, K = map(int, input().split())
S = input()
oasis = set()
for i in range(M):
    x, y = map(int, input().split())
    oasis.add((x, y))
x = 0
y = 0
for s in S:
    if s == "R":
        x += 1
    elif s == "L":
        x -= 1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1
    H -= 1
    if H < 0:
        print("No")
        exit()
    if (x, y) in oasis:
        if H < K:
            H = K
            oasis.remove((x, y))
print("Yes")
