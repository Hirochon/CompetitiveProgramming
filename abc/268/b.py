S = input()
T = input()

sentouFlag = False
totyuFlag = False
for i in range(len(T)-len(S)+1):
    ssFlag = True
    for j in range(len(S)):
        if T[i+j] != S[j]:
            ssFlag = False
            break
    if i == 0 and ssFlag:
        sentouFlag = True
    if i == 0 and not ssFlag:
        totyuFlag = True
        break

if sentouFlag and (not totyuFlag):
    print("Yes")
else:
    print("No")
