amount_students = int(input())  #Количество студентов
array_students = [0]*amount_students  # Список результатов студентов
amount_result_test = [0]*amount_students # Список количества тестов пройденных каждым студентом
input_data = input()

def create_array_resalt(amount):
    for i in range(amount):
        student_i = 0
    pass

def update_result_students(id, result, amount_resalt):
    """
Функция принимает ID студента и результат, и количество результатов студента
Должна создать массив в ячейке array_students[id] длиноой количество результатов перед эти сохранива старый и добавив
новый элемент от отсортировать
    """
    old_result = [0]*amount_resalt
    new_result = [0]*amount_resalt
    for i in range(amount_resalt-1):
        old_result[i] = array_students[id][i]       # запоминаем прошлые результаты
    old_result[amount_resalt-1] = result
    array_students[id] = sorted(old_result, reverse=True)


    pass

while input_data != '#':
    result_of_test = input_data.split()
    id_student = int(result_of_test[0])
    amount_result_test[id_student] +=1
    update_result_students(id_student, int(result_of_test[1]), int(amount_result_test[id_student] ))

    print(array_students)
    print(amount_result_test)


    input_data = input()
