import heapq

a = []
heapq.heapify(a)

heapq.heappush(a, (1,2,3))
heapq.heappush(a, (3,2,1))
heapq.heappush(a, (2,4,3))
heapq.heappush(a, (2,2,3))

while a:
    print(heapq.heappop(a))

b = [(1,2,3), (3,2,1), (2,4,3), (2,2,3)]

b.sort()
print()
for bi in b:
    print(bi)