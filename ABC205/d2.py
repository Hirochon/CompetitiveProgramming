N, Q = map(int, input().split())

A = list(map(int, input().split()))

K = [int(input()) for _ in range(Q)]

ans_set = set([i + 1 for i in range(10**5)])

anset = ans_set - set(A)

ans = list(anset)

for i in K:
    print(ans[i - 1])
