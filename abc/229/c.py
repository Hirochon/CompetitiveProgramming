N, W = map(int, input().split())

sList = [()]*N

for i in range(N):
    a, b = map(int, input().split())
    sList[i] = (a, b)

sList.sort()

ans = 0

for a, b in sList[::-1]:
    if W - b > 0:
        ans += a*b
        W -= b
    else:
        ans += W*a
        break
    # print(a, b, ans, W)

print(ans)
