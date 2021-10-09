N, P = map(int, input().split())

A = [i for i in map(int, input().split())]

ans = 0

for i in A:
    if i < P:
        ans += 1

print(ans)