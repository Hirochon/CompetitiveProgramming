import numpy as np

S = input()
npS = np.array([s for s in S])

def gacha(aStr):
    st = ""
    for s in aStr:
        st += s
    return st

ans = [""]*len(S)

for i in range(len(npS)):
    a = np.roll(npS, i)
    ans[i] = gacha(a)

sortedAns = sorted(ans)

print(sortedAns[0])
print(sortedAns[-1])
