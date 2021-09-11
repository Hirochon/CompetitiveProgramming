alpha = "abcdefghijklmnopqrstuvwxyz"
P = [i for i in map(int, input().split())]

for i in P:
    print(alpha[i-1], end="")
print()