S = input()
b1 = -1
b2 = -1
r1 = -1
r2 = -1
k = -1
for i, s in enumerate(S):
    if s == "B":
        if b1 == -1:
            b1 = i
        else:
            b2 = i
    if s == "R":
        if r1 == -1:
            r1 = i
        else:
            r2 = i
    if s == "K":
        k = i

if (b1 + b2) % 2 == 1:
    if r1 < k < r2:
        print("Yes")
        exit()
print("No")
