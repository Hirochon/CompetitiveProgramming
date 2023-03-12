S = input()
S_list = [s for s in S]

for i in range(len(S_list) // 2):
    tmp = S_list[i*2+1]
    S_list[i*2+1] = S_list[i*2]
    S_list[i*2] = tmp
for s in S_list:
    print(s, end='')
print()