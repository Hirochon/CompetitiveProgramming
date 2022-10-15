X, K = map(int, input().split())

X_str_zeropa = str(X).zfill(K)
for k in range(1, K+1):
    # print(X_str_zeropa[-k])
    # print(X_str_zeropa)
    if X_str_zeropa[:-k] != '' and int(X_str_zeropa[:-k]) == 0:
        X_str_zeropa = "0"
        break
    if int(X_str_zeropa[-k]) < 5:
        X_str_zeropa = (X_str_zeropa[:-k] + "0" * k).zfill(K)
        continue
    if X_str_zeropa[:-k] == "":
        kuriage = 0
    else:
        kuriage = int(X_str_zeropa[:-k])
    X_str_zeropa = (str(kuriage + 1) + "0" * k).zfill(K)
print(int(X_str_zeropa))