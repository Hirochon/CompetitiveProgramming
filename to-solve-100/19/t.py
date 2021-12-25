import bisect

S = [0,4,2,1,8]

S.sort()

## 探している値をそのまま表すならば基準
print(bisect.bisect_left(S, -1)) # 0
print(bisect.bisect_left(S, 2)) # 2
print(bisect.bisect_left(S, 3)) # 3
print(bisect.bisect_left(S, 8)) # 4
print(bisect.bisect_left(S, 9)) # 5

## 探している値をindexにするなら基準
print(bisect.bisect_right(S, -1)) # 0
print(bisect.bisect_right(S, 2)) # 3
print(bisect.bisect_right(S, 3)) # 3
print(bisect.bisect_right(S, 8)) # 5
print(bisect.bisect_right(S, 9)) # 5
