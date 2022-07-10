from itertools import product

def prime_factorize(n):
    a = set([1, n])
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a

N = int(input())
nList = sorted(list(prime_factorize(N)))
print(nList)

for n in product(nList, 3):
    print(n, n[1])
