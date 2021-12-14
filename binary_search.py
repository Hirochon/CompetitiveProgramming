## 入力される値の数
n = int(input())
## 入力される値の配列
S = list(map(int, input().split()))

## ズレが0だと最大indexに範囲が及ばない
def binarySearch(x: int) -> bool:
    min = 0
    max = n - 1
    while min - max != 1:
        middle = (min + max) // 2
        if S[middle] == x:
            return True
        elif S[middle] < x:
            ## ターゲットとする値より大きければ、
            ## 最小を中間の値+1のindexに変更
            min = middle+1
        else:
            ## ターゲットとする値より小さければ、
            ## 最大を中間の値-1のindexに変更
            max = middle-1
    return False
