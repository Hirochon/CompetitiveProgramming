def tes(R, C):
    # R, C = map(int, input().split())

    ans = ""
    if R <= C and R <= 8 and C <= 15-R+1:
        ans = "black" if R % 2 != 0 else "white"
    elif R <= C and R > 8 and 15-R+1 <= C:
        ans = "black" if R % 2 != 0 else "white"
    elif R > C and C <= 8 and R <= 15-C+1:
        ans = "black" if C % 2 != 0 else "white"
    elif R > C and C > 8 and 15-C+1 <= R:
        ans = "black" if C % 2 != 0 else "white"

    # print(ans)
    print(ans, end="")

if __name__ == "__main__":
    R, C = map(int, input().split())
    tes(R, C)
    print()

    for i in range(1, 16):
        for j in range(1, 16):
            tes(i, j)
            print(" ", end="")
        print()
