from collections import defaultdict

M = int(input())

dd = defaultdict(set)

for i in range(M):
    u, v = map(int, input().split())
    dd[u].add(v)
    dd[v].add(u)

p = {v : i+1 for i, v in enumerate(map(int, input().split()))}

se = set(i for i in range(1, 10))
amari = (se - set(p.keys())).pop()
p[amari] = 0

def swap(a, b, pp):
    tmp = pp[a]
    pp[a] = pp[b]
    pp[b] = tmp
    return pp

n = amari
ans = 0

def judge(pp):
    for i in range(1, 9):
        if i != pp[i]:
            return False
    return True

def tansaku(n, pp, ans):
    for d in dd[n]:
        pp = swap(n, d, pp)
        n = d
        ans += 1
        if judge(pp):
            return ans
        ans = tansaku()

ans = tansaku(n, p, ans)
