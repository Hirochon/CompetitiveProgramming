N = int(input())
A = list(map(int, input().split()))

sorottemasu = 0
soroemasu = 0
ans = 0
i=0
for a in A:
    # print(i, a)
    if i+1 == a:
        sorottemasu += 1
        if sorottemasu != 1:
            if ans == 0:
                ans += 1
            ans *= (sorottemasu - 1)
    elif A[a-1] == i+1:
        soroemasu += 1
    i += 1

# print(ans, soroemasu)
ans += soroemasu // 2

print(ans)
