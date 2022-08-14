R, C = map(int, input().split())

if R + C <= 16:
    if min(R, C) % 2 == 1:
        print('black')
    elif min(R, C) % 2 == 0:
        print('white')
else:
    if max(R, C) % 2 == 1:
        print('black')
    elif max(R, C) % 2 == 0:
        print('white')
