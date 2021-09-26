from collections import deque
sys.setrecursionlimit(10**6)

N = int(input())

A = deque(list(map(int, input().split())))

ans = [0] * 10

def dfs(a, n):
    n -= 1
    a_left = a.copy()

    al = a_left.popleft()
    a_left[0] = (a_left[0] + al) % 10
    if n == 1:
        ans[a_left[0]] += 1
        ans[a_left[0]] //= 998244353
    else:
        dfs(a_left, n)

    ar = a.popleft()
    a[0] = (a[0] * ar) % 10
    if n == 1:
        ans[a[0]] += 1
        ans[a[0]] //= 998244353
    else:
        dfs(a, n)

dfs(A, N)

print(*ans, sep="\n")