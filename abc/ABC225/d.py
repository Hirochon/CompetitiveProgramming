import sys
sys.setrecursionlimit(100000)

N, Q = map(int, input().split())

dBack = dict()
dPrev = dict()

def prev(dic, q):
    if q in dic:
        s = prev(dic, dic[q])
        return s + " " + dic[q]
    return ""

def back(dic, q):
    if q in dic:
        k = back(dic, dic[q])
        return dic[q] + " " + k
    return ""

for i in range(Q):
    query = input().split()
    if query[0] == "1":
        dBack[query[1]] = query[2]
        dPrev[query[2]] = query[1]
    elif query[0] == "2":
        del dBack[query[1]]
        del dPrev[query[2]]
    else:
        # print("============")
        # print(dPrev)
        k = prev(dPrev, query[1])
        k += " " + query[1]
        k += " " + back(dBack, query[1])
        kl = k.split()
        print(len(kl), *kl)
        # print("============")

# print(dBack, dPrev)