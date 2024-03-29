import sys
sys.setrecursionlimit(10**6)

N = int(input())
past = {}

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        if n in past.keys():
            return past[n]
        past[n] = fib(n-1) + fib(n-2)
        return past[n]

print(fib(N))
