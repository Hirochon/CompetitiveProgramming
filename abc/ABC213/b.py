N = int(input())

A_map = map(int, input().split())

num_1 = -1
num_1_p = 0
num_2 = -2
num_2_p = 0

for i, v in enumerate(A_map):
    if v > num_1:
        num_2 = num_1
        num_1 = v

        num_2_p = num_1_p
        num_1_p = i + 1

    elif v > num_2:
        num_2 = v
        num_2_p = i + 1
print(num_2_p)