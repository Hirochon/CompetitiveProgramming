A, B = input().split()

if A > B:
    moL = len(B)
else:
    moL = len(A)

for i in range(moL):
    i += 1
    i *= -1
    if int(A[i]) + int(B[i]) >= 10:
        print("Hard")
        exit()
print("Easy")
