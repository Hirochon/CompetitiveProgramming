N, S = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

def saiki(i, forS, plusS):
    if forS == S:
        return plusS
    if i == N:
        return ""
    if forS > S:
        return ""
    s1 = saiki(i+1, forS+A[i], plusS+"H")
    s2 = saiki(i+1, forS+B[i], plusS+"T")
    if s1 != "":
        return s1
    if s2 != "":
        return s2
    return ""

ans = saiki(0, 0, "")
if ans == "":
    print("No")
else:
    print("Yes")
    print(ans)
