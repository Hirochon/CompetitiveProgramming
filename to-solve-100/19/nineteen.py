import bisect

d = int(input())
n = int(input())
m = int(input())

D = [0]
K = []

for i in range(n-1):
    di = int(input())
    D.append(di)

for i in range(m):
    ki = int(input())
    K.append(ki)

D.sort()

ans = 0
for k in K:
    bsI = bisect.bisect_left(D,k)
    
    if bsI < n:
        if D[bsI] == k:
            continue

        if bsI == 0:
            ans += min(k - D[bsI], d - k)
        else:
            ans += min(k - D[bsI-1], abs(k - D[bsI]), d - k)
    else:
        ans += min(k - D[bsI-1], d - k)

    # print("ans", ans)

print(ans)
