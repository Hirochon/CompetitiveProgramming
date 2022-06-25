N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
tansaku = [True if i in A else False for i in range(1, N+1)]
# print(tansaku)
for l in L:
    num = A[l-1]
    if num == N:
        continue
    if tansaku[num]:
        continue
    tansaku[num] = True
    tansaku[num-1] = False
    A[l-1] += 1

print(*A)
