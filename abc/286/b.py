N = int(input())
S = input()

ans = ""

flag = False
for i in range(N):
    if S[i] == "n":
        flag = True
        ans += S[i]
    elif flag and S[i] == "a":
        ans += "ya"
        flag = False
    else:
        ans += S[i]
        flag = False
print(ans)
