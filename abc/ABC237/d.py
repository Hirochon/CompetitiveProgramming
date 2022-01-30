from collections import deque

N = int(input())
S = input()
ans = deque([N])
# print(ans)

for i, s in enumerate(S[::-1]):
    if s == "R":
        ans.appendleft(N - i - 1)
    else:
        ans.append(N - i - 1)

for a in ans:
    print(a, end=" ")
print()
