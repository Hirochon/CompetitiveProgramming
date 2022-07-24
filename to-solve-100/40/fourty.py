from collections import defaultdict
# import pprint as pp

N, K = map(int, input().split())
d = defaultdict(int)
s = set()
for i in range(K):
    a, b = map(int, input().split())
    # a-=1
    b -= 1
    d[a] = b
    s.add(a)

dp = [[[0,0] for _ in range(3)] for j in range(N + 1)]
if 1 in s:
    dp[1][d[1]]=[1,0]
else:
    dp[1]=[[1,0],[1,0],[1,0]]
for i in range(2,N+1):
    for j in range(3):
        if i in s:
            dp[i][d[i]]=[(sum(dp[i-1][(d[i]+1)%3])+sum(dp[i-1][(d[i]+2)%3]))%10000,dp[i-1][d[i]][0]]
        else:
            dp[i][j]=[(sum(dp[i-1][(j+1)%3])+sum(dp[i-1][(j+2)%3]))%10000,dp[i-1][j][0]]
        
ans=0
for t in dp[-1]:
    for j in t:
        ans+=j
# pp.pprint(dp)
print(ans%10000)
