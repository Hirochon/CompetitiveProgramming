N, M = map(int, input().split())

kara_A = [[] for _ in range(2001)]
kara_B = [[] for _ in range(2001)]

AA = [0 for _ in range(2001)]
BB = [0 for _ in range(2001)]

A_set = set()

for i in range(M):
    A, B = map(int, input().split())
    A_set.add(A)
    kara_A[A].append(B)
    kara_B[B].append(A)
    AA[A] = B
    BB[B] = A

for a in sorted(A_set):
    if kara_B[a]:
        for A in kara_B[a]:
            if A != AA[a]:
                kara_A[A].append(AA[a])

ans = 0

for A in kara_A:
    A_len = len(A)
    if A_len > 0:
        ans += A_len
        print(A)

print(ans + N)
