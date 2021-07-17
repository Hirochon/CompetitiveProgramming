from collections import deque

N, K = map(int, input().split())

c = list(map(int, input().split()))
cin = c[:K]
dq = deque(cin)

max = len(set(dq))

# for i in c[K:]:
for i in range(N-K):
    dq.popleft()
    # dq.append(i)
    dq.append(c[K+i])
    tmp = len(set(dq))
    if tmp > max:
        max = tmp

print(max)