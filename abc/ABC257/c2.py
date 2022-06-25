import bisect

N = int(input())
S = input()
W = list(map(int, input().split()))
child_list = []
adult_list = []
adult_num = 0
child_num = 0
for i in range(N):
    if S[i] == "0":
        child_list.append(W[i])
        child_num += 1
    else:
        adult_list.append(W[i])
        adult_num += 1
child_list.sort()
adult_list.sort()

ans = -1

for i, child in enumerate(reversed(child_list)):
    adult_value = adult_num - bisect.bisect_right(adult_list, child)
    ans = max(ans, adult_value + child_num - i)

for i, adult in enumerate(adult_list):
    child_value = bisect.bisect_right(child_list, adult-1)
    ans = max(ans, child_value + adult_num - i)
print(ans)
