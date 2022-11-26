from collections import defaultdict
import numpy as np

H, W = map(int, input().split())
S = []
T = []
for i in range(H):
    s = list(input())
    S.append(s)
for i in range(H):
    t = list(input())
    T.append(t)

num_S = np.array(S)
num_T = np.array(T)

ans_dict = defaultdict(int)
for i in range(W):
    new_s = "".join(num_S[:, i])
    ans_dict[new_s] += 1

print(ans_dict)

for i in range(W):
    new_t = "".join(num_T[:, i])
    ans_dict[new_t] -= 1

print(ans_dict)

for k, v in ans_dict.items():
    if v != 0:
        print('No')
        exit()
print('Yes')
