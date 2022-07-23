from itertools import product
N = int(input())

for s in product(range(2), repeat=N):
    print(s)
