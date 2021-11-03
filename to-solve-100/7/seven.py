from itertools import combinations

N = int(input())

AB = set()

for i in range(N):
    a, b = map(int, input().split())
    AB.add((a, b))

ans = 0

for ab0, ab1 in combinations(AB, 2):
    ab0x, ab0y = ab0
    ab1x, ab1y = ab1
    ## 差分
    gAb1x = ab1x - ab0x
    gAb1y = ab1y - ab0y
    ## 回転行列
    kAbx = -1 * gAb1y
    kAby = gAb1x
    ## 元に戻す
    abx1 = kAbx + ab0x
    aby1 = kAby + ab0y
    abx2 = abx1 + gAb1x
    aby2 = aby1 + gAb1y
    # print(ab)
    # print("====")
    # print(abx1, aby1)
    # print(abx2, aby2)
    # print("====")
    ## 正方形できるかチェック
    if (abx1, aby1) in AB and (abx2, aby2) in AB:
        ans = max(ans, gAb1x**2 + gAb1y**2)

print(ans)
