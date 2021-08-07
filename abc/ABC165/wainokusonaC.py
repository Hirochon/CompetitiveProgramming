def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


# N nagasa M saidaiti Q kumisuu
N, M, Q = map(int, input().split())
ans_dict = {}
ans = 0
for i in range(Q):
    a_s, b_s, c_s, d_s = map(int, input().split())
    key = str(a_s) + str(b_s) + str(c_s)
    if key in ans_dict:
        ans_dict[key] += d_s
    else:
        ans_dict[key] = d_s
ans_list = list(ans_dict.values())
ans_list = sorted(ans_list, reverse=True)
ans_keys = list(ans_dict.keys())
key_dict = {}
for an_ke in ans_keys:
    if an_ke[:-1] not in key_dict:
        key_dict[an_ke[:-1]] = ans_dict[an_ke]
    else:
        if key_dict[an_ke[:-1]] < ans_dict[an_ke]:
            key_dict[an_ke[:-1]] = ans_dict[an_ke]
# iketeru
# print(key_dict.items())

key_dict.values()
# ans_keys_kai = [x[:-1] for x in ans_keys]
# atai wo syutoku
# key_s = []
# key_s.append(get_keys_from_value(ans_dict, ans_list[0])[0][:-1])
# # print(key_s)
# ans += ans_list[0]
# flag_s = 1
# i = 0
# while(flag_s != N - 1):
#     i += 1
#     ke = get_keys_from_value(ans_dict, ans_list[i])[0][:-1]
#     if ke[:-1] not in key_s:
#         key_s.append(ke)
#         ans += ans_list[i]
#         flag_s += 1
# print(ans)
