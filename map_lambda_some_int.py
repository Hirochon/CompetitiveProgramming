# a = map(int, input().split())
# print(a)
# a, b, c = map(int, input().split())
# print(a, b, c)
# d, e, f = map(lambda x: int(x)**2, input().split())
# print(d, e, f)
a = map(lambda x: int(x)**2, input().split())
for b in a:
    print(b, end=' ')
