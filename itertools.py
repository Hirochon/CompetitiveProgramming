# 参考URL https://docs.python.org/ja/3/library/itertools.html

import itertools


# itertools.count(rangeの上限がないバージョン) 無限ループに陥らないように注意
def count():
    for i in itertools.count(10):
        if i > 40:
            break
        print(i, end=' ')
    print()


# itertools.cycle(無限に値をループする) こちらも無限ループに陥らないように注意
def cycle():
    count = 0
    for i in itertools.cycle([1, 2, 3, 4, 5]):
        if count >= 10:
            break
        print(i, end=' ')
        count += 1
    print()


# itertools.repeat(無限に繰り返す)
def repeat():
    """
    itertools.repeat(element, [,n]) -> iterator

    elementを無限回またn回まで重複する
    nを与えないと無限イテレータになる

    eg: repeat(10, 3) --> 10 10 10
    """

    print(list(itertools.repeat("a", 5)))  # -> ['a', 'a', 'a', 'a', 'a']
    for i in itertools.repeat(1, 5):
        print(i, end=' ')   # -> 1 1 1 1 1
    print()


# 与えられた配列をどんどん演算(デフォルトは加算)していく
a_list = [1, 3, 5, 7, 9]
b_list = [1, 2, 3, 4, 5]
def accumulate():
    print(list(itertools.accumulate(a_list)))   # -> [1, 4, 9, 16, 25]
    print(list(itertools.accumulate(b_list, lambda x, y: x * y)))   # -> [1, 2, 6, 24, 120]


def compress():
    """
    itertools.compress(iterable, selectors) -> iterator

    selectorsの評価値が真となるようなiterableの要素を取り出すイテレータを作る
    ポジション的なfilterに相当する

    eg:  compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    """
    print(list(itertools.compress([1, 2, 3, 4, 5, 6], [1, 0, 1, 1, 0])))   # -> [1, 3, 4]

import random

c_list = [x for x in range(10)]
random.shuffle(c_list)
# print(c_list)

# これは…いつ使うんだろw
def dropwhile():
    print(list(itertools.dropwhile(lambda x: x < 9, c_list)))


# itertools.product 全パターン出力奴
def product():
    """
    itertools.product(iterable1, ..., [,repeat=1]) -> iterator
    入力されたiterablesのデカルト積/直積を返すイテレータを作る
    repeatを指定すると、iterablesの数を倍にすることができる
    product(A, repeat=4)はproduct(A, A, A, A)と同じとなる

    eg: product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
    """
    print(list(itertools.product("AB", repeat=3)))
    # [('A', 'A', 'A'),
    #  ('A', 'A', 'B'),
    #  ('A', 'B', 'A'),
    #  ('A', 'B', 'B'),
    #  ('B', 'A', 'A'),
    #  ('B', 'A', 'B'),
    #  ('B', 'B', 'A'),
    #  ('B', 'B', 'B')]

    print(list(itertools.product("ABC", "123")))
    # [('A', '1'),
    #  ('A', '2'),
    #  ('A', '3'),
    #  ('B', '1'),
    #  ('B', '2'),
    #  ('B', '3'),
    #  ('C', '1'),
    #  ('C', '2'),
    #  ('C', '3')]


# itertools.permutations
def permutations():
    """
    itertools.permutations(iterable, [,r]) -> iterator

    iterableから順列を返すイテレータを作る, rは順列の長さを指定できる
    rを指定しないと全順列となる

    eg: permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    """
    list(itertools.permutations("ABC"))
    # [('A', 'B', 'C'),
    #  ('A', 'C', 'B'),
    #  ('B', 'A', 'C'),
    #  ('B', 'C', 'A'),
    #  ('C', 'A', 'B'),
    #  ('C', 'B', 'A')]

    list(map(lambda x: int(x[0]) + int(x[1]), itertools.permutations("12345", 2)))
    # ->[3, 4, 5, 6, 3, 5, 6, 7, 4, 5, 7, 8, 5, 6, 7, 9, 6, 7, 8, 9]


# itertools.combinations
def combinations():
    """
    itertools.combinations(iterable, r) -> iterator

    iterableから組み合わせを返すイテレータを作る、permutationsと違って、rの指定は必須

    eg: combinations('ABCD', 2) --> AB AC AD BC BD CD
    """
    list(itertools.combinations("ABCDE", 2))
    # [('A', 'B'),
    #  ('A', 'C'),
    #  ('A', 'D'),
    #  ('A', 'E'),
    #  ('B', 'C'),
    #  ('B', 'D'),
    #  ('B', 'E'),
    #  ('C', 'D'),
    #  ('C', 'E'),
    #  ('D', 'E')]


# itertools.combinations_with_replacement
def combinations_with_replacement():
    """
    itertools.combinations_with_replacement(iterable, r) -> iterator

    combinationsと似ているが、違うところとしては組み合わせのとき重複ありを考える

    eg: combinations_with_replacement('ABCD', 2) --> AA AB AC AD BB BC BD CC CD DD
    """
    list(itertools.combinations_with_replacement("ABCDE", 2))
    # [('A', 'A'),
    #  ('A', 'B'),
    #  ('A', 'C'),
    #  ('A', 'D'),
    #  ('A', 'E'),
    #  ('B', 'B'),
    #  ('B', 'C'),
    #  ('B', 'D'),
    #  ('B', 'E'),
    #  ('C', 'C'),
    #  ('C', 'D'),
    #  ('C', 'E'),
    #  ('D', 'D'),
    #  ('D', 'E'),
    #  ('E', 'E')]


# count()
# cycle()
# repeat()
# accumulate()
# compress()
# dropwhile()
product()
permutations()
combinations()
combinations_with_replacement()
