from collections import deque, defaultdict
N = int(input())
sx, sy, tx, ty = map(int, input().split())

start_list = deque([])
n_list = [0 for _ in range(N)]
XYR = []
past_set = set([])
for i in range(N):
    x, y, r = map(int, input().split())
    XYR.append((x, y, r))
    if (x - sx)**2 + (y - sy)**2 == r**2:
        start_list.append(i)
        past_set.add(i)
    if (x - tx)**2 + (y - ty)**2 == r**2:
        n_list[i] = 2
# print(start_list, n_list)
way = defaultdict(list)
for i in range(N):
    for j in range(i, N):
        # if i == j:
        #     continue
        d = (XYR[i][0] - XYR[j][0])**2 + (XYR[i][1] - XYR[j][1])**2
        if (XYR[i][2] - XYR[j][2])**2 <= d <= (XYR[i][2] + XYR[j][2])**2:
            way[i].append(j)
            way[j].append(i)
        
# print(way)
while start_list:
    i = start_list.popleft()
    for j in way[i]:
        if n_list[j] == 2:
            print('Yes')
            exit()
        if j not in past_set:
            past_set.add(j)
            start_list.append(j)
print('No')
