S = input()

max = 0
count = 0

ansSet = set(["A", "G", "C", "T"])

for s in S:
    if s in ansSet:
        count += 1
        if max < count:
            max = count
    else:
        count = 0

print(max)
