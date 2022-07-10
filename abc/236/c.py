N, M = map(int, input().split())

S = list(input().split())
T = list(input().split())

j = 0
for i in range(N):
    if S[i] == T[j]:
        print("Yes")
        j += 1
    else:
        print("No")
