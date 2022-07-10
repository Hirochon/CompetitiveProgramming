N = int(input())

ans = set()

for i in range(N):
    L = tuple(map(int, input().split()))
    ans.add(L)
print(len(ans))