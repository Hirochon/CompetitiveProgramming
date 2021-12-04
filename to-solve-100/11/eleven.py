from itertools import product

N, M = map(int, input().split())

K = []
S = []
for i in range(M):
    k, *m = map(int, input().split())
    K.append(k)
    S.append(m)
# print(K, S)

P = list(map(int, input().split()))
# print(P)

ans = 0

for prod in product(range(2), repeat=N):
    isOK = True
    for m in range(M):
        isSwitch = sum([prod[S[m][i]-1] for i in range(K[m])]) % 2
        if isSwitch != P[m]:
            isOK = False
            break
    if isOK:
        ans += 1
print(ans)
