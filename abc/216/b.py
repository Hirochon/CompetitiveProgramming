N = int(input())

ans = set()

for i in range(N):
    S = input()
    if S in ans:
        print("Yes")
        exit()
    ans.add(S)
print("No")