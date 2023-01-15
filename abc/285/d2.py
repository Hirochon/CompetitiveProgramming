from collections import deque

N = int(input())
queue = deque([])
TS = []
st_map = {}

for _ in range(N):
    s, t = input().split()
    TS.append((t, s))
    st_map[s] = t

for t, s in sorted(TS):
    queue.append((s, t, True))

passed = set()
while queue:
    s, t, b = queue.popleft()
    print(s, t, b)
    if b and (s, t) in passed:
        continue
    if not b and (s, t) in passed:
        print("No")
        exit()
    if len(passed) == N:
        break
    passed.add((s, t))
    if t in st_map:
        queue.appendleft((t, st_map[t], False))

print("Yes")
