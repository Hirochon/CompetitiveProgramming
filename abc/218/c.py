import numpy as np

N = int(input())

S = np.array([[""]*N]*N)
T = np.array([[""]*N]*N)


for i in range(N):
    s = input()
    for j in range(N):
        S[i][j] = s[j]

for i in range(N):
    t = input()
    for j in range(N):
        T[i][j] = t[j]


def check(G):
    G_row = len(G)
    G_column = len(G[0])

    max_i = -1
    flag = True

    for i in range(G_row):
        for j in range(G_column):
            if G[i, j] == "#" and flag:
                flag = False
                break
        if flag:
            max_i = i
        else:
            break
    if max_i != -1:
        G = G[max_i+1:]

    return np.rot90(G)

S_kai = check(check(check(check(S))))
T_kai = check(check(check(check(T))))

def len_check(S_kai, T_kai):
    s_row = len(S_kai)
    s_column = len(S_kai[0])

    t_row = len(T_kai)
    t_column = len(T_kai[0])

    if s_row == t_row and s_column == t_column:
        return True
    
    return False


for i in range(4):
    if len_check(S_kai, T_kai):
        flag_ans = True
        for i in range(len(S_kai)):
            for j in range(len(S_kai[0])):
                if S_kai[i][j] != T_kai[i][j]:
                    flag_ans = False
                    break
            if not flag_ans:
                break
        if flag_ans:
            print('Yes')
            exit()
        else:
            S_kai = np.rot90(S_kai)
    else:
        S_kai = np.rot90(S_kai)

print("No")
