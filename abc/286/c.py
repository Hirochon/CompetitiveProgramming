N, A, B = map(int, input().split())
S = input()

min_cost = 1e18
ans = 0

for i in range(N):
    # print(S)
    cost = i*A
    count = 0
    for j in range(N//2):
        if S[j] != S[N-j-1]:
            count += 1
        # print(S[j], S[N-j-1])
    cost += B*count
    if cost < min_cost:
        min_cost = cost
        ans = cost
    s = S[0]
    S = S[1:] + s

print(ans)
