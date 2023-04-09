H, W = map(int, input().split())
S = []
for i in range(H):
    s = input()
    ss = []
    for sss in s:
        ss.append(sss)
    S.append(ss)

for i in range(H):
    for j in range(W-1):
        if S[i][j] == "T" and S[i][j+1] == "T":
            S[i][j] = "P"
            S[i][j+1] = "C"
for i in range(H):
    print("".join(S[i]))
