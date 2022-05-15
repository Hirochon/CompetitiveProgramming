import sys
sys.setrecursionlimit(10**6)

m = int(input())
n = int(input())

mn = []
for i in range(n):
    mn.append(list(map(int, input().split())))

ans = 0
def dfs(current: tuple, value: int, past_set: set):
    # def dfs(current: tuple, value: int, past_set: set, ini: int):
    # if ini == 4:
    #     print(current, value, past_set)
    global ans
    value += 1
    next_past_set = past_set.copy()
    next_past_set.add(current)
    ans = max(ans, value)
    for (ii, jj) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new = (current[0] + ii, current[1] + jj)
        if new[0] >= 0 and new[0] < n and new[1] >= 0 and new[1] < m:
            if mn[new[0]][new[1]] == 1:
                if new not in next_past_set:
                    dfs(new, value, next_past_set)
                    # dfs(new, value, next_past_set, ini)

for i in range(n):
    for j in range(m):
        if mn[i][j] == 1:
            dfs((i, j), 0, set())
            # dfs((i, j), 0, set(), ini=i)
print(ans)