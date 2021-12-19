N, M = map(int, input().split())

abDict = {i: [] for i in range(1, N+1)}
cdDict = {i: [] for i in range(1, N+1)}
abPastDict = {i: 0 for i in range(1, N+1)}
cdPastDict = {i: 0 for i in range(1, N+1)}

for i in range(M):
    a, b = map(int, input().split())
    abDict[a].append(b)
    abDict[b].append(a)

for i in range(M):
    c, d = map(int, input().split())
    cdDict[c].append(d)
    cdDict[d].append(c)

print(abDict)
print(cdDict)


for i in range(1, N+1):
    if abPastDict[i] == 1:
        continue
    abPastDict[i] = 1
    v = abDict[i]
    tansaku = []
    for j in range(1, N+1):
        v2 = cdDict[j]
        # if len(v) == len(v2):

