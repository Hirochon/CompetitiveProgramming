from itertools import combinations

flag = True

while flag:
    ans = 0
    n, x = map(int, input().split())

    if n == 0 and x == 0:
        flag = False
        break

    nl = [i for i in range(1, n+1)]

    for i in combinations(nl, 3):
        if sum(i) == x:
            ans += 1
    print(ans)
