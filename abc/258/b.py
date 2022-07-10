from collections import deque

N = int(input())
A = []
max_num = 0
for i in range(N):
    aa = []
    a = input()
    for i in range(len(a)):
        aa.append(int(a[i]))
        max_num = max(max_num, int(a[i]))
    A.append(aa)

# print(A)
# print(max_num)
queue = deque([])

for i in range(N):
    for j in range(N):
        if max_num == A[i][j]:
            queue.append((i, j, [max_num], set([(i, j)])))
# print(queue)

answers = []

while queue:
    i, j, ans, past = queue.popleft()
    way_points = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    real_way_points = []
    max_way_num = 0
    for way_point in way_points:
        if way_point[0] < 0 or way_point[0] >= N or way_point[1] < 0 or way_point[1] >= N:
            continue
        if way_point in past:
            continue
        ## まずは行ける場所を探す
        real_way_points.append(way_point)
        max_way_num = max(max_way_num, A[way_point[0]][way_point[1]])
    if i == 0:
        if (N-1, j) not in past:
            real_way_points.append((N-1, j))
            max_way_num = max(max_way_num, A[N-1][j])
    if j == 0:
        if (i, N-1) not in past:
            real_way_points.append((i, N-1))
            max_way_num = max(max_way_num, A[i][N-1])
    if i == N-1:
        if (0, j) not in past:
            real_way_points.append((0, j))
            max_way_num = max(max_way_num, A[0][j])
    if j == N-1:
        if (i, 0) not in past:
            real_way_points.append((i, 0))
            max_way_num = max(max_way_num, A[i][0])
    if i == 0 and j > 0:
        if (N-1, j-1) not in past:
            real_way_points.append((N-1, j-1))
            max_way_num = max(max_way_num, A[N-1][j-1])
    if i == N-1 and j > 0:
        if (0, j-1) not in past:
            real_way_points.append((0, j-1))
            max_way_num = max(max_way_num, A[0][j-1])
    if i > 0 and j == 0:
        if (i-1, N-1) not in past:
            real_way_points.append((i-1, N-1))
            max_way_num = max(max_way_num, A[i-1][N-1])
    if i > 0 and j == N-1:
        if (i-1, 0) not in past:
            real_way_points.append((i-1, 0))
            max_way_num = max(max_way_num, A[i-1][0])
    if i == 0 and j < N-1:
        if (N-1, j+1) not in past:
            real_way_points.append((N-1, j+1))
            max_way_num = max(max_way_num, A[N-1][j+1])
    if i == N-1 and j < N-1:
        if (0, j+1) not in past:
            real_way_points.append((0, j+1))
            max_way_num = max(max_way_num, A[0][j+1])
    if i < N-1 and j == 0:
        if (i+1, N-1) not in past:
            real_way_points.append((i+1, N-1))
            max_way_num = max(max_way_num, A[i+1][N-1])
    if i < N-1 and j == N-1:
        if (i+1, 0) not in past:
            real_way_points.append((i+1, 0))
            max_way_num = max(max_way_num, A[i+1][0])

    # print(real_way_points)
    # print(max_way_num)

    for real_way_point in real_way_points:
        if max_way_num == A[real_way_point[0]][real_way_point[1]]:
            if len(ans) == N-1:
                copy_ans = ans.copy()
                copy_ans.append(max_way_num)
                answers.append(copy_ans)
                break
            if len(ans) < N:
                copy_ans = ans.copy()
                copy_ans.append(max_way_num)
                copy_past = past.copy()
                copy_past.add(real_way_point)
                # print("queue", real_way_point[0], real_way_point[1], copy_ans, copy_past)
                queue.append((real_way_point[0], real_way_point[1], copy_ans, copy_past))

num_ans = []
for i in range(N):
    sans = ""
    for ww in answers[i]:
        sans += str(ww)
    num_ans.append(int(sans))

print(max(num_ans))
