from collections import defaultdict

INF = float('inf')

class UnionFind:
    def __init__(self, n):
        self.n = n
        """
        各要素の親要素番号を格納するリスト
        要素が根(ルート)の場合は -(そのグループの要素数)を格納する
        """
        self.parents = [-1] * n
    
    def find(self, x):
        """
        要素xが所属するグループの根を返す。(経路圧縮が行われる)
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        """
        要素xが属するグループと要素yが属するグループと併合する
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        要素xが属するグループのサイズ(要素数を返す)
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        要素x,yが同じグループに属するかどうかを返す
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        要素xが属するグループに属する要素をリストで返す
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根の要素をリストで返す
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        グループの数を返す
        """
        return len(self.roots)

    def all_group_members(self):
        """
        {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        """
        print()での表示用
        ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        """
        return "¥n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


N, M, Q = map(int, input().split())

# for i in range(M):
#     a, b, c = map(int, input().split())

# for i in range(Q):
#     u, v, w = map(int, input().split())

edges = [] # (from, to, cost, edge_index)

for i in range(M + Q):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    edges.append((a, b, c, i))

# クラスカル法で最小全域木を求める

edges = sorted(edges, key=lambda x: x[2])
uf = UnionFind(N) # 頂点同士が繋がっているか調べる用

answers = [None] * Q

for e in edges:
    if not uf.same(e[0], e[1]):
        if e[3] >= M: # クエリの辺だった場合
            answers[e[3] - M] = True
        else:
            uf.unite(e[0], e[1])

for ans in answers:
    if ans:
        print("Yes")
    else:
        print("No")
