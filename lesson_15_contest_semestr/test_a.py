"""
Больше-меньше
Вам дано выражение вида "a x b", где a и b - натуральные числа, а x - знак сравнения, '<' или '>'. Истинно ли данное выражение?

Формат входных данных
В первой строке число a, во второй знак сравнения, в третьей - число b. Оба числа - натуральные.

Формат выходных данных
Если выражение истинно, выведите YES, иначе NO
>>> main(['1','<','2'])
YES
>>> main(['10','>','100'])
NO
"""
def main(test = None):
    data_input = test or [input() for i in range(3)]
    data = []
    for i in data_input:
        if i in '<>':
            comparison_char = i
        else:
            data.append(int(i))
    if comparison_char == '>':
        if data[0] > data[1]:
            print('YES')
        else:
            print('NO')
    elif comparison_char == '<':
        if data[0] < data[1]:
            print('YES')
        else:
            print('NO')
if __name__ == '__main__':
    main()