S = []
for i in range(10):
    s = input()
    S.append(s)
place = []
first_check = False
second_check = False
third_column_num = -1
second_column_num = -1
finish_check = False
for i in range(10):
    for j in range(10):
        if S[i][j] == '#':
            if first_check == False:
                place.append((i, j))
                first_check = True
                second_column_num = i
                third_column_num = j
        if first_check and S[i][j] == '.':
            if second_check == False:
                place.append((i, j-1))
                second_check = True
        if first_check and second_check and j == third_column_num and S[i][j] == '.':
            place.append((i-1, j))
            finish_check = True
        if finish_check:
            break
    if first_check and second_check == False:
        place.append((second_column_num, 9))
        second_check = True
    if finish_check:
        break
    # print(place)
if finish_check == False:
    place.append((9, third_column_num))
print(place[0][0] + 1, place[2][0] + 1)
print(place[0][1] + 1, place[1][1] + 1)