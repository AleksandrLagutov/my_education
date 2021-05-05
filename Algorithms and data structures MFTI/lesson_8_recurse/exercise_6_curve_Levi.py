import turtle


def draw(len, n):
    """
    :param len: длина линии
    :param n: уровень рекурсии
    :return: ни чего не возвращает
    """
    if n == 0:
        turtle.speed(1)
        turtle.forward(len)
    else:
        turtle.left(45)
        draw(len, n-1)
        turtle.right(90)
        draw(len, n-1)
        turtle.left(45)
    pass


draw(10, 10)
