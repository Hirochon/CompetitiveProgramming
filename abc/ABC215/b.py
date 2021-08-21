N = int(input())

i = 0
while True:
    if pow(2, i) > N:
        ans = i - 1
        break
    i += 1
print(ans)