"""
Вам даны 2 координаты 2 клеток на шахматном поле. Нужно ответить на вопрос, можно ли попасть из одной клетки в другую
за не более чем 2 хода конем. В случае, если попасть возможно, надо вывести количество ходов,
 за которое это можно сделать. Если попасть невозможно, следует вернуть -1.

Формат входных данных
На вход подаются числа от 1 до 8 в 4 строках. Первые 2 строки задают координаты начальной клетки, вторые 2 -- координаты
 конечной клетки.

Формат выходных данных
Одно число — количество ходов, за которые можно попасть из из одной клетки во вторую. Если невозможно -- вывести -1.
"""

x1, y1, x2, y2 = [int(input()) for i in range(4)]

flag = True
if not (x1 == x2 and y1 == y2):
    for i in range(1, 9):
        for j in range(1, 9):
            if flag and (abs(x1-i) == 2 and abs(y1-j) == 1 or abs(x1-i) == 1 and abs(y1-j) == 2):
                if i == x2 and j == y2:
                    print(1)
                    flag = False
                    break
                elif abs(x2 - i) == 2 and abs(y2 - j) == 1 or abs(x2 - i) == 1 and abs(y2 - j) == 2:
                    print(2)
                    flag = False
                    break
            elif i == 8 and j == 8 and flag:
                print(-1)
else:
    print(0)

