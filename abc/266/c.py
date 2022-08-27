import math

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

BA1 = Bx - Ax
BA2 = By - Ay
BA = math.sqrt(BA1**2 + BA2**2)
DA1 = Dx - Ax
DA2 = Dy - Ay
DA = math.sqrt(DA1**2 + DA2**2)
ATheta = math.acos((BA1*DA1 + BA2*DA2) / (BA*DA)) * 180 / math.pi
print((BA1*DA1 + BA2*DA2) / (BA*DA))
print(ATheta)

AB1 = Ax - Bx
AB2 = Ay - By
AB = math.sqrt(AB1**2 + AB2**2)
CB1 = Cx - Bx
CB2 = Cy - By
CB = math.sqrt(CB1**2 + CB2**2)
BTheta = math.acos((AB1*CB1 + AB2*CB2) / (AB*CB)) * 180 / math.pi
print((AB1*CB1 + AB2*CB2) / (AB*CB))
print(BTheta)

BC1 = Bx - Cx
BC2 = By - Cy
BC = math.sqrt(BC1**2 + BC2**2)
DC1 = Dx - Cx
DC2 = Dy - Cy
DC = math.sqrt(DC1**2 + DC2**2)
CTheta = math.acos((BC1*DC1 + BC2*DC2) / (BC*DC)) * 180 / math.pi
print((BC1*DC1 + BC2*DC2) / (BC*DC))
print(CTheta)

AD1 = Ax - Dx
AD2 = Ay - Dy
AD = math.sqrt(AD1**2 + AD2**2)
CD1 = Cx - Dx
CD2 = Cy - Dy
CD = math.sqrt(CD1**2 + CD2**2)
DTheta = math.acos((AD1*CD1 + AD2*CD2) / (AD*CD)) * 180 / math.pi
print((AD1*CD1 + AD2*CD2) / (AD*CD))
print(DTheta)
