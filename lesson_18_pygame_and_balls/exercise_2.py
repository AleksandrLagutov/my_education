"""
Реализация "Шарики" на Pygame в ООП порадигме
"""
import pygame
import sys


class Balls:
    numbers_of_balls = 0
    def __init__(self, position):
        """
        Принимает начальные координаты, и устанавливает начальную скорость.
        :param x:
        :param y:
        """
        self.x = int(position[0])
        self.y = int(position[1])
        self.vx = 20
        self.vy = 20
        self.col = 255, 250, 10
        self.siz = 20
        self.number = Balls.numbers_of_balls

    def coords(self):
        return self.x, self.y

    def colors(self):
        return self.col
    def size(self):
        return self.siz

class Moving:
    pass


class Collision:
    pass


class Draw:

    pass

# Инициализация pygame и отрисовка первоначального экрана
pygame.init()
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balls")
clock = pygame.time.Clock()

list_of_balls = []
# основной цикл программы
while True:
    dt = clock.tick(50) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                list_of_balls.append(Balls(event.pos))

    window.fill((0, 0, 0))
    for _ in list_of_balls:
        _.x += _.vx*dt
        _.y += _.vy*dt
        if int(_.x) + 20 >= width or int(_.x) - 20 <= 0:
            _.vx = - _.vx
        if int(_.y) + 20 >= height or int(_.y) - 20 <= 0:
            _.vy = - _.vy
        pygame.draw.circle(window, (_.colors()), (_.coords()), _.size())

    pygame.display.flip()