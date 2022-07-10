h1, h2, h3, w1, w2, w3 = map(int, input().split())

H = [h1, h2, h3]
H1 = set()
H2 = set()
H3 = set()

for i in range(3):
    for a1 in range(1, H[i]+1):
        if a1 >= w1:
            break
        for a2 in range(1, H[i]+1):
            if a2 >= w2:
                break
            if a1 >= H[i] or a2 >= H[i]:
                break
            if a1 + a2 >= H[i]:
                break
            if i == 0:
                H1.add((a1, a2, H[i] - a1 - a2))
            elif i == 1:
                H2.add((a1, a2, H[i] - a1 - a2))
            elif i == 2:
                H3.add((a1, a2, H[i] - a1 - a2))

ans = 0

for hh11 in H1:
    if hh11[0] >= w1 or hh11[1] >= w2 or hh11[2] >= w3:
        continue
    for hh22 in H2:
        if hh22[0] >= w1 or hh22[1] >= w2 or hh22[2] >= w3:
            continue
        if hh22[0] + hh11[0] >= w1 or hh22[1] + hh11[1] >= w2 or hh22[2] + hh11[2] >= w3:
            continue
        for hh33 in H3:
            # print(hh11, hh22, hh33)
            ww11 = hh11[0] + hh22[0] + hh33[0]
            ww22 = hh11[1] + hh22[1] + hh33[1]
            ww33 = hh11[2] + hh22[2] + hh33[2]
            if ww11 == w1 and ww22 == w2 and ww33 == w3:
                ans += 1
print(ans)