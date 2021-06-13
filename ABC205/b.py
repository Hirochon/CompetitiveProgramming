N = int(input())

A = map(int, input().split())

sorted_A = sorted(A)

for i in range(1, N + 1):
    if i != sorted_A[i - 1]:
        print("No")
        exit()

print("Yes")
