N = int(input())
A = list(map(int, input().split()))

kisu = []
gusu = []

A.sort()
# print(A)

for a in A[::-1]:
    # print(a)
    if a % 2 == 0 and len(gusu) != 2:
        gusu.append(a)
    elif a % 2 == 1 and len(kisu) != 2:
        kisu.append(a)
    if len(gusu) == 2 and len(kisu) == 2:
        break
if len(gusu) != 2 and len(kisu) != 2:
    print(-1)
    exit()
ki = sum(kisu)
gu = sum(gusu)
print(max(ki, gu))
