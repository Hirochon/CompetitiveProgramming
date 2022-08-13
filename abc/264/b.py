R, C = map(int, input().split())

RC = [["" for _ in range(15)] for _ in range(15)]
# print(RC)
worb = True
for i in range(8):
    worb = not worb
    x = i
    y = i
    for j in range(4):
        for k in range(15-i*2):
            # print(x, y)
            if j == 0:
                RC[x][y] = "white" if worb else "black"
                if y+i < 14:
                    y += 1
            elif j == 1:
                RC[x][y] = "white" if worb else "black"
                if x+i < 14:
                    x += 1
            elif j == 2:
                RC[x][y] = "white" if worb else "black"
                if y+i > 0:
                    y -= 1
            elif j == 3:
                RC[x][y] = "white" if worb else "black"
                if x+i > 0:
                    x -= 1
        for d in range(15):
            print(RC[d])
        print()

print(RC)
print(RC[R-1][C-1])
