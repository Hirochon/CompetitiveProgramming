from collections import deque

Q = int(input())
dq = deque([])

ini = 0

for i in range(Q):
    query = [v for v in map(int, input().split())]
    if len(query) != 1:
        cal = query[0]
        value = query[1]
        if cal == 1:
            dq.append(value - ini)
            dql = list(dq)
            dq = deque(sorted(dql))
        elif cal == 2:
            ini += value
    else:
        minValue = dq.popleft()
        print(minValue + ini)