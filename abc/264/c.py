from itertools import product

H1, W1 = map(int, input().split())
A = []
for i in range(H1):
    a = list(map(int, input().split()))
    A.append(a)
H2, W2 = map(int, input().split())
B = []
for i in range(H2):
    b = list(map(int, input().split()))
    B.append(b)

for bitH in product(range(2), repeat=H1):
    if bitH.count(1) != H2:
        continue
    searchH = [i for i, j in enumerate(bitH) if j == 1]
    for bitW in product(range(2), repeat=W1):
        if bitW.count(1) != W2:
            continue
        searchW = [i for i, j in enumerate(bitW) if j == 1]
        flag = False
        for i in range(H2):
            for j in range(W2):
                if A[searchH[i]][searchW[j]] != B[i][j]:
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print('Yes')
            exit()
print('No')
