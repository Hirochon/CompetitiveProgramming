N = int(input())
amari = N % 4
kai = N // 4

for i in range(4):
    if (amari + i) % 4 == 2:
        print(N+i)
