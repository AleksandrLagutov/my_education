import turtle


def draw(l, n):
    """
    Функиця принимает длину и уровень рекурсии
    :return:
    """
    if n == 0:
        pass
    else:
        for i in range(n):
            turtle.speed(1)
            turtle.forward(l)
            turtle.left(60)
            turtle.forward(l)
            turtle.right(120)
            draw(l, i)
            turtle.forward(l)
            turtle.left(60)
            turtle.forward(l)
            turtle.left(60)
            draw(l, n - 1)

    pass


draw(20, 2)