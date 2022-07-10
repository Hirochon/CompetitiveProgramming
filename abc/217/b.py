S1 = input()
S2 = input()
S3 = input()

s = set(["ABC", "ARC", "AGC", "AHC"])

s.remove(S1)
s.remove(S2)
s.remove(S3)

print(*s)
