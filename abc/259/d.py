N = int(input())
sx, sy, tx, ty = map(int, input().split())

start_list = []
end_list = set([])

for i in range(N):
    x, y, r = map(int, input().split())
    if (x - sx)**2 + (y - sy)**2 == r**2:
        start_list.append((x, y, r))
    if (x - tx)**2 + (y - ty)**2 == r**2:
        end_list.add((x, y, r))

while start_list:
    x, y, r = start_list.pop()
    
