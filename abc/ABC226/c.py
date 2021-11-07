import sys
sys.setrecursionlimit(10**6)

N = int(input())

W = [[0]]* (N+1)
T = [-1] * (N+1)
past = set()

for i in range(N):
    waza = list(map(int, input().split()))
    W[i+1] = waza
    if waza[1] == 0:
        T[i+1] = waza[0]

def tansaku(I):
    time = 0
    if W[I][1] != 0:
        waza = W[I][2:]
        for i in range(W[I][1]):
            if T[waza[i]] == -1:
                time += tansaku(waza[i])
                past.add(waza[i])
            else:
                if waza[i] not in past:
                    time += T[waza[i]]
                    past.add(waza[i])
    else:
        time += W[I][0]
    return time


fin = W[-1]
value = fin[2:]
ans = W[-1][0]

for i in range(fin[1]):
    if value[i] not in past:
        if T[value[i]] != -1:
            ans += tansaku(value[i])
            past.add(value[i])
        else:
            ans += T[value[i]]
            past.add(value[i])

print(ans)
