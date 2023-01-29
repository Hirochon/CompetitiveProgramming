from collections import defaultdict
N, M = map(int, input().split())
S = []
# T = defaultdict(int)
T = set()

for i in range(N):
    S.append(input())
for i in range(M):
    t = input()
    # T[t] += 1
    T.add(t)

count = 0
# print(T)

for i in range(N):
    s = S[i][3:]
    # if s in T and T[s] > 0:
    if s in T:
        # count += T[s]
        count += 1
    # print(T)

print(count)
