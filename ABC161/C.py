N, K = map(int, input().split())
ans = N % K
if ans > (K - ans):
    ans = abs(K - ans)
print(ans)
