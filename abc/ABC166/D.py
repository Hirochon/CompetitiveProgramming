import itertools


X = int(input())
ans_A = 0
ans_B = 0
for i, j in itertools.combinations(range(-120, 120), 2):
    j *= -1
    if i**5 - j**5 == X:
        ans_A = i
        ans_B = j
        break
print(ans_A, ans_B)
