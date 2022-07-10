from itertools import permutations

N = int(input())
A = [[0 for _ in range(2*N)] for _ in range(2*N)]
pastSet = set()
for i in range(N*2-1):
    AIA = map(int, input().split())
    for j, AIa in enumerate(AIA):
        A[i][i+j+1] = AIa
# print(A)
# i = 0
ans = 0
for v in permutations(range(N*2), N*2):
    flag1 = False
    for i in range(N):
        if v[i*2] > v[i*2+1]:
            flag1 = True
            break
    if flag1:
        continue

    ansSub = 0
    flag = True
    for i in range(N):
        v1 = v[i*2]
        v2 = v[i*2+1]
        # print("v1, v2", v1, v2)
        # if v1 < v2:
        if i == 0:
            ansSub = A[v1][v2]
        else:
            ansSub ^= A[v1][v2]
        # else:
        #     flag = False
        #     break
    # if flag:
    ans = max(ans, ansSub)
    # i+=1
    # if i==20:
    #     exit()
print(ans)
