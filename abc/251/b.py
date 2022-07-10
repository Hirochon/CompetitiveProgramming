from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)
A.append(0)

sets = set()
for (a1, a2, a3) in combinations(A, 3):
    if a1 + a2 + a3 <= W:
        sets.add((a1 + a2 + a3))
print(len(sets))