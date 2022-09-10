from itertools import permutations, product

N, M = map(int, input().split())
S = []
T = set()
for i in range(N):
    s = input()
    S.append(s)
for i in range(M):
    t = input()
    T.add(t)

kari_ans = set()

add_sco_list = []
for v in product(range(1, N), repeat=N):
    asl = ["_"*al for al in v]
    add_sco_list.append(asl)

## 全通りのパターンを用意する
for v in permutations(range(N), N):
    new_s_list = [S[v[i]] for i in range(N)]
    for add_sco in add_sco_list:
        new_s = ""
        for i in range(N-1):
            new_s += new_s_list[i] + add_sco[i]
        new_s += new_s_list[-1]
        if 3 > len(new_s):
            continue
        if len(new_s) > 16:
            break
        kari_ans.add(new_s)

# print(kari_ans - T)

ans_list = list(kari_ans - T)
if len(ans_list) == 0:
    print(-1)
else:
    print(ans_list[0])
