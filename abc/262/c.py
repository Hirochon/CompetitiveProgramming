N = int(input())

sorottemasu = 0
soroemasu = 0
ans = 0
a_dict = {}
a_set = set()
i = 0
for a in map(int, input().split()):
    # print(i, a)
    if i+1 == a:
        sorottemasu += 1
        if sorottemasu != 1:
            if ans == 0:
                ans += 1
            ans *= (sorottemasu - 1)
    elif a in a_set:
        if a_dict[a] == i+1:
            soroemasu += 1
    if a > i+1:
        a_set.add(i+1)
        a_dict[i+1] = a
    i += 1

# print(ans, soroemasu)
ans += soroemasu

print(ans)
