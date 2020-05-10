A, B, C, K = map(int, input().split())
ans = 0
flag = 0
if A > 0:
    if K > A:
        ans += A
        K -= A
    else:
        ans += K
        flag += 1
if B > 0 and flag == 0:
    K -= B
    if K < 1:
        flag += 1
if C > 0 and flag == 0:
    if K > C:
        ans -= C
    else:
        ans -= K
print(ans)
