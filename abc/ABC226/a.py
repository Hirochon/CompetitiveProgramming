from decimal import Decimal

X = Decimal(input())

print(X.quantize(Decimal('0'), rounding="ROUND_HALF_UP"))