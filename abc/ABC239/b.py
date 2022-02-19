X = int(input())
strX = str(X)

if strX[0] == "-":
    if strX[-1] == "0":
        print(strX[:-1])
    else:
        if len(strX) == 2:
            print("-1")
        else:
            print(int(strX[:-1]) - 1)
            # print(strX[:-2] + str(int(strX[-2]) + 1))
else:
    if len(strX) == 1:
        print("0")
    else:
        print(strX[:-1])