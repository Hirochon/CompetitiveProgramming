from itertools import product

N, K = map(int, input().split())

A = list(map(int, input().split()))

# print(a)
kijun = A[0]
ans = 10**12

for bvs in product(range(2), repeat=N):
    if not bvs[0]:
        continue
    inputValues = [A[i] for i in range(N) if bvs[i]]
    LengthIV = len(inputValues)
    if LengthIV < K:
        continue
    # print(inputValues)

    tmpAns = 0
    for i in range(1, LengthIV):
        tmp = inputValues[i-1] - inputValues[i]
        if tmp < 0:
            continue
        tmp += 1
        print(tmp)
        inputValues[i] += tmp
        tmpAns += tmp
        print(inputValues, tmpAns)
    ans = min(ans, tmpAns)

print(ans)
