S1 = input()
S2 = input()
S3 = input()
T = input()

for i in range(len(T)):
    j = int(T[i])
    if j == 1:
        print(S1, end="")
    if j == 2:
        print(S2, end="")
    if j == 3:
        print(S3, end="")
print()