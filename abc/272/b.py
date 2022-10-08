from itertools import combinations

N, M = map(int, input().split())
K = []
X = []
for i in range(M):
    k, *x = map(int, input().split())
    K.append(k)
    X.append(x)

pair = [[0 if i > j else 1 for i in range(N)] for j in range(N)]

for values in X:
    for i, j in combinations(values, 2):
        # print(i, j)
        pair[i-1][j-1] = 1
        pair[j-1][i-1] = 1

for i in range(N):
    # print(pair[i])
    if sum(pair[i]) != N:
        print('No')
        exit()
print('Yes')