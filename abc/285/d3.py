from collections import defaultdict, deque
N = int(input())
V = {}
into_num = defaultdict(int)
original_num = set()
for _ in range(N):
    s, t = input().split()
    V[s] = t
    into_num[s] += 0
    into_num[t] += 1
    original_num.add(s)
    original_num.add(t)

# print(into_num)

def sort_chon(into_num: defaultdict, V: dict) -> list:
    queue = deque()
    ans = []
    for key, value in into_num.items():
        if value == 0:
            queue.append(key)
            ans.append(key)
    # print(queue)
    while queue:
        q = queue.popleft()
        if q in V:
            into_num[V[q]] -= 1
            if into_num[V[q]] == 0:
                queue.append(V[q])
                ans.append(V[q])
    return ans

result = sort_chon(into_num, V)
# print(result)
if len(result) == original_num.__len__():
    print("Yes")
else:
    print("No")
