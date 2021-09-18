X = input()
m = "abcdefghijklmnopqrstuvwxyz"

dic = {x:m[i] for i, x in enumerate(X)}
newDic = {}

N = int(input())
sortS = [""]*N

for i in range(N):
    S = input()
    newS = ""
    for j in range(len(S)):
        newS += dic[S[j]]
    newDic[newS] = S
    sortS[i] = newS

for s in sorted(sortS):
    print(newDic[s])
