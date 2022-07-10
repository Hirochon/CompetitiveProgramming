X = float(input())
ans = 100
i = 0
while(ans < X):
    i += 1
    ans = (float(ans) * 1.01) // 1

print(i)
