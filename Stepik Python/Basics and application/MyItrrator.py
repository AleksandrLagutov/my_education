
class MyList:
    def __init__(self, list, func):
        self.list =list
        self.func = func

    def judge(self,num):
        return "element =" + str(num)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.list):
            self.index += 1
            self.resalt_of_f2 = self.func(self.list[self.index -1])
            return self.resalt_of_f2
        raise StopIteration

def f2(n):
    return n / 2


l = MyList([1,2,3,4,5,2], f2)
print(type(l))

for i in l:
    print(i)
print('2sdf')
print(list(l))