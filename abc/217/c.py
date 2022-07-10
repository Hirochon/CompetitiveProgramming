N = int(input())

p = map(int, input().split())

q = {v : i+1 for i, v in enumerate(p)}

for i in range(N):
    print(q[i+1], end=" ")
print()