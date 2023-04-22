N = int(input())
middle = N // 2
left = 0
right = N
while True:
    if right - left == 1:
        print('! {}'.format(left))
        break
    mid = (left + right) // 2
    print('? {}'.format(mid))
    if int(input()) == 0:
        left = mid
    else:
        right = mid