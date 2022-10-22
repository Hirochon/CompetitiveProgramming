N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(2 * N + 2)]

for i in range(1, N + 1):
    # print(i)
    ans[i*2] = ans[A[i - 1]] + 1
    ans[i*2+1] = ans[A[i - 1]] + 1

# print(*ans)
for i, a in enumerate(ans):
  if i:
    print(a)