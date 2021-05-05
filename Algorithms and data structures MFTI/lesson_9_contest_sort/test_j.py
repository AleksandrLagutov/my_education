"""
Задача J: Словарь для блондинки
Блондинка Даша любит решать кроссворды на латинском языке, пользуясь орфографическим словарем. Часто Даша отгадывает
последние буквы слова и долго ищет каким словам подходит такая концовка. Она мечтает о словаре, где бы слова были разбиты на главы по количеству букв в слове и написаны задом наперед. Помогите ей составить такой словарь по заданному орфографическому словарю латинском языка.

Формат входных данных
В первой строке содержится единственное целое число N (1≤N≤100) — количество латинских слов в словаре. Далее следует N
слов по одному слову на строку. Все слова состоят только из маленьких латинских букв. Общее количество слов на входе не превышает 100. Длина каждого слова не превосходит 15 символов.

Формат результата
Длина слов в данном блоке. На следующих строках слова задом наперед и исходное слово через пробел в лексикографическом
порядке.
"""
size_input_data = int(input())
input_data = []
sort_data = []
new_sort_data = []
flag = True

def sort_input_data(data:list):
    """
    Функция должна отсортировать массив по длине второго вложенного элемента если вторые равны то учитывать перввый в
      возрастании


    :return:
    """
    for top in range(1, len(data)):
        k = top
        while k > 0:
            if len(data[k-1][1]) > len(data[k][1]):
                data[k], data[k-1] = data[k-1], data[k]
            if len(data[k-1][1]) == len(data[k][1]) and data[k-1][0] > data[k][0]:
                data[k], data[k-1] = data[k-1], data[k]
            k -= 1
    return data


for i in range(size_input_data):
    input_data.append(input())
for k in range(1, 16):
    for i in range(size_input_data):
        if len(input_data[i]) == k:
            sort_data.append(list([input_data[i][::-1], input_data[i]]))
sort_input_data(sort_data)
len_words = len(sort_data[0][0])
print(len_words)
for i in range(size_input_data):
    if len(sort_data[i][0]) != len_words:
        print(len(sort_data[i][0]))
        len_words = len(sort_data[i][0])
    print(*sort_data[i])
