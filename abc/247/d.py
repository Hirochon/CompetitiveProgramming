Q = int(input())

q1 = []
q2 = []

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q1.append((query[1], query[2]))
    elif query[0] == 2:
        q2.append(query[1])

state = {"i": 0, "x": q1[0][0], "c": q1[0][1]}
for q2_v in q2:
    # print("q2_v", q2_v)
    mokuhyo = q2_v
    output = 0
    while mokuhyo > 0:
        if state["c"] < mokuhyo:
            output += state["c"] * state["x"]
            mokuhyo -= state["c"]
            state["i"] += 1
            state["c"] = q1[state["i"]][1]
            state["x"] = q1[state["i"]][0]
        else:
            output += mokuhyo * state["x"]
            state["c"] -= mokuhyo
            mokuhyo = 0
    print(output)
