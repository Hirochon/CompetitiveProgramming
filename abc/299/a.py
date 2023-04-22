N = int(input())
S = input()
bou1 = -1
bou2 = -1
ten = -1
for i, s in enumerate(S):
    if s == '|' and bou1 != -1:
        bou2 = i
    if s == '|' and bou1 == -1:
        bou1 = i
    if s == '*':
        ten = i
if bou1 < ten < bou2:
    print("in")
else:
    print("out")