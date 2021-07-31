from collections import defaultdict

dd = defaultdict(int)

for i in range(4):
    dd[i] += 1

print(dd)
print(min(dd), max(dd))