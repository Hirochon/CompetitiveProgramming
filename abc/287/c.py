from collections import defaultdict, deque
N, M = map(int, input().split())
path_graph_count = defaultdict(int)
path_graph = defaultdict(list)
passed = set([i+1 for i in range(N)])

for i in range(M):
    u, v = map(int, input().split())
    path_graph_count[u] += 1
    path_graph_count[v] += 1
    path_graph[u].append(v)
    path_graph[v].append(u)

mattan_queue = []
for k, v in path_graph_count.items():
    if v % 2 != 0:
        if v == 1:
            mattan_queue.append(k)
            if len(mattan_queue) > 2:
                print('No')
                exit()
        else:
            print('No')
            exit()

if len(mattan_queue) != 2:
    print('No')
    exit()

start_point = mattan_queue[0]
next_point = path_graph[start_point][0]

queue = deque([(start_point, next_point)])
passed.remove(start_point)
while queue:
    kako, ima = queue.popleft()
    passed.remove(ima)
    for n in path_graph[ima]:
        if n == kako:
            continue
        queue.append((ima, n))
        # print("memo", kako, ima, n)

if len(passed) > 0:
    print('No')
    exit()

print('Yes')
