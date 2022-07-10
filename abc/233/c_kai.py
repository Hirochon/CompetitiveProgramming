import sys
sys.setrecursionlimit(10**7)

N, X = map(int, input().split())

numsList = []
for i in range(N):
    nums = []
    L, *A = map(int, input().split())
    for a in A:
        if X % a == 0:
            nums.append(a)
    numsList.append(nums)

ans = 0

def dfs(div: int, num):
    global ans
    if div == N-1:
        for value in numsList[div]:
                if X == num*value:
                    ans += 1
    else:
        for value in numsList[div]:
            dfs(div+1, num*value)

dfs(0, 1)
print(ans)
