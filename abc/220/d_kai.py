MOD = 998244353

N = int(input())
A = [i for i in map(int, input().split())]

dp = [0]*10
dp[A[0]] = 1

for x in A[1:]:
    dp_c = [0]*10
    for i in range(10):
        dp_c[(x + i) % 10] += dp[i]
        dp_c[(x * i) % 10] += dp[i]
        dp_c[(x + i) % 10] %= MOD
        dp_c[(x * i) % 10] %= MOD
    dp = dp_c
print(*dp, sep="\n")