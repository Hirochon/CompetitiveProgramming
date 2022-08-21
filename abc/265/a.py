X, Y, N = map(int, input().split())

def sanko():
    if X*3 > Y:
        return Y
    else:
        return X*3
sanko_price = sanko()

set_price = (N // 3) * sanko_price
amari_price = (N % 3) * X
print(set_price + amari_price)
