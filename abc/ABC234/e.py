strX = input()
x = int(strX)
maxX = 9876543210
lenX = len(strX)

if x > maxX:
    for i in range(lenX):
        print(strX[0], end="")
    print()
elif lenX < 3:
    print(x)
else:
    sx = int(strX[1]) - int(strX[0])
    if sx*lenX < 10 and sx*lenX > -10:
        for i in range(lenX):
            print(int(strX[0])+sx*i, end="")
        print()
        exit()
    else:
        for i in range(lenX):
            print(strX[0], end="")
        print()
