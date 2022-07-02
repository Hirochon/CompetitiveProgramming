N = int(input())
A = []
for i in range(N):
    a = input()
    num_a = []
    for aa in a:
        num_a.append(int(aa))
    A.append(num_a)
ans = 0
way = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(N):
    for j in range(N):
        for k in range(8):
            now = 0
            x, y = i, j
            for l in range(N):
                now += A[x][y]
                now *= 10
                x += way[k][0]
                y += way[k][1]
                x %= N
                y %= N
            ans = max(ans, now)
print(ans//10)
