from collections import Counter

N, M = map(int, input().split())

A = {i:1 for i in map(int, input().split())}
B = {i:2 for i in map(int, input().split())}
C = sorted(dict(Counter(A) + Counter(B)).items(), key=lambda x:x[0])

ans = 2e10
flag = 0
mae = 4e10

for i, v in C:
    if v == 3:
        print(0)
        exit()

    if v != flag:
        flag = v
        if abs(mae - i) < ans:
            ans = abs(mae - i)
    mae = i

print(ans)