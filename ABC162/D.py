from collections import deque


N = int(input())
S = input()
S_que = deque(S)
num = len(S_que)
ans = 0
if N >= 3:
    for i in range(num - 2):
        S_list = []
        kore = S_que.popleft()
        S_list.append(kore)
        chon = 0
        que_test_G = S_que.copy()
        num_G = len(que_test_G)
        for j in range(num_G - 1):
            chon += 1
            kore2 = que_test_G.popleft()
            if kore2 not in S_list:
                S_list.append(kore2)
                que_test_B = que_test_G.copy()
                num_B = len(que_test_B)
                for k in range(num_B):
                    chon += 1
                    kore3 = que_test_B.popleft()
                    if kore3 not in S_list:
                        if chon > 2:
                            # print(S_list)
                            # print(i, j, k)
                            ans += 1
            S_list.remove(kore2)
print(ans)
