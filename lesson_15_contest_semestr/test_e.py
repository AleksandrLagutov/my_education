"""
Дан список целых чисел. Отсортировать его так, чтобы сначала шли чётные по возрастанию, потом — нечётные во возрастанию.

Формат входных данных
Одна строка — список чисел через пробел. Длина списка не превосходит 10000.

Формат выходных данных
Отсортированный список чисел через пробел.
"""
data_input = list(map(int, input().split()))
even_list = []
not_even_list = []

for i in data_input:
    if i % 2 == 0:
        even_list.append(i)
    else:
        not_even_list.append(i)
even_list.sort()
not_even_list.sort()
result = even_list + not_even_list
print(*result)
