from collections import deque

a, N = map(int, input().split())

dn = deque([(N, 0)])
pastN = set()

while len(dn) != 0:
    n, i = dn.pop()
    # print(n, i)

    if n in pastN:
        continue
    pastN.add(n)
    if n > 10:
        strN = str(n)
        intN = int(strN[1:] + strN[0])
        dn.append((intN, i+1))
    if n % a == 0:
        ans = n // a
        if ans == 1:
            print(i+1)
            exit()
        dn.append((ans, i+1))
    # print(dn, pastN)
print(-1)