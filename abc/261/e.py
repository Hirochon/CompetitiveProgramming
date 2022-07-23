N, C = map(int, input().split())
T = []
A = []
for i in range(N):
    t, a = map(int, input().split())
    T.append(t)
    A.append(a)

X = C
past = 0
for i in range(N):
    if T[i] == 1:
        X &= A[i]
        print(X)
        past &= A[i]
    elif T[i] == 2:
        X |= A[i]
        print(X)
        past |= A[i]
    elif T[i] == 3:
        X ^= A[i]
        print(X)
        past ^= A[i]
    X |= past
