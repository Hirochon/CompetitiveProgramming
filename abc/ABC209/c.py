N = int(input())

C = sorted(list(map(int, input().split())))

ans = 1

for i in range(N):
    ans *= (C[i] - i)
    if ans > (1e9 + 7):
        ans %= int(1e9 + 7)
print(ans)