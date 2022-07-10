import numpy as np

N, M = map(int, input().split())
ans_list = np.zeros(N - 1, dtype=int)
AB = []
flag = 0
ans_num_1 = []
for i in range(M):
    ab = list(map(int, input().split()))
    AB.append(ab)
    if 1 in ab:
        for j in ab:
            if j != 1:
                ans_num_1.append(j)
                ans_list[j - 2] = 1
        AB.remove(ab)
if 0 not in ans_list:
    flag = 1
    print("Yes")
# print(ans_list)
while(flag != 1):
    if flag == 0:
        for ab in AB:
            for ans_num in ans_num_1:
                if ans_num in ab:
                    for j in ab:
                        if ans_num != j:
                            ans_list[j - 2] = ans_num
                    AB.remove(ab)
            
        if 0 not in ans_list:
            flag = 1
            print("Yes")
if flag == 1:
    for ans in ans_list:
        print(ans)
