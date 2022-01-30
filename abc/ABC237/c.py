S = input()

s_len = len(S)
j1 = -1
for i, s in enumerate(S[::-1]):
    if s == "a":
        continue
    j1 = i
    break

if j1 != -1:
    S = S[:s_len-j1]
# print(S)

j2 = -1
for i, s in enumerate(S):
    if j1 == i:
        j2 = j1
        break
    if s == "a":
        continue
    j2 = i
    break

if j2 != -1:
    formated_S = S[j2:]
else:
    formated_S = S
# print(formated_S)

def is_palindrome(str):
    return 1 if str == str[::-1] else 0

if is_palindrome(formated_S):
    print("Yes")
else:
    print("No")
