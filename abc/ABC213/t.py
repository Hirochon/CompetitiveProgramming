from bisect import insort
import bisect

s = [[] for _ in range(3)]

for i in range(3):
    bisect.insort(s[i], i*2)
    bisect.insort(s[i], i*1)
    bisect.insort(s[i], i*3)

print(s)

a = set()
print(len(a))
a.add(2)
print(len(a))
a.add(3)
print(len(a))
if 2 not in a:
    print("ssss")