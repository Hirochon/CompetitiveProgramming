N, K = map(int, input().split())
ans_list = [0 for x in range(N)]
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for j in range(d):
        ans_list[A[j] - 1] += 1
ans = ans_list.count(0)
print(ans)
