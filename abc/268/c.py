from collections import defaultdict
N = int(input())
P = list(map(int, input().split()))

ddInt = defaultdict(int)
# ddList = defaultdict(list)

for i, p in enumerate(P):
    real_value1 = p
    real_value2 = p + 1
    real_value3 = p - 1 + N

    sabun1 = (real_value1 + N - i) % N
    sabun2 = (real_value2 + N - i) % N
    sabun3 = (real_value3 + N - i) % N

    ddInt[sabun1] += 1
    ddInt[sabun2] += 1
    ddInt[sabun3] += 1

# print(ddInt)
print(max(ddInt.values()))
