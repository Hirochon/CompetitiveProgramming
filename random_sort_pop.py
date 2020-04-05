# 初動: 繰り返したい回数を入力してもらう
# ① Aで一番左側を返して削除する
# ② １〜２の間でランダム与えたられたものに返されたものを乗算する
# ③ リスト内に重なりがないか確認後に代入する
# ④ ソートして小さいもの順に並べて①に戻る
# 最後: リスト内に余った数字を出力
from random import uniform


N = int(input("繰り返したい回数を入力してください: "))
A = [2]
for i in range(N):
    porori = A.pop(0)
    for j in range(2):
        value = int(porori * uniform(1, 2))
        if value not in A:
            A.append(value)
    A.sort()
print(A)
