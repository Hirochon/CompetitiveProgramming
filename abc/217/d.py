import bisect, array

def main():
    L, Q = map(int, input().split())
    ans = array.array("i", [0, L])
    query =  [tuple(map(int, input().split())) for _ in range(Q)]
    for c, x in query:
        if c == 1:
            bisect.insort_left(ans, x)
        if c == 2:
            index = bisect.bisect(ans, x)
            print(ans[index] - ans[index-1])

main()