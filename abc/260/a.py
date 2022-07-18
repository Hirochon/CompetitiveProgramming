from collections import defaultdict
S = input()

ans = defaultdict(int)
for i in range(len(S)):
    ans[S[i]] += 1

for s in S:
    if ans[s] == 1:
        print(s)
        exit()
print(-1)
