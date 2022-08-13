S = input()
a_dict = {"a": 1, "t": 2, "c": 3, "o": 4, "d": 5, "e": 6, "r": 7}

S_num_string = []
for s in S:
    S_num_string.append(str(a_dict[s]))
# print(S_num_string)
ans = 0
## バブルソートを使ってソートする
for i in range(len(S_num_string)):
    for j in range(len(S_num_string)-1, i, -1):
        if S_num_string[j] < S_num_string[j-1]:
            S_num_string[j], S_num_string[j-1] = S_num_string[j-1], S_num_string[j]
            ans += 1
print(ans)
# print(S_num_string)
