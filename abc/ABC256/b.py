from collections import deque

N = int(input())
A = map(int, input().split())

P = 0
queue = deque([0])

for a in A:
    queue[0] = 1
    for _ in range(a):
        queue.appendleft(0)
        if queue.__len__() == 5:
            v = queue.pop()
            # print(v)
            P += v

print(P)
