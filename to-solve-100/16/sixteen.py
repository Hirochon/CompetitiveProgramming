from itertools import permutations

N = int(input())

P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

a = 0
b = 0

for i, v in enumerate(permutations(range(1, N+1), N)):
    # print(v, P, Q)
    if v == P:
        a = i
    if v == Q:
        b = i

print(abs(a-b))
