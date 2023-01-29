S = input()
T = input()

dp = [1 for _ in range(len(T)*2+2)]
dp[0] = 0
dp[-1] = 0
for i in range(len(T)):
    if (S[i] == T[i] or S[i] == "?" or T[i] == "?") and dp[i] == 0:
        dp[i+1] = 0
    
    if (S[-i-1] == T[-i-1] or S[-i-1] == "?" or T[i-1] == "?") and dp[-i-1] == 0:
        dp[-i-2] = 0

# print(dp)

for i in range(len(T)+1):
    front = dp[i]
    back = dp[len(T)+1+i]
    # print(i, len(T)+1+i)
    # print(front, back)
    if front == 0 and back == 0:
        print("Yes")
    else:
        print("No")
