import itertools
import numpy as np


def judge(li, T):
    answer = 0
    for i in range(Q):
        a, b, c, d = T[i]
        if li[b - 1] - li[a - 1] == c:
            answer += d
            # print(d)
    return answer


N, M, Q = map(int, input().split())
ans = 0
T = []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    T.append([a, b, c, d])


num = list(np.arange(M) + 1)
# print(num)

for tup in itertools.combinations_with_replacement(num, N):
    # num(配列)内のN個分タプルを返す
    # print(df)

    li = list(tup)
    f = judge(li, T)
    ans = max(ans, f)
print(ans)
