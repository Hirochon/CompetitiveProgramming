from collections import defaultdict

N, X = map(int, input().split())

# numsList = []
numDictList = []
for i in range(N):
    # nums = set()
    dd = defaultdict(int)
    L, *A = map(int, input().split())
    for a in A:
        if X % a == 0:
            # if a not in nums:
            #     nums.add(a)
            dd[a] += 1
    # numsList.append(nums)
    numDictList.append(dict(dd))

print(numDictList)


# def tansaku(value, d):
#     rAns = 1
#     for k, v in numDictList[d].items():
#         if value % k != 0:
#             continue
#         if d < len(numDictList):
#             rAns += tansaku(value/k, d+1) * v
#     return rAns

# tansaku(0,1,0)
