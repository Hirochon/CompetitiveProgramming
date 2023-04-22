N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

win_flag = T
not_t_flag = True
for c in C:
    if c == win_flag:
        not_t_flag = False
        break
if not_t_flag:
    win_flag = C[0]

ans = -1
max_v = -1
for i, r in enumerate(R):
    if C[i] == win_flag:
        if r > max_v:
            max_v = r
            ans = i + 1
print(ans)
