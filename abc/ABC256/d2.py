from ctypes import HRESULT
import heapq

N = int(input())
L = []
R = []
heapq.heapify(L)
heapq.heapify(R)
for i in range(N):
    l, r = map(int, input().split())
    heapq.heappush(L, l)
    heapq.heappush(R, r)

while L.__len__():
    
