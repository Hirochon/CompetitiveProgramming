n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

def binarySearch(x: int) -> bool:
    min = 0
    max = n - 1
    while min - max != 1:
        # print("min", min)
        # print("max", max)
        middle = (min + max) // 2
        # print("middle", middle)
        if S[middle] == x:
            return True
        elif S[middle] < x:
            min = middle+1
        else:
            max = middle-1
        # print("after min", min)
        # print("after max", max)
    return False

ans = 0

for t in T:
    # print("====")
    if binarySearch(t):
        ans += 1
    # print("====")
print(ans)
