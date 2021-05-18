class ExtendedStack(list):
    def sum(self):
        top1_1, top_2 = self.pop(), self.pop()
        self.append(top1_1 + top_2)
        # операция сложения

    def sub(self):
        top1_1, top_2 = self.pop(), self.pop()
        self.append(top1_1 - top_2)
        # операция вычитания

    def mul(self):
        top1_1, top_2 = self.pop(), self.pop()
        self.append(top1_1 * top_2)
        # операция умножения

    def div(self):
        top1_1, top_2 = self.pop(), self.pop()
        if top_2 != 0:
            self.append(top1_1 // top_2)
        # операция целочисленного деления
