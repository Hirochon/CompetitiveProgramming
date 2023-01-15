N = int(input())
ST = []
st_map = {}
pass_set = set()

for _ in range(N):
    s, t = input().split()
    ST.append((t, s))
    st_map[s] = t

def saiki(pass_set, t):
    if t in pass_set:
        return (pass_set, True)
    if t not in st_map:
        return (pass_set, False)
    pass_set.add(t)
    return saiki(pass_set, st_map[t])


for t, s in sorted(ST):
    # print("st", s, t)
    if s in pass_set:
        continue
    # pass_set.add(s)
    pass_set, flag = saiki(pass_set, t)
    if flag:
        print("No")
        exit()

print("Yes")
