Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())
ABCD = [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)]

def isP(p0x, p0y, p1x, p1y, p2x, p2y, px, py):
    Area = 0.5 *(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
    s = 1/(2*Area)*(p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py)
    t = 1/(2*Area)*(p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py)
    
    return (0 < s < 1) and (0 < t < 1) and (0<1-s-t<1)

for i in range(4):
    excludeP = [v for j, v in enumerate(ABCD) if j != i]
    P = ABCD[i]
    if isP(excludeP[0][0], excludeP[0][1], excludeP[1][0], excludeP[1][1], excludeP[2][0], excludeP[2][1], P[0], P[1]):
        print("No")
        exit()
print("Yes")
