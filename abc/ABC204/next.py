import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

hako = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    hako[A].append(B)


def dfs(next_i):
    if michi[next_i]:
        return
    michi[next_i] = True
    for ii in hako[next_i]:
        dfs(ii)


ans = 0

for i in range(1, N + 1):
    michi = [False for _ in range(N + 1)]
    dfs(i)
    ans += sum(michi)

print(ans)
