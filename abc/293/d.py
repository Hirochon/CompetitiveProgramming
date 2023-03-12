N, M = map(int, input().split())
X = 0
Y = 0
## トポロジカルソートで解く
# 1. 入次数が0の頂点をキューに入れる
# 2. キューから頂点を取り出し、その頂点から出る辺を削除する
# 3. 2で削除した辺によって入次数が0になった頂点をキューに入れる
# 4. 2-3をキューが空になるまで繰り返す
# 5. キューが空になったら、すべての頂点を訪問できている
# 6. 5で訪問できていない頂点があれば、そのグラフは閉路を持つ
# 7. 5で訪問できている頂点があれば、その順序がトポロジカルソートの結果
inNum = {str(i+1): 0 for i in range(N)}
relation_map = {}
for i in range(M):
    a, b, c, d = input().split()
    inNum[a] += 1
    inNum[c] += 1
    if b == "R":

for key, value in relation_map.items():
    inNum[key] -= 1
    inNum[value] -= 1
    if 
Y_list = []
for key in Y_list:
    del inNum[key]
