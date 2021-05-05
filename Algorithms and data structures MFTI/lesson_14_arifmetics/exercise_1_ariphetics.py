"""
>>> is_empty_stack()
True
>>> push_steck(5)
>>> is_empty_stack()
False
>>> pop_steck()
5
>>> is_empty_stack()
True
"""
steck = []


def push_steck(x):
    """
    Функция кладет в стек переданное значение
    :return:
    """
    steck.append(x)

def pop_steck():
    """
    Функия забирает крайний элемент из стека и респечатывает его
    :return:
    """
    x = steck.pop()
    return x

def is_empty_stack():
    """
    Функция проверяет пустой ли стек, если  пустой возвращает True
    :return:
    """
    if len(steck) == 0:
        return True
    return False


def clear_steck():
    steck.clear()

def last_steck():
    return steck[-1]



def main():
    print('Всё круто')
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

