X = input()
Y = input()
if (len(X) + 1 == len(Y)) and (X == Y[:-1]):
    print("Yes")
else:
    print("No")
