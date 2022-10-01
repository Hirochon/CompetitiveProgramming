from collections import deque
N = int(input())
A = list(map(int, input().split()))
set_A = set(A)
count = N - len(set_A)
sorted_A = sorted(set_A)
deque_A = deque(sorted_A)
ans = 0

while deque_A.__len__() > 0:
    if deque_A[0] == ans + 1:
        ans += 1
        deque_A.popleft()
    else:
        if count >= 2:
            ans += 1
            count -= 2
        elif count == 1:
            deque_A.pop()
            count -= 1
            ans += 1
        else:
            if deque_A:
                deque_A.pop()
            if deque_A:
                deque_A.pop()
                ans += 1
ans += count // 2
print(ans)
