## 入力される値の数
n = int(input())
## 入力される値の配列
S = list(map(int, input().split()))

## ズレが0だと最大indexに範囲が及ばない
def binarySearch(x: int) -> bool:
    minI = 0
    maxI = n - 1
    while minI - maxI != 1:
        middleI = (minI + maxI) // 2
        if S[middleI] == x:
            return True
        elif S[middleI] < x:
            ## ターゲットとする値より当てずっぽ値が小さければ、
            ## 最小を中間の値+1のindexに変更
            minI = middleI+1
        else:
            ## ターゲットとする値より当てずっぽ値が大きければ、
            ## 最大を中間の値-1のindexに変更
            maxI = middleI-1
    return False
