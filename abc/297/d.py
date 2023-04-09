a, b = map(int, input().split())
count = 0
while a != b:
    if a > b:
        c = a // b
        amari = a % b
        a = amari
    else:
        c = b // a
        amari = b % a
        b = amari
    count += c
    if amari == 0:
        count -= 1
        break
print(count)