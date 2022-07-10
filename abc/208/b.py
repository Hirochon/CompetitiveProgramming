P = int(input())

kaijo_list = []

j = 1
ans = 0

for i in range(1, 11):
    j *= i
    kaijo_list.append(j)

for i in range(10):
    num = kaijo_list[9 - i]
    while P >= num:
        P -= num
        ans += 1
    if P == 0:
        break

print(ans)
