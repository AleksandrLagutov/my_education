import turtle

def draw(len, n, pref=0):
    """
    Графическое изображение Контарового множества
    :param len:
    :param n:
    :param pref:
    :return:
    """
    if n == 0:
        pref = len
        pass


    else:
        turtle.penup()
        turtle.goto((turtle.xcor() + pref), turtle.ycor() )
        turtle.pendown()
        turtle.forward(len)
        turtle.penup()
        turtle.goto((turtle.xcor()-len),(turtle.ycor()-10))
        draw(len/3, n-1, pref)

draw(200, 3)