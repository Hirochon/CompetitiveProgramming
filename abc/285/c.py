S = input()

alphabet_mapping = {s: i+1 for i, s in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

ans = 0
kake = 1
for i, s in enumerate(reversed(S)):
    # print(s)
    # print(alphabet_mapping[s])
    ans += alphabet_mapping[s] * kake
    kake *= 26
    # print(ans)
print(ans)