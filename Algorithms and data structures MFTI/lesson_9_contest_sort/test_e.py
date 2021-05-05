"""
Некоторые скобочные структуры правильные, другие — неправильные.
Ваша задача — определить правильная ли скобочная структура.
Входные данные
Слово в алфавите из двух круглых скобочек ( и ). Длина слова меньше 4001
Выходные данные
Либо NO, либо YES
"""
data_input = str(input())

def check_structure(data):
    for i in range(len(data)-1):
        new_data = data.replace('()', '')
        data = new_data
    return data
result = check_structure(data_input)
if result.find('(') == -1 and result.find(')') == -1:
    print('YES')
else:
    print('NO')
