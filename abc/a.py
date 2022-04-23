A,B,C,D,E,F,X = map(int,input().split())

t_ans = X // (A+C) * B * A
t_amari = X % (A+C)
a_ans = X // (D+F) * E * D
a_amari = X % (D+F)

# print(t_ans, a_ans)

t_plus = min(t_amari, A)
t_ans += t_plus * B
a_plus = min(a_amari, D)
a_ans += a_plus * E

# print(t_ans, a_ans)

if t_ans > a_ans:
    print("Takahashi")
elif t_ans < a_ans:
    print("Aoki")
else:
    print("Draw")
