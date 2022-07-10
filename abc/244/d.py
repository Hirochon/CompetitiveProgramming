S1, S2, S3 = input().split()
T1, T2, T3 = input().split()

point = 0

if S1 == T1:
    point += 1
if S2 == T2:
    point += 1
if S3 == T3:
    point += 1

if point == 0:
    print("Yes")
elif point == 1:
    print("No")
elif point == 3:
    print("Yes")
