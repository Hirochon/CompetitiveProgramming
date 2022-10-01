from collections import deque
N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
deque_A = deque(sorted_A)
real_A = deque([])
plus_list = deque([])
ans = 0
# print(deque_A)
plus_count = 0
i = 1
while len(deque_A) > 0:
    left_value = deque_A.popleft()
    if i == left_value:
        real_A.append(i)
        i += 1
    elif left_value < i:
        plus_list.append(left_value)
        flag = True
        while flag:
            if deque_A.__len__() == 0:
                flag = False
                break
            left_value_2 = deque_A.popleft()
            if left_value_2 == left_value:
                plus_list.append(left_value_2)
            else:
                deque_A.appendleft(left_value_2)
                flag = False
        # print(plus_list)
    else:
        deque_A.appendleft(left_value)
        if len(plus_list) >= 2:
            real_A.append(i)
            i += 1
            plus_list.popleft()
            plus_list.popleft()
            continue

        plus_list.append(deque_A.pop())
        if len(plus_list) >= 2:
            real_A.append(i)
            i += 1
            plus_list.popleft()
            plus_list.popleft()
            continue

        if deque_A.__len__() == 0:
            break
        plus_list.append(deque_A.pop())
        real_A.append(i)
        i += 1
        plus_list.popleft()
        plus_list.popleft()

plus_count = len(plus_list) // 2
# print(real_A, plus_list)
# print(len(real_A) + plus_count)
for a in real_A:
    print(a)
