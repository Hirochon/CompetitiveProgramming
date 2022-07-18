import bisect
from collections import defaultdict
N, K = map(int, input().split())
P = list(map(int, input().split()))
p_master = [0 for _ in range(N)]
for i, p in enumerate(P):
    p_master[p-1] = i

dd = defaultdict(list)
# bil = [P[0]]
# dd[P[0]].append(0)
bil = []

ans = [-1 for _ in range(N)]
# if K == 1:
#     ans[0] = 0

for i, p in enumerate(P):
    index = bisect.bisect_left(bil, p)
    flag = True
    if index == len(bil):
        bil.append(p)
        flag = False
    dd[bil[index]].append(i+1)
    if flag:
        dd[p] = dd[bil[index]]
        del dd[bil[index]]
    bil[index] = p
    # print("i:", i, "p:", p, "index:", index, "dd:", dict(dd), "bil:", bil)

    if len(dd[bil[index]]) == K:
        for v in dd[bil[index]]:
            ans[v-1] = i
        del dd[bil[index]]
        bil.pop(index)
    # print("ans:", ans)

# print(ans)

for i in range(N):
    if ans[p_master[i]] == -1:
        print(-1)
    else:
        print(ans[p_master[i]]+1)
