n, q = map(int, input().split())
p = [-1] * (n+1)
r = [-1] * (n+1)

# print(p, r)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p[query[2]] = query[1]
        r[query[1]] = query[2]

    if query[0] == 2:
        p[query[2]] = -1
        r[query[1]] = -1
    
    if query[0] == 3:
        x = query[1]
        while p[x] != -1:
            x = p[x]
        res = []
        while r[x] != -1:
            res.append(x)
            x = r[x]
        res.append(x)
        res.insert(0, len(res))
        # print("=========")
        print(*res)
        # print("=========")
        