from collections import defaultdict

N = int(input())

dd = defaultdict(set)

for i in range(N-1):
    a, b = map(int, input().split())
    dd[a].add(b)
    dd[b].add(a)

for i in range(1, N+1):
    if len(dd[i]) == N-1:
        print("Yes")
        exit()
print("No")