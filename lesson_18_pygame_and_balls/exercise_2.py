"""
Реализация "Шарики" на Pygame в ООП порадигме
"""
import pygame
import sys

# Инициализация pygame и отрисовка первоначального экрана
pygame.init()
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balls")
clock = pygame.time.Clock()


# основной цикл программы
while True:
    window.fill((0, 0, 0))
    pygame.display.flip()