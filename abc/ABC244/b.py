N = int(input())

T = input()

## 東:0 南:1 西:2 北:3
muki = 0

## 0:東, 1:北
xy = [0, 0]

def move(muki, xy):
    if muki == 0:
        xy = [xy[0] + 1, xy[1]]
    elif muki == 1:
        xy = [xy[0], xy[1] - 1]
    elif muki == 2:
        xy = [xy[0] - 1, xy[1]]
    elif muki == 3:
        xy = [xy[0], xy[1] + 1]
    return xy

for t in T:
    if t == 'S':
        xy = move(muki, xy)
    if t == 'R':
        muki = (muki + 1) % 4

print(xy[0], xy[1])
