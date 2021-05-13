"""
Дан список стран и языков на которых говорят в этой стране в формате <Название Страны> : <язык1> <язык2> <язык3> ...
 в файле task5/input.txt. На ввод задается N - длина списка и список языков. Для каждого языка укажите, в каких странах на нем говорят.
"""
list_of_lang_and_cauntr = []
with open('list_of_countries', 'r', encoding='utf8') as file:
    for line in file:
       list_of_lang_and_cauntr.append(line.strip('\n'))
dictionary = dict([i for i in world.split(':')] for world in list_of_lang_and_cauntr)
N = int(input())
input_list_langu = [input() for i in range(N)]
for language in input_list_langu:
    for key in dictionary:
        if language in dictionary[key].split():
            print(key, end=" ")
    print()