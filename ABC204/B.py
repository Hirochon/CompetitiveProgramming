N = int(input())

ans = 0

A = map(int, input().split())

for a in A:
    if (a > 10):
        a -= 10
        ans += a

print(ans)
