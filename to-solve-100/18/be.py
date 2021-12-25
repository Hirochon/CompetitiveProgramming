import bisect

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = map(int, input().split())

ans = 0
for t in T:
    idx = bisect.bisect_left(S, t)
    if idx == n:
        continue
    if S[idx] == t:
        ans += 1
print(ans)
