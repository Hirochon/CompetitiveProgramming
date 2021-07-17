from collections import deque

H, W, C = map(int, input().split())

A = [[v for v in map(int, input().split())] for _ in range(H)]

req_min_pair = 1e10
min_pair = deque(sorted([A[0][0], A[0][1]]))

if A[0][0] < A[0][1]:
    min_sum = deque([[0,0], [0,1]])
else:
    min_sum = deque([[0,1], [0, 0]])

value = A[0][0] + A[0][1] + C * 1

for h in range(H):
    for w in range(W):
        if w < W - 1:
            w_v1 = A[h][w]
            w_v2 = A[h][w+1]
            if req_min_pair > w_v1 + w_v2:
                req_min_pair = w_v1 + w_v2
                req_min_dq = [[h, w], [h, w+1]]
        
        if h < H-1:
            h_v1 = A[h][w]
            h_v2 = A[h+1][w]
            if req_min_pair > h_v1 + h_v2:
                req_min_pair = h_v1 + h_v2
                req_min_dq = [[h, w], [h+1, w]]
            
        if w > 1 or h > 1:
            if min_pair[1] > A[h][w]:
                v = min_pair[0] + A[h][w] + C * (abs(min_sum[0][0] - h) + abs(min_sum[0][1] - w))
                if v < value:
                    value = v
                    min_pair.pop()
                    min_sum.pop()
                    if min_pair[0] > A[h][w]:
                        min_pair.appendleft(A[h][w])
                        min_sum.appendleft([h, w])
                    else:
                        min_pair.append(A[h][w])
                        min_sum.append([h, w])

value1 = req_min_pair + C * (abs(req_min_dq[1][0] - req_min_dq[1][1]) + abs(req_min_dq[0][0] - req_min_dq[0][1]))


if value > value1:
    print(value1)
else:
    print(value)
