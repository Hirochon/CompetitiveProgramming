from collections import defaultdict

H, W = map(int, input().split())
S = []
T = []
for i in range(H):
    S.append(input())
for i in range(H):
    T.append(input())

print()
print(S[0])
print()

ans_dict = defaultdict(int)
for i in range(W):
    ## Sを行ごとに表示する
    new_s = ""
    for j in range(H):
        new_s += S[j][i]
    ans_dict[new_s] += 1

# print(ans_dict)

for i in range(W):
    new_t = ""
    for j in range(H):
        new_t += T[j][i]
    ans_dict[new_t] -= 1

# print(ans_dict)

for k, v in ans_dict.items():
    if v != 0:
        print('No')
        exit()
print('Yes')
