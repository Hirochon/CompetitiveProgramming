N, M = map(int, input().split())

N2 = N*2

A = [""] * N2
ans = [[0, i] for i in range(N2)]

for i in range(N2):
        inA = input()
        A[i] = inA

def janken(p1, p2):
    if p1 == p2:
        return 0, 0
    elif p1 == "G":
        if p2 == "P":
            return 0, 1
        else:
            return 1, 0
    elif p1 == "P":
        if p2 == "C":
            return 0, 1
        else:
            return 1, 0
    elif p1 == "C":
        if p2 == "G":
            return 0, 1
        else:
            return 1, 0

for j in range(M):
    for i in range(N):
        p1 = ans[i*2][1]
        p2 = ans[i*2+1][1]
        # print(p1, p2)
        p1p, p2p = janken(A[p1][j], A[p2][j])
        # print(p1p, p2p)
        ans[i*2][0] -= p1p
        ans[i*2 + 1][0] -= p2p
        # print(ans)
    ans.sort()
    # print(ans)

for p, i in ans:
    print(i+1)
