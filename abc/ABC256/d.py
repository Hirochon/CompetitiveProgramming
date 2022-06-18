N = int(input())

X = []
Y = []
max_num = 0
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    max_num = max(max_num, y)

kukan = [[] for _ in range(max_num+1)]

for x, y in zip(X, Y):
    if kukan[x] and kukan[x][0] == "e":
        kukan[x] = []
    else:
        kukan[x].append("s")
    
    if kukan[y] and kukan[y][0] == "s":
        kukan[y] = []
    else:
        kukan[y].append("e")

# print(kukan)
ans = []
start = 0
s_point = 0
for i, k in enumerate(kukan):
    for kk in k:
        # print(kk, i, s_point, start)
        if kk == "s":
            s_point += 1
            if start == 0:
                start = i
        elif kk == "e":
            if s_point == 1:
                ans.append([start, i])
                start = 0
            s_point -= 1

for a in ans:
    print(a[0], a[1])
