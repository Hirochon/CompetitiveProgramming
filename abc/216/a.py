X, Y = map(int, input().split("."))

if Y < 3:
    print(X, "-", sep="")
elif Y < 7:
    print(X)
else:
    print(X, "+", sep="")