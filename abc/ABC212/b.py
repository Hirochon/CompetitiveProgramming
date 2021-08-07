X = input()

flag1 = 0
flag2 = 0

for i in range(3):
    if X[i] == X[i+1]:
        flag1 += 1

    tmp = int(X[i])
    strTmp = str(tmp + 1)[-1]
    if strTmp == X[i+1]:
        flag2 += 1

if flag1 == 3 or flag2 == 3:
    print("Weak")
else:
    print("Strong")