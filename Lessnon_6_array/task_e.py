amount_students = int(input())  #Количество студентов
array_students = [0]*amount_students  # Список результатов студентов
amount_result_test = [0]*amount_students # Список количества тестов пройденных каждым студентом
input_data = input()




def sort_on_summ_bals(element):
    """
    Функция возвращает сумму элкментов в списке, если на вход подается одно число то возвращает его
    :param element:
    :return:
    """
    if type(element) != int:
        sum_elements = sum(element)
    else:
        sum_elements = element
    return sum_elements


def update_result_students(id, result, amount_result):
    """
Функция принимает ID студента и результат, и количество результатов студента
Должна создать массив в ячейке array_students[id] длиноой количество результатов перед эти сохранива старый и добавив
новый элемент от отсортировать
    """
    old_result = [0]*amount_result
    new_result = [0]*amount_result
    for i in range(amount_result-1):
        old_result[i] = array_students[id][i]       # запоминаем прошлые результаты
    old_result[amount_result-1] = result
    array_students[id] = sorted(old_result, reverse=True)


    pass

while input_data != '#':
    result_of_test = input_data.split()
    id_student = int(result_of_test[0])
    amount_result_test[id_student] += 1
    update_result_students(id_student, int(result_of_test[1]), int(amount_result_test[id_student]))

    print(array_students)



    input_data = input()
sorted_array_students = sorted(array_students, key=lambda x: sort_on_summ_bals(x), reverse=True)
print(sorted_array_students)


