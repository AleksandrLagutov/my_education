numbers_of_piole = int(input())
input_data_answer = input().split()
list_answer = [None]*numbers_of_piole
for i in range(numbers_of_piole):
    list_answer[i] = int(input_data_answer[i])


def search_knight(answer, numbers, guess):
    """
    Функция анализирует ответы и возвращае количество рыцарей в зависимости от первоначального предположения

    :param guess: предположение кто стоит первый рацарь или лжец
    :param answer: массив ответов жителей
    :param numbers: количество жителей
    :return: возвращает количество жителей или False если такая последовательность ответов не может существовать
    """
    list_possibility = [None]*(numbers + 1)
    list_possibility[0] = guess
    for i in range(numbers):
        if answer[i] == 0 and list_possibility[i] == 'knight':
            list_possibility[i + 1] = 'liar'
        elif answer[i] == 0 and list_possibility[i] == 'liar':
            list_possibility[i + 1] = 'knight'
        elif answer[i] == 1 and list_possibility[i] == 'knight':
            list_possibility[i + 1] = 'knight'
        elif answer[i] == 1 and list_possibility[i] == 'liar':
            list_possibility[i + 1] = 'liar'

    if list_possibility[numbers] == list_possibility[0]:
        #print('correct')
        if guess == 'knight':
            knight = list_possibility.count('knight') - 1
        else:
            knight = list_possibility.count('knight')
        return knight
    else:
        return False


print(min(search_knight(list_answer, numbers_of_piole, 'knight'), search_knight(list_answer, numbers_of_piole, 'liar')))
