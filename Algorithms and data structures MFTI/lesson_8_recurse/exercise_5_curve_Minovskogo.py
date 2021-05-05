import turtle

def draw(len, n):
    """
    Функция принимает длину линии и уровень рекурсии
    и рисует саму ломанную
    :param len: длина линии
    :param n: уровень рекурсии
    :return: не возвращает
    """
    if n == 0:
        turtle.forward(len)
        return
    else:
        len //= 8
        draw(len, n - 1)
        turtle.left(90)
        draw(len, n - 1)
        turtle.right(90)
        draw(len, n - 1)
        turtle.right(90)
        draw(len, n - 1)
        draw(len, n - 1)
        turtle.left(90)
        draw(len, n - 1)
        turtle.left(90)
        draw(len, n - 1)
        turtle.right(90)
        draw(len, n - 1)
    pass


draw(3200, 2)