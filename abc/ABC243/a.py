V, A, B, C = map(int, input().split())

ABC = [A, B, C]

while V >= 0:
    for i in range(3):
        V -= ABC[i]
        if V < 0:
            if i == 0:
                print('F')
                exit()
            elif i == 1:
                print('M')
                exit()
            else:
                print('T')
                exit()
