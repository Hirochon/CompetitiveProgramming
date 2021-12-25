L, R = map(int, input().split())
S = input()

print(S[:L-1], end="")
for s in reversed(S[L-1:R]):
    print(s, end="")
print(S[R:], end="")
print()
