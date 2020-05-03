N, M = map(int, input().split())
H = list(map(int, input().split()))
ans_list = [1 for x in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    if H[A - 1] == H[B - 1]:
        ans_list[A - 1] = 0
        ans_list[B - 1] = 0
    elif H[A - 1] > H[B - 1]:
        ans_list[B - 1] = 0
    else:
        ans_list[A - 1] = 0
print(ans_list.count(1))
