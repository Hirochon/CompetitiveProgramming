from collections import defaultdict
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = defaultdict(int)
for i in range(M):
    x, y = map(int, input().split())
    XY[x] = y
# print(T)
for i in range(N-1):
    T -= A[i]
    if T <= 0:
        print("No")
        exit()
    T += XY[i+2]
    # print(T)
print("Yes")
