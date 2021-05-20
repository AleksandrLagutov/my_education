class multiffilter():
    def jude_half(pos,neg):
        return True if pos >= neg else False
        pass

    def jude_any(k, b):
        return True if k >= 1 else False

    def jude_all(pos,neg):
        return True if neg == 0 else False
        pass

    def __init__(self, itarable, *funcs, jude = jude_any):
        self.itarable = itarable
        self.funcs = funcs
        self.jude = jude
        pass

    def __iter__(self):
        self.index = 0

        return self

    def __next__(self):

        print(self.index)
        pos = 0
        neg = 0
        if self.index < len(self.itarable):
            self.index += 1
            for _ in self.funcs:
                if _(self.itarable[self.index - 1]):
                    pos += 1
                else:
                    neg += 1
            if self.jude(pos, neg):
                print('ys')
                return self.itarable[self.index - 1]


        else:
            raise StopIteration
def f1(x):
    return x % 2 == 0
def f2(x):
    return x % 3 == 0

a = [i for i in range(20)]

print(list(multiffilter(a, f1, f2)))