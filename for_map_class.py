class fizzbuzz:
    """fizzbuzz問題を大げさにクラス化して、
       高級関数mapが使いたいだけの自己満足奴"""

    # @staticmethod # インスタンス化しない時にこれつけるといける
    def fb_func(self, n):   # クラス内で関数呼びだしされたければ、selfつけるべし。
        """FizzBuzz判定装置"""

        if n % 2 == 0:
            if n % 3 == 0:
                return 'FizzBuzz'
            else:
                return 'Fizz'
        elif n % 3 == 0:
            return 'Buzz'
        return n

    def for_map(self, m=20):
        """map関数×for文が使いたかっただけ"""

        ans = []
        for fb in map(self.fb_func, range(m)):
            ans.append(fb)
        return ans


fb = fizzbuzz()
fb_list = fb.for_map()
for i in map(print, fb_list):
    pass
