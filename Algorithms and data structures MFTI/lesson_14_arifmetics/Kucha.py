"""
Реализация структуры данныйх Куча
потомки  i = 2i + 1; i = 2i + 2
рпедок i = (i-1)//2
"""

class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        """
        Добаление элементов в кучу
        сам жлемент добавляем в конец списка и восстанавливаем свойство кучи
        :param x:
        :return:
        """
        self.values.append(x)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def extract_min(self):
        """
        возвращает верзний элемент кучи
        что бы восстановить кучу возьмем последний элемент и постави его на верх
        и от него будем воссанавливать кучу
        :return:
        """
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        return tmp

    def sift_down(self, i):
        """
        Идем по куче вниз и восстанваливаем свойство кучи
        """
        while 2 * i + 1 < self.size:
            j = i
            if self.values[2*i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:   # Проверяем есть ли правый потомок
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j



