import turtle


def draw(len, n):
    """
    Функиця принимает длину и уровень рекурсии
    :return:
    """
    if n == 0:
        turtle.forward(len)
        return
    else:
        len //= 3
        turtle.speed('fastest')
        draw(len, n - 1)
        turtle.left(60)
        draw(len, n - 1)
        turtle.right(120)
        draw(len, n - 1)
        turtle.left(60)
        draw(len, n - 1)


draw(400, 5)
