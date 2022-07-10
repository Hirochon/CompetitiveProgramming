N = int(input())
S = input()
W = list(map(int, input().split()))
child_list = []
adult_list = []
adult_num = 0
child_num = 0
for i in range(N):
    if S[i] == "0":
        child_list.append(i)
        child_num += 1
    else:
        adult_list.append(i)
        adult_num += 1
ans = -1
sorted_adult_list = sorted(adult_list)
sorted_child_list = sorted(child_list)
adult_i = 0
child_i = -1
while adult_i != len(adult_list):
    if sorted_adult_list[adult_i] > sorted_child_list[child_i]:
        ans = max(ans, len(sorted_adult_list[adult_i:]) + len(sorted_child_list[:child_num+child_i+1]))
        break
    
