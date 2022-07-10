import heapq

N, K = map(int, input().split())

P = list(map(int, input().split()))

P1 = P[:K-1]
minP1 = 0
heapq.heapify(P1)
for i in range(K-1, N):
    if minP1 < P[i]:
        heapq.heappush(P1, P[i])
        minP1 = heapq.heappop(P1)
    # print(P[i], P1, minP1)
    print(minP1)
