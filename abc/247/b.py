from collections import defaultdict

N = int(input())
mList = []
dd = defaultdict(int)

for i in range(N):
    s, t = input().split()
    mList.append((s, t))
    dd[s] += 1
    dd[t] += 1
# print(dd)
new_list = []

for s, t in mList:
    if dd[s] > 1 or dd[t] > 1:
        new_list.append((s, t))
# print(new_list)
new_dd = defaultdict(int)
for s, t in new_list:
    new_dd[s] += 1
    new_dd[t] += 1
# print(new_dd)
for s, t in new_list:
    if new_dd[s] > 1 and new_dd[t] > 1:
        if s == t and new_dd[s] == 2:
            continue
        print('No')
        exit()
print('Yes')