import numpy as np

N, Q = map(int, input().split())

A = list(map(int, input().split()))

K = [int(input()) for _ in range(Q)]


flag = True
i = 1
j = 0

ans = []

while flag:
    if i in A:
        i += 1
    else:
        j += 1
        if j in K:
            ans.append(i)
        i += 1
        if len(ans) == len(K):
            flag = False
            break

k_index = np.argsort(K)

for k in k_index:
    print(ans[k])
