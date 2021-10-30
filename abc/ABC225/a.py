from itertools import permutations

S = input()
ans = set()

for s in permutations(S, 3):
    ans.add(s)

print(len(ans))