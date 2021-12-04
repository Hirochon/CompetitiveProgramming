from itertools import product

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

s = set([sum([A[i] if v[i] else 0 for i in range(n)]) for v in product(range(2), repeat=n)])

for m in M:
    if m in s:
        print("yes")
    else:
        print("no")
