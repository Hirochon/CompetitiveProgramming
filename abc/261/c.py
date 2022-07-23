from collections import defaultdict
N = int(input())
S = []
dd = defaultdict(int)
past = set()
for i in range(N):
    s = input()
    S.append(s)

for i in range(N):
    # print(past, dd)
    if S[i] not in past:
        past.add(S[i])
        dd[S[i]] += 1
        print(S[i])
    else:
        print(S[i], "(", dd[S[i]], ")", sep="")
        dd[S[i]] += 1
