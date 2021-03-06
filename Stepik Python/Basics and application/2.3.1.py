class multifilter():
    def judge_half(pos,neg):
        return True if pos >= neg else False

    def judge_any(pos, neg):
        return True if pos >= 1 else False

    def judge_all(pos,neg):
        return True if neg == 0 else False

    def __init__(self, itarable, *funcs, judge = judge_any):
        self.itarable = itarable
        self.funcs = funcs
        self.jude = judge

    def __iter__(self):
        for _ in self.itarable:
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(_):
                    pos += 1
                else:
                    neg += 1
            if self.jude(pos, neg):
                yield _


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]