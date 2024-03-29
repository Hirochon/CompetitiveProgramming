from itertools import product

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

set_values = set()
for values in product(range(2), repeat=n):
    sum_num = 0
    for i, v in enumerate(values): 
        # print(i, v, A[i])
        if v:
            sum_num += A[i]
    set_values.add(sum_num)

for mm in m:
    if mm in set_values:
        print("yes")
    else:
        print("no")
