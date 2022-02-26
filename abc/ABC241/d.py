import heapq
from bisect import bisect_left, bisect_right
Q = int(input())
A = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(A, query[1])
        print(A)
    elif query[0] == 2:
        index = bisect_right(A, query[1])
        limitedA = A[:index]
        if len(limitedA) >= query[2]:
            print(limitedA[-query[2]])
        else:
            print(-1)
    elif query[0] == 3:
        index = bisect_left(A, query[1])
        limitedA = A[index:]
        if len(limitedA) >= query[2]:
            print(limitedA[query[2] - 1])
        else:
            print(-1)
while len(A) > 0:
    print(heapq.heappop(A))