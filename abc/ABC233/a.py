import math

X, Y = map(int, input().split())

sa = (Y - X)

if sa < 1:
    print(0)
elif sa % 10 == 0:
    print(sa//10)
else:
    ss = str(sa)
    if len(ss) > 1:
        print(int(ss[:-1])+1)
    else:
        print(1)
    # print(ss[:-1])
