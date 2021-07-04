import numpy as np

N, K = map(int, input().split())

sei = K // N
amari = K % N

ans = np.zeros(N, dtype="int") + sei

a_list = np.array(list(map(int, input().split())))
a_sorted = sorted(a_list)
a_index = np.argsort(a_list)

for i in range(amari):
    ans[a_index[i]] += 1


for i in range(N):
    print(ans[i])
