N = int(input())

ans = "1"

for i in range(2, N+1):
    ans = ans + " " + str(i) + " " + ans

print(ans)
