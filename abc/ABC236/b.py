N = int(input())

nList = [0 for _ in range(N)]

for a in map(int, input().split()):
    nList[a-1] += 1

for i, n in enumerate(nList):
    if n != 4:
        print(i+1)
        exit()
