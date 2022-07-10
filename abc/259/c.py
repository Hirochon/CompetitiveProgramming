S = input()
T = input()

if S[0] != T[0] or S[1] != T[1]:
    print('No')
    exit()

if len(S) == 2 and len(T) == 2:
    print('Yes')
    exit()

for i in range(1, len(T)):
    # print(S)
    # print(T)
    if len(T) == i+1:
        if len(S) == len(T):
            print('Yes')
            exit()
    if len(S) > i+1:
        if T[i+1] == S[i+1]:
            continue
    if T[i+1] == S[i] and S[i] == S[i-1]:
        S = S[:i] + T[i] + S[i:]
        continue
    print('No')
    exit()