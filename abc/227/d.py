import heapq

N, K = map(int, input().split())

A = list(map(lambda x: int(x) * -1, input().split()))

heapq.heapify(A)
ans = 0
keep = [0]*K

while len(A) >= K:
    for i in range(K):
        keep[i] = heapq.heappop(A) * -1
    minV = min(keep)
    ans += minV
    for i in range(K):
        rV = keep[i] - minV
        if rV > 0:
            heapq.heappush(A, -1 * rV)
print(ans)