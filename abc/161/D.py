K = int(input())
if K <= 12:
    print(K)
else:
    i = flag = 12
    while(K != flag):
        i += 1
        bunkai = list(str(i))
        length = len(bunkai)
        flag2 = 0
        for j in range(length - 1):
            if bunkai[j] == bunkai[j + 1] or (abs(int(bunkai[j]) - int(bunkai[j + 1])) == 1):
                flag2 += 1
                continue
            else:
                break
        if flag2 == (length - 1):
            flag += 1
    print(i)
