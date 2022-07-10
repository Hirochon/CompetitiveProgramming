K = int(input())
S = input()
s_len = len(S)
if K >= s_len:
    print(S)
else:
    for i in range(K):
        print(S[i], end="")
    print('...')
