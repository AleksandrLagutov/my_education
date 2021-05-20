
class MyList:
    def __init__(self, list):
        self.list =list

    def __iter__(self):
        self.index = 0
        resalt = []
        for x in self.list:
            if x % 2 == 0:
                yield x



def f2(n):
    return n / 2


l = MyList([1,2,3,4,5,2])
print(type(l))

print(list(l))