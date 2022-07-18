from collections import defaultdict
N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_tuple_list = []
b_tuple_list = []
ab_tuple_list = []
for i in range(N):
    a_tuple_list.append((A[i], i))
    b_tuple_list.append((B[i], i))
    ab_tuple_list.append((A[i] + B[i], i))

a_tuple_list.sort()
a_tuple_list.reverse()
b_tuple_list.sort()
b_tuple_list.reverse()
ab_tuple_list.sort()
ab_tuple_list.reverse()

# print(a_tuple_list)
# print(b_tuple_list)
# print(ab_tuple_list)

a_dict = defaultdict(list)
b_dict = defaultdict(list)
ab_dict = defaultdict(list)
for i in range(N):
    a_dict[a_tuple_list[i][0]].append(a_tuple_list[i][1])
    b_dict[b_tuple_list[i][0]].append(b_tuple_list[i][1])
    ab_dict[ab_tuple_list[i][0]].append(ab_tuple_list[i][1])

# print(a_dict)
# print(b_dict)
# print(ab_dict)

ans = set()

i = 0
j = 0
k = 0
while i < X:
    value = a_tuple_list[j][0]
    # print(a_dict[value])
    # print(a_dict[value][::-1][k])
    if a_dict[value][::-1][k] not in ans:
        ans.add(a_dict[value][::-1][k])
        i += 1
    k += 1
    if len(a_dict[value]) == k:
        j += 1
        k = 0

i = 0
j = 0
k = 0
while i < Y:
    value = b_tuple_list[j][0]
    # print(b_dict[value])
    # print(b_dict[value][::-1][k])
    if b_dict[value][::-1][k] not in ans:
        ans.add(b_dict[value][::-1][k])
        i += 1
    k += 1
    if len(b_dict[value]) == k:
        j += 1
        k = 0

i = 0
j = 0
k = 0
while i < Z:
    value = ab_tuple_list[j][0]
    # print(ab_dict[value])
    # print(ab_dict[value][::-1][k])
    if ab_dict[value][::-1][k] not in ans:
        ans.add(ab_dict[value][::-1][k])
        i += 1
    k += 1
    if len(ab_dict[value]) == k:
        j += 1
        k = 0

answer = sorted(list(ans))
for a in answer:
    print(a+1)
