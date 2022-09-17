from itertools import product

N = int(input())

bin_N = bin(N)[2:]
length_bin_N = len(bin_N)
zeros = [0] * length_bin_N
# print(zeros)

one_index = [i for i, x in enumerate(bin_N) if x == '1']
# print(one_index)

pro = product([0, 1], repeat=len(one_index))

bin_ans = []

for p in pro:
    # print(p)
    current = zeros[:]
    # ans = [fo]
    for i, val in enumerate(p):
        # print(val)
        if val:
            current[one_index[i]] = val
    # print(current)
    bin_ans.append(current)
# print(bin_ans)

for b in bin_ans:
    print(int(''.join(map(str, b)), 2))
