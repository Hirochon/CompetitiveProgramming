from collections import defaultdict

Q = int(input())
dd = defaultdict(int)

ini = 0

for i in range(Q):
    query = [v for v in map(int, input().split())]
    if len(query) != 1:
        cal = query[0]
        value = query[1]
        if cal == 1:
            value -= ini
            dd[value] += 1
        elif cal == 2:
            ini += value
    else:
        minValue = min(dd)
        dd[minValue] -= 1
        if dd[minValue] == 0:
            del dd[minValue]
        print(minValue + ini)