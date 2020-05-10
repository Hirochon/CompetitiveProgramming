import numpy as np
from itertools import product
min_num = 2000000
N, M, X = map(int, input().split())
V_list = []
A_list = np.zeros(M)
AC_list = []
swich_list = [0 for x in range(N)]
for i in range(N):
    CA = list(map(int, input().split()))
    C = CA[0]
    A = CA[1:]
    A_list += A
    AC_list.append(A)
    V_list.append(CA)
if (A_list >= X).all():
    V_list.sort()
    for pro in product('01', repeat=N):
        pro = list(pro)
        value = 0
        ans_list = np.zeros(M)
        for i, p in enumerate(pro):
            if int(p):
                ans_list += AC_list[i]
                value += V_list[i][0]
        if (ans_list >= X).all():
            if min_num > value and value != 0:
                min_num = value
    print(min_num)

else:
    print('-1')
