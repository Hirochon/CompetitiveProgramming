from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
set_A = set(A)
set_sorted_A = sorted(set_A)

current_num = 0
p_ans_dict = {}
for a in set_sorted_A[::-1]:
    p_ans_dict[a] = current_num
    current_num += 1
ans_dict = defaultdict(int)
for a in A:
    ans_dict[p_ans_dict[a]] += 1

for i in range(N):
    print(ans_dict[i])
