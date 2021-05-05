"""
Задача I: Матпомощь
Студентов надо построить в шеренгу от самого легкого до самого тяжелого. Кто мало весит - тем выдать матпомощь..
При одинаковом весе сначала идет студент с большим ростом (тощий).

Формат входных данных
Целое число N, 0 < N < 100, - количество студентов. Затем N пар чисел (float) через пробел - рост в метрах и вес в
килограммах одного студента.

Формат результата
Рост и вес (печатать рост с точностью до сантиметров, а вес - до граммов) по одному студенту на строку от первого
 студента в шеренге к последнему
"""
def sort_input_data(data:list):
    """
    Функция должна отсортировать массив по второму вложенному элементу ели вторые  равны то учитывать вотой в реверсном
    возрастании


    :return:
    """
    for top in range(1, number):
        k = top
        while k > 0:
            if data[k-1][1] > data[k][1]:
                data[k], data[k-1] = data[k-1], data[k]
            if data[k-1][1] == data[k][1] and data[k-1][0] < data[k][0]:
                data[k], data[k-1] = data[k-1], data[k]
            k -= 1
    return data

number = int(input())
data_input = []*number
for i in range(number):
    data_input.append(list(map(float, input().split())))
for i in range(number):
    data_input[i][0] = round(data_input[i][0], 2)
    data_input[i][1] = round(data_input[i][1], 3)

data_result = sort_input_data(data_input)
for i in range(number):
    print(format(data_result[i][0], '.2f'), end=' ')
    #print(f'{data_result[i][1]:.3f}')  Выыод через F функцию не проходил тесты. Различия в версиях Python
    print(format(data_result[i][1], '.3f'))
