S = input()
T = input()

if len(S) < len(T):
    print('No')
    exit()

for i in range(len(S)):
    if i > len(S)-len(T):
        break
    flag = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            flag = 1
            break
    if flag == 0:
        print('Yes')
        exit()
print('No')