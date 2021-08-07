import math

N = int(input()) * 2

sqrt_N = math.sqrt(N)

N_min = math.floor(sqrt_N)
N_max = N_min + 1

if N_min * N_max >= N:
    print(N_min)
elif (N_min + 1) * (N_max + 1) >= N:
    print(N_min + 1)
