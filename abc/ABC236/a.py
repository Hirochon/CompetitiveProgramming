S = input()

a, b= map(int, input().split())

for i, s in enumerate(S):
    if i == a-1:
        print(S[b-1], end="")
    elif i == b-1:
        print(S[a-1], end="")
    else:
        print(s, end="")
print()