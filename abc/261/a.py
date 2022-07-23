L1, R1, L2, R2 = map(int, input().split())

ans = 0

for i in range(101):
    if L1 <= i < R1:
        # print(i)
        if L2 <= i < R2:
            # print(i)
            ans += 1

print(ans)
