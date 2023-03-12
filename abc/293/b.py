N = int(input())
A = map(int, input().split())
call_list = [False for _ in range(N)]
for i, a in enumerate(A):
    if call_list[i]:
        continue
    call_list[a-1] = True
ans = []
for i, call in enumerate(call_list):
    if not call:
        ans.append(i+1)
print(len(ans))
print(*ans)