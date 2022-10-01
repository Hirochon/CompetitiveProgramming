N, Q = map(int, input().split())
A = []
for _ in range(N):
    L, *a = map(int, input().split())
    A.append(a)

S = []
T = []
for _ in range(Q):
    s, t = map(int, input().split())
    S.append(s)
    T.append(t)

for s, t in zip(S, T):
    print(A[s-1][t-1])
