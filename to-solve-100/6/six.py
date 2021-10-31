N = int(input())

S = input()
count = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            pin = str(i) + str(j) + str(k)
            sfind1 = S.find(pin[0])
            if sfind1 == -1:
                continue
            S2 = S[sfind1+1:]
            sfind2 = S2.find(pin[1])
            if sfind2 == -1:
                continue
            S3 = S2[sfind2+1:]
            sfind3 = S3.find(pin[2])
            if sfind3 == -1:
                continue
            count += 1
            # print(S[sfind1] + S2[sfind2] + S3[sfind3])
print(count)