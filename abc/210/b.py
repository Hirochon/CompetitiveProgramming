N = int(input())

S = input()

for i, v in enumerate(S):
    if int(v) == 1:
        if i % 2 == 0:
            print("Takahashi")
            break
        else:
            print("Aoki")
            break