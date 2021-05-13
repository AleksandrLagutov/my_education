import turtle


def draw(len, n, k = 1):
    """

    :param len: длина линии
    :param n: уровень рекурсии
    :param k: коэфицент необходимый для разворота кривой при угле в 90 градусов
    :return:
    """
    if n == 0:
        turtle.speed('fastest')
        turtle.forward(len)
    else:
        turtle.right(45)
        draw(len, n - 1)
        turtle.left(90*k)
        draw(len, n -1, -1)
        turtle.left(45)


draw(1, 20)
