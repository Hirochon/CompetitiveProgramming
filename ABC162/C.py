from math import gcd
from functools import reduce


def gcd_kai(*numbers):
    return reduce(gcd, numbers)


K = int(input())
ans = 1
if K == 1:
    next
else:
    ans += (K - 1) * K * 3
    ans_sub = 0
    for i in range(2, K):
        for j in range(i + 1, K + 1):
            for k in range(i, K + 1):
                ans_sub += gcd_kai(i, j, k)
    ans += ans_sub * 3
    for i in range(2, K + 1):
        ans += i
print(ans)
