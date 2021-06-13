import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))

x = []

x.append(a[0] - 1)

for i in range(1, n):
    if a[i] - a[i - 1] > 1:
        x.append(x[-1] + a[i] - a[i - 1] - 1)
    else:
        x.append(x[-1])

for i in range(q):
    k = int(input())
    if x[n - 1] < k:
        print(a[n - 1] + k - x[n - 1])
    else:
        index = bisect.bisect_left(x, k)
        print(a[index] - 1 - x[index] + k)
