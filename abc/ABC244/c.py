# import sys
N = int(input())

sets = set()

for i in range(N*2+1):
    sets.add(i+1)
# print(sets)
n = 0
for i in range(N*2 + 1):
    if i % 2 == 0:
        v = sets.pop()
        print(v)
        # print("i", i)
        # sys.stdout.flush()
    else:
        v = int(input())
        if v in sets:
            sets.remove(v)

v = input()
if v == 0:
    exit()
