n=int(input())
s=[]
for i in range(n):
    s.append(input())

for i in range(n):
    for j in range(n):
        if i + 5 < n:
            cnt = 0
            for k in range(6):
                if s[i + k][j] == "#":
                    cnt += 1
                if cnt >= 4:
                    print("Yes")
                    exit()
        if j + 5 < n:
            cnt = 0
            for k in range(6):
                if s[i][j + k] == "#":
                    cnt += 1
                if cnt >= 4:
                    print("Yes")
                    exit()

        if i + 5 < n and j + 5 < n:
            cnt = 0
            for k in range(6):
                if s[i + k][j + k] == "#":
                    cnt += 1
                if cnt >= 4:
                    print("Yes")
                    exit()
        
        if i - 5 >= 0 and j + 5 < n:
            cnt = 0
            for k in range(6):
                if s[i - k][j + k] == "#":
                    cnt += 1
            if cnt >= 4:
                print("Yes")
                exit()
        
print("No")