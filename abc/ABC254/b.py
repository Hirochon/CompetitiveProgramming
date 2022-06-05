N = int(input())
A = [[1]]

for i in range(N):
    if i == N - 1:
        break
    # AA = [A[i].copy()[0]]
    AA = []
    for j in range(len(A[i])+1):
        if j == 0:
            AA.append(A[i][0])
        elif j == len(A[i]):
            AA.append(A[i][-1])
        else:
            AA.append(A[i][j-1] + A[i][j])
    A.append(AA)

for a in A:
    print(*a)
