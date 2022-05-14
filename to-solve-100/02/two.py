N = int(input())

def countYakusu(num):
    ansC = 0
    for i in range(1, num+1):
        if num % i == 0:
            ansC += 1
    return ansC

ans = 0

for i in range(1, N+1, 2):
    if countYakusu(i) == 8:
        ans += 1

print(ans)