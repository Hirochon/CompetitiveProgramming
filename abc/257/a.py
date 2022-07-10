N, X = map(int, input().split())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
for a in alphabet:
    for i in range(N):
        ans += a

print(ans[X-1])
