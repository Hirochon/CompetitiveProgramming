from collections import deque


A = deque([i + 1 for i in range(0, 5)])
B = A.copy()
C = A.copy()
D = A.copy()

E = ['Hello World']
print(E[0][::-1])
F = deque(E[0][::-1], 11)
G = F.copy()
print(F)
F.appendleft("!")
print(F)
G.append("/")
print(G)

# 標準出力
print("標準出力: " + str(A))

# rotateしてみる！
A.rotate()
print("rotate(): " + str(A))
B.rotate(-1)
print("rotate(-1): " + str(B))

# appendとappendleft
C.append(6)
print("append(6): " + str(C))
C.appendleft(0)
print("appendleft(0): " + str(C))

# extendとextendleft
D.extend([6, 7])
print("extend([6, 7]): " + str(D))
D.extendleft([0, -1])
print("extendleft([0, -1]): " + str(D))

# insert!
D.insert(3, 10)
print("insert(3, 10): " + str(D))
D.insert(-2, 20)
print("insert(-2, 20): " + str(D))
D.insert(-100, 30)
print("insert(-100, 30): " + str(D))

# キュー！
for i in range(1, 6):
    A.append(i)
    print(A.popleft(), end=' ')
print()
print(A)

# スタック！
for i in range(4, 9):
    A.append(i)
    print(A.pop(), end=' ')
print()
print(A)
