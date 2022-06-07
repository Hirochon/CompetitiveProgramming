## https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e
from collections import deque

w, h = map(int, input().split())
WH = []
for i in range(h):
    W = input().split()
    WH.append(W)

past = set()
ans = 0
queue = deque([(0,0,(-1,-1))])
while queue.__len__():
    x, y, (px, py) = queue.popleft()
