S = input()
v1 = False
v2 = False
v3 = True

big_alpha = set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
small_alpha = set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])

for i, s in enumerate(S):
    for j in range(len(S)):
        if i == j:
            continue
        if s == S[j]:
            v3 = False
    if s in big_alpha:
        v1 = True
    if s in small_alpha:
        v2 = True

if v1 and v2 and v3:
    print("Yes")
else:
    print("No")
