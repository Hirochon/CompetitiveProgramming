N = int(input())
S = input()

for i in range(1, N):
    flag = True
    for j in range(N):
        if i+j >= N:
            break
        if S[j] == S[i+j]:
            print(j)
            flag = False
            break
    if flag:
        print(N-i)
