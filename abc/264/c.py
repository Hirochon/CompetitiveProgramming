H1, W1 = map(int, input().split())
A = []
for i in range(H1):
    a = list(map(int, input().split()))
    A.append(a)
H2, W2 = map(int, input().split())
B = []
for i in range(H2):
    b = list(map(int, input().split()))
    B.append(b)

ans = {}
uniq = set()
k = 0
for i in range(H2):
    for j in range(W2):
        uniq.add(B[i][j])
        ans[B[i][j]] = k
        k += 1

## 
