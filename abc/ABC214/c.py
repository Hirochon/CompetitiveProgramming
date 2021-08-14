N = int(input())

S = [s for s in map(int, input().split())]
T = [t for t in map(int, input().split())]

for i in range(N*2):
    T[(i+1) % N] = min(T[(i+1) % N], S[i % N] + T[i % N])

for t in T:
    print(t)