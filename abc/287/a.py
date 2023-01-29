N = int(input())

tohyo = 0

for i in range(N):
    S = input()
    if S == "For":
        tohyo += 1
    elif S == "Against":
        tohyo -= 1

if tohyo > 0:
    print("Yes")
elif tohyo < 0:
    print("No")
