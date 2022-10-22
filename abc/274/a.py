from decimal import Decimal, ROUND_HALF_UP

A, B = map(int, input().split())
c = str(float(B) / float(A))
print(Decimal(c).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
