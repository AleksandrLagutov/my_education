"""
Напечатайте входную строку, отсортировав ее по возрастанию ASCII кода символов.

Входные данные

Строка, заканчивающаяся точкой, длиной не более 1000 символов. Точку сортировать не нужно. Все, что находится после первой точки - игнорировать.

Выходные данные

Отсортированная строка с точкой на конце.
"""
data_input = input()
end_str = data_input.find('.')
data = data_input[0:end_str]


def sort_list(A):
    """
    Функиия принимает строку, переводит строку в лист, сортирует лис. Отсартированный массив возвращает в строку
    :param A: str
    :return: str
    """
    list_a = []
    new_a = ''
    for i in range(len(A)):
        list_a.append(A[i])

    for top in range(len(list_a)):
        k = top
        while k > 0 and list_a[k-1] > list_a[k]:
            list_a[k], list_a[k-1] = list_a[k-1], list_a[k]
            k -= 1
    for i in range(len(A)):
        new_a += list_a[i]
    new_a += '.'
    return new_a


print(sort_list(data))
