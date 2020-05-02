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
print(c_list)

# これは…いつ使うんだろw
def dropwhile():
    print(list(itertools.dropwhile(lambda x: x < 9, c_list)))


# count()
# cycle()
# repeat()
# accumulate()
# compress()
# dropwhile()
