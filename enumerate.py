f = list(input())
for i, r in enumerate(f):
    if r == 'A':
        f[i] = '4'
        continue
    elif r == 'E':
        f[i] = '3'
        continue
    elif r == 'G':
        f[i] = '6'
        continue
    elif r == 'I':
        f[i] = '1'
        continue
    elif r == 'O':
        f[i] = '0'
        continue
    elif r == 'S':
        f[i] = '5'
        continue
    elif r == 'Z':
        f[i] = '2'
        continue

for k in f:
    print(k, end='')
