K = int(input())

binK = bin(K)
for b in binK[2:]:
    if b == "1":
        print(2, end="")
    else:
        print(0, end="")
print()
