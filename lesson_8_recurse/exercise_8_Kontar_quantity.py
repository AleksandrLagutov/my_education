import turtle

def draw(len, n, x = 0, y = 0):
    """
    Графическое изображение Контарового множества
    :param len:
    :param n:
    :param pref:
    :return:
    """
    dist = len/3
    if n == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(len)
        return

    else:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(len)
        draw(dist, n-1, x, y-20)
        draw(dist, n-1, x + dist*2, y-20)



draw(200, 5)