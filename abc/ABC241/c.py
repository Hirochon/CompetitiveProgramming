# N 行 N 列のマス目があり、それぞれのマスは白または黒で塗られています。
# マス目の状態は N 個の文字列 Si で表され、 Si の j 文字目が # であることはマス目の上から i 行目、左から j 列目のマスが黒く塗られていることを、 . であることは白く塗られていることをさします。
#
# 高橋君はこのマス目のうち高々 2 つの白く塗られているマスを選び、黒く塗ることができます。
# マス目の中に、黒く塗られたマスが縦、横、ななめのいずれかの向きに 6 つ以上連続するようにできるか判定してください。
# ただし、黒く塗られたマスがななめに 6 つ以上連続するとは、N 行 N 列のマス目に完全に含まれる 6 行 6 列のマス目であって、その少なくとも一方の対角線上のマスがすべて黒く塗られているようなものが存在する事をさします。
N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)

for i in range(N):
    sagasu = 0
    init = 0
    for j in range(N):
        if S[i][j] == '#':
            sagasu += 1
        if init != 6:
            init += 1
            continue
        if S[i][j] == '.':
            sagasu -= 1
        if sagasu == 6:
            print('Yes')
            exit()

for i in range(N):
    sagasu = 0
    init = 0
    for j in range(N):
        if S[j][i] == '#':
            sagasu += 1
        if init != 6:
            init += 1
            continue
        if S[j][i] == '.':
            sagasu -= 1
        if sagasu == 6:
            print('Yes')
            exit()


ii = 0
ij = N - 1
## 配列を斜めに探索していく
i = 0
for j in range(N):
    k = 0
    while ii + k + i < N and ij + k - j >= 0:
        x = ij + k - j
        y = ii + k + i
        if S[y][x] == "#":
            sagasu += 1
        if init != 6:
            init += 1
            continue
        if S[y][x] == ".":
            sagasu -= 1
        if sagasu == 6:
            print("Yes")
            exit()
        k += 1
