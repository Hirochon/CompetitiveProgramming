from collections import deque

N, M = map(int, input().split())

A_k = [0]*M
A = [[] for _ in range(M)]
f = [0]*M

for i in range(M):
    k = int(input())
    A_k[i] = k
    A[i] = deque([a for a in map(int, input().split())][::-1])
    f[i] = A[i][-1]

a = deque()

while True:
    A[1].pop
