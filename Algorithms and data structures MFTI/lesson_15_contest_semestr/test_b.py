"""
Количество элементов, не равных максимальному
На вход вашей программе подается последовательность целых чисел, заканчивающаяся нулем. Необходимо найти количество элементов этой последовательности, не равных максимальному значению в ней. Длина последовательности не превосходит 10 6 . Сами числа по модулю не превосходят 1000. Гарантируется, что последовательность содержит хотя бы один элемент.

Формат входных данных
На вход подается последовательность целых чисел. Каждое число подается с новой строки. Последовательность оканчивается нулем.

Формат выходных данных
Одно число — количество элементов последовательности, не равных максимальному.
>>> main(['1', '0'])
0
>>> main(['1', '2', '3', '4', '5', '0'])
4
>>> main(['1', '2', '3', '4', '4', '0'])
3
"""

def main(test = None):
    counter = 0
    tmp = test or int(input())
    data_input = []
    while tmp != 0 and type(tmp) != list:
        data_input.append(tmp)
        tmp = int(input())
    data_input = test[:-1] or data_input
    max_elemen = max(data_input)
    for i in data_input:
        if i != max_elemen:
            counter += 1
    return counter

if __name__ == '__main__':
    main()