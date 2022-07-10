N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

setA = set(A)
ans1 = 0
ans2 = 0

for i in range(len(B)):
    if B[i] in setA:
        ans2 += 1
        if A[i] == B[i]:
            ans1 += 1
            ans2 -= 1

print(ans1)
print(ans2)
