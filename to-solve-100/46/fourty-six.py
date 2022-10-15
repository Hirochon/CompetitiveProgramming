n = int(input())
p = [None] * (n+1)# i番目の列数 = i+1番目の行数
for i in range(n):
  p[i], p[i+1] = map(int, input().split())

INF = 10**18
m = [[None] * n for _ in range(n)]
for i in range(n):
  m[i][i] = 0
  
for l in range(2,n+1):# 行列の連鎖数
  for i in range(n-l+1):
    j = i + l - 1# [i, j]の範囲の計算の最小コストを考える
    m[i][j] = INF
    for k in range(i,j):
      m[i][j] = min(m[i][j], m[i][k]+m[k+1][j] + p[i-1]*p[k]*p[j])

print(m[0][n-1])