T = int(input())
TEST = []
for _ in range(T):
    test = int(input())
    TEST.append(test)

for test in TEST:
    MAX = int(test**(1/3))
    # print(MAX)
    for i in range(2, MAX+1):
        if test % (i**2) == 0:
            b = test // (i**2)
            a = i
            print(a, b)
            break
        elif test % i == 0:
            a2 = test // i
            a = int(a2**(1/2))
            if a**2 == a2:
                b = i
                print(a, b)
                break
