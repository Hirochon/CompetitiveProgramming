S = input()
T = input()

S_list = [[S[0]]]
T_list = [[T[0]]]

i = 0
for s in S[1:]:
    if s == S_list[i][0]:
        S_list[i].append(s)
    else:
        S_list.append([s])
        i += 1

i = 0
for t in T[1:]:
    if t == T_list[i][0]:
        T_list[i].append(t)
    else:
        T_list.append([t])
        i += 1

if len(S_list) != len(T_list):
    print('No')
    exit()

for s, t in zip(S_list, T_list):
    if s[0] != t[0]:
        print('No')
        exit()
    if len(s) == len(t):
        continue
    if len(s) >= 2 and len(t) >= 2:
        if len(s) <= len(t):
            continue
    print('No')
    exit()
print('Yes')
