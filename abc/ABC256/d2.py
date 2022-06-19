N = int(input())
MAX_NUM = 200100
LR = [0 for _ in range(MAX_NUM)]

for i in range(N):
    l, r = map(int, input().split())
    LR[l] += 1
    LR[r] -= 1

# print(LR[:100])

ans = []
start = 0
s_point = 0
for i, lr in enumerate(LR):
    if lr > 0:
        s_point += lr
        if start == 0:
            start = i
    elif lr < 0:
        s_point += lr
        if s_point == 0:
            ans.append([start, i])
            start = 0

for a in ans:
    print(a[0], a[1])
