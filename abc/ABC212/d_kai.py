import heapq

Q = int(input())

diff = 0
hp = []
heapq.heapify(hp)

for i in range(Q):
    query = [v for v in map(int, input().split())]

    if query[0] == 1:
        heapq.heappush(hp, query[1] - diff)
    elif query[0] == 2:
        diff += query[1]
    else:
        print(heapq.heappop(hp) + diff)
