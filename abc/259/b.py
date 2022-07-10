import math
a, b, d = map(int, input().split())

a_dash = round(a * math.cos(d/180*math.pi), 8) - round(b * math.sin(d/180*math.pi), 8)
b_dash = round(a * math.sin(d/180*math.pi), 8) + round(b * math.cos(d/180*math.pi), 8)

print(a_dash, b_dash)
