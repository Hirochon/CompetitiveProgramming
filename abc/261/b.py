N = int(input())
A = []
for i in range(N):
    a = input()
    A.append(a)

for i in range(N):
    for j in range(N):
        if A[i][j] == 'W' and A[j][i] == 'L':
            continue
        elif A[i][j] == 'L' and A[j][i] == 'W':
            continue
        elif A[i][j] == 'D' and A[j][i] == 'D':
            continue
        elif A[i][j] == '-' and A[j][i] == '-':
            continue
        else:
            print('incorrect')
            exit()
print('correct')