a = list(map(int, input().split()))
k = a[0]
a[0] = a[1]
a[1] = k
k = a[0]
a[0] = a[2]
a[2] = k
print(a[0], a[1], a[2], sep=' ')
