from collections import deque

N = int(input())
W = [[0]] * (N+1)

for i in range(N):
    waza = list(map(int, input().split()))
    W[i+1] = waza

q = deque(W[-1][2:])
time = W[-1][0]
past = [-1] * (N+1)

while q:
    v = q.popleft()
    if past[v] == -1:
        time += W[v][0]
        past[v] = 1
    if W[v][1] != 0:
        wazaList = W[v][2:]
        for waza in wazaList:
            if past[waza] == -1:
                q.append(waza)
print(time)
