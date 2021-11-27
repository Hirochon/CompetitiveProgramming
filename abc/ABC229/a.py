S1 = input()
S2 = input()

S = S1 + S2

if S.count("#") > 2:
    print("Yes")
else:
    if S1[0] == S1[1] and S1[0] == "#":
        print("Yes")
    elif S2[0] == S2[1] and S2[0] == "#":
        print("Yes")
    elif S2[0] == S1[0] and S2[0] == "#":
        print("Yes")
    elif S2[1] == S1[1] and S2[1] == "#":
        print("Yes")
    else:
        print("No")
