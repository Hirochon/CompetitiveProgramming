N = int(input())
S = input()
ans = -1
count = -1
minus_flag = False

for s in S:
    if s == 'o':
        if count == -1:
            count = 1
        else:
            count += 1
        continue
    if s == '-':
        minus_flag = True
        ans = max(ans, count)
        count = -1
if minus_flag:
    ans = max(ans, count)
print(ans)
