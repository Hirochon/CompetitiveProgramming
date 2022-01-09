n = int(input())
nList = []
for i in range(n):
    u, k, *v = map(int, input().split())
    nList.append(v)
# print("nList", nList)
ans = [[0, 0] for _ in range(n)]
def dfs(kNum, depth):
    if ans[kNum][0] != 0:
        return depth
    depth += 1
    # print("kNum, depth", kNum, depth)
    ans[kNum][0] = depth
    for num in nList[kNum]:
        # print("num:", num-1)
        depth = dfs(num-1, depth)
    depth += 1
    ans[kNum][1] = depth
    return depth

d = 0
for i in range(n):
    if ans[i][0] == 0:
        d = dfs(i, d)

for i, a in enumerate(ans):
    print(i+1, *a)
