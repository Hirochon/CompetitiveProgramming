N = int(input())
H = list(map(int, input().split()))
maxH = 0
for h in H:
    if maxH >= h:
        break
    maxH = h
print(maxH)