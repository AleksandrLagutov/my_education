"""
Реализация "Шарики" на Pygame в ООП порадигме
"""
import pygame
import sys


class Balls:
    def __init__(self, x, y):
        """
        Принимает начальные координаты, и устанавливает начальную скорость.
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
        self.vx = 10
        self.vy = 10


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
dt = clock.tick(50)/1000

# основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.fill((0, 0, 0))
    pygame.display.flip()
