"""
Напечатайте входную последовательность натуральных чисел, отсортировав ее по возрастанию сначала единиц, потом десятков,
потом сотен и тп.
Входные данные
Целое число 0 < N ≤ 1000. Затем N натуральных чисел, не превышающих 30000, через пробел.
Выходные данные
Числа по возрастанию единиц, при равных единиц - по возрастанию десятков, при равных единицах и десятков -
по возрастанию сотен и тп.
"""
size = int(input())
data_input = input().split()
data_list = [None]*size
revers_data = [None]*size
if 0 < size <= 1000 and size == len(data_input):
    for i in range(size):
        data_list[i] = int(data_input[i]) if int(data_input[i]) < 30000 else None
    if not(None in data_list):
        for i in range(size):
            revers_data[i] = data_input[i][::-1]
        revers_data.sort()
        for i in range(size):
            revers_data[i] = revers_data[i][::-1]
        print(*revers_data, end=' ')

    else:
        print(0)
