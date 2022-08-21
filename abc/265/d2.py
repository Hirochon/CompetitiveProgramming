N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
ruisekiwa = []
for i in range(N):
    if i == 0:
        ruisekiwa.append(A[i])
    else:
        ruisekiwa.append(ruisekiwa[i-1] + A[i])
print(ruisekiwa)
