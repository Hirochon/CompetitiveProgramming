import math

N = int(input())

N_z = math.floor(N * 1.08)

if N_z < 206:
    print("Yay!")
elif N_z == 206:
    print("so-so")
else:
    print(":(")
