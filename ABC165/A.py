K = int(input())
flag = 0
A, B = map(int, input().split())
for i in range(A, B + 1):
    if i % K == 0:
        print("OK")
        flag += 1
        break
if flag == 0:
    print("NG")
