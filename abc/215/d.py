import math
import heapq

N, M = map(int, input().split())

A = 1
min = 10e6
for i in map(int, input().split()):
    A *= i
    if i != 1 and min > i and i < 10e2:
        min = i

ans = []
heapq.heapify(ans)
for i in range(1, M+1):
    if i % min == 0:
        continue
    if math.gcd(A, i) == 1:
        heapq.heappush(ans, i)

length = len(ans)
print(length)
for _ in range(length):
    print(heapq.heappop(ans))