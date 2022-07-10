S = input()
T = input()

alpha = "abcdefghijklmnopqrstuvwxyz"
alphaDic = {v: i for i, v in enumerate(alpha)}
aLen = 26

# print(alphaDic[S[0]])
# print(alphaDic[T[0]])

sInitNum = alphaDic[S[0]]
tInitNum = alphaDic[T[0]]

for i in range(32):
    if tInitNum == (sInitNum + i) % aLen:
        break
K = i
# print(K)

for s, t in zip(S, T):
    # print(s, t)
    # print(alphaDic[s], alphaDic[t])
    if alphaDic[t] != (alphaDic[s] + K) % aLen:
        print("No")
        exit()
print("Yes")