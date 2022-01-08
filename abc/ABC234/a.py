t = int(input())

def f(t_h):
    return t_h**2 + 2*t_h + 3

print(f(f(f(t)+t)+f(f(t))))
