A, B, C, X, Y = map(int, input().split())

AB = C*2
kaburi = min(X, Y)

nX = X - kaburi
nY = Y - kaburi

ans = 0

if A + B < AB:
    ans += kaburi * (A+B)
else:
    ans += kaburi * AB

if A < AB:
    ans += nX * A
else:
    ans += nX * AB

if B < AB:
    ans += nY * B
else:
    ans += nY * AB

print(ans)
