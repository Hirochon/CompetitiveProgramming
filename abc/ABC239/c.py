x1, y1, x2, y2 = map(int, input().split())

def matchXY(x, y, a, b):
    xAns11 = x + 2
    yAns11 = y + 1
    xAns12 = x + 2
    yAns12 = y - 1
    xAns13 = x - 2
    yAns13 = y + 1
    xAns14 = x - 2
    yAns14 = y - 1

    xAns21 = x + 1
    yAns21 = y + 2
    xAns22 = x - 1
    yAns22 = y + 2
    xAns23 = x + 1
    yAns23 = y - 2
    xAns24 = x - 1
    yAns24 = y - 2

    if yAns11 == xAns11*a + b:
        return True
    elif yAns12 == xAns12*a + b:
        return True
    elif yAns13 == xAns13*a + b:
        return True
    elif yAns14 == xAns14*a + b:
        return True
    elif yAns21 == xAns21*a + b:
        return True
    elif yAns22 == xAns22*a + b:
        return True
    elif yAns23 == xAns23*a + b:
        return True
    elif yAns24 == xAns24*a + b:
        return True
    else:
       return False

if x1 == x2:
    if y1 - y2 % 2 == 0:
        y = y1 - y2
        if matchXY(x1, 0, 1, y):
            print("Yes")
            exit()
    print("No")
    exit()
if y1 == y2:
    if x1 - x2 % 2 == 0:
        x = x1 - x2
        if matchXY(0, y1, x, 1):
            print("Yes")
            exit()
    else:
        print("No")
        exit()

## 傾きを求める
dx = x2 - x1
dy = y2 - y1
a = dy / dx * -1

## x1, x2とy1, y2の中間点を求める
x = (x1 + x2) / 2
y = (y1 + y2) / 2

b = y - a * x

# print("a, b", a, b)

if matchXY(x1, y1, a, b):
    print("Yes")
else:
    print("No")
