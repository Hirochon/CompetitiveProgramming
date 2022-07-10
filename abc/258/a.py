K = int(input())

h = K // 60 + 21
if K >= 60:
    m = K - 60
else:
    m = K

print("{}:{:02d}".format(h, m))
