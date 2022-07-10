import heapq

N = int(input())
S = [s for s in map(int, input().split())]
T = [t for t in map(int, input().split())]

ansList = []
heapq.heapify(ansList)

for i, t in enumerate(T):
    heapq.heappush(ansList, (t, i))

ans = [0 for _ in range(N)]
index = 0

while index < N:
    t, i = heapq.heappop(ansList)
    if ans[i] > 0:
        continue
    ans[i] = t
    index += 1
    heapq.heappush(ansList, (S[i]+t, (i+1)%N))

print(*ans, sep="\n")
