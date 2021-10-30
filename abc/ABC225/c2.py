N, M = map(int, input().split())

B = [[0]*M for _ in range(N)]

for i in range(N):
    b = list(map(int, input().split()))
    for j in range(M):
        B[i][j] = b[j]

start = B[0][0]
startM = (start-1)//7
startN = (start-1)%7 + 1

for i in range(N):
    for j in range(M):
        # print(B[i][j])
        # print((startM + i) * 7, (j + startN))
        # print((B[i][j-1]-1) // 7, (B[i][j]-1) // 7)
        if j != 0 and (B[i][j-1]-1) // 7 != (B[i][j]-1) // 7:
            print("No")
            exit()
        if B[i][j] != (startM + i) * 7 + (j + startN):
            print("No")
            exit()
print("Yes")