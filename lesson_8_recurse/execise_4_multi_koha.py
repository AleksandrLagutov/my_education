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
def right_angle_koha(len, n):
    for i in range(3):
        draw(len, n)
        turtle.right(360/3)



right_angle_koha(400, 5)