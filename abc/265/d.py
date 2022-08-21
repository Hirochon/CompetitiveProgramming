from collections import deque
N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
deque_A = deque(A)
p_list = deque([deque_A.popleft()])
p = p_list[0]
q_list = deque([deque_A.popleft()])
q = q_list[0]
r_list = deque([deque_A.popleft()])
r = r_list[0]
# print(p, q, r)
while deque_A.__len__() > 0:
    if p == P and q == Q and r == R:
        # print(p_list)
        # print(q_list)
        # print(r_list)
        print("Yes")
        exit()
    if p != P:
        poped_q = q_list.popleft()
        q -= poped_q
        p_list.append(poped_q)
        p += poped_q
        if p > P:
            while p > P:
                poped_p = p_list.popleft()
                p -= poped_p
    if q != Q:
        poped_r = r_list.popleft()
        r -= poped_r
        q_list.append(poped_r)
        q += poped_r
        if q > Q:
            if p == P:
                poped_p = p_list.popleft()
                p -= poped_p
    if r != R:
        poped_a = deque_A.popleft()
        r_list.append(poped_a)
        r += poped_a
        if r > R:
            if p == P and q == Q:
                poped_p = p_list.popleft()
                p -= poped_p
#     print(p, q, r)
# print(p_list)
# print(q_list)
# print(r_list)
print("No")
