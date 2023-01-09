T = int(input())
N = []
A = []
for i in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    N.append(n)
    A.append(a)

for a in A:
    count = 0
    for aa in a:
        if aa % 2 == 1:
            count += 1
    print(count)