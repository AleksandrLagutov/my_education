"""
Реализация "Шарики" на Pygame в ООП порадигме
При больших скоростях столкновение рабтает не корректно
"""
import pygame
import sys
import random


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


    def render(self):
        return pygame.draw.circle(window, self.col, (self.coords()), self.siz)

    def update(self):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if int(self.x) + self.siz >= width or int(self.x) - self.siz <= 0:
            self.vx = - self.vx
        if int(self.y) + self.siz >= height or int(self.y) - self.siz <= 0:
            self.vy = - self.vy
    def collision(self, this_ball):
        index = list_of_balls.index(this_ball)
        for pos in list_of_balls[index:]:
            if ((this_ball.x - pos.x) ** 2 + (this_ball.y - pos.y) ** 2) ** 0.5 < 40 and pos.x != this_ball.x and pos.y != this_ball.y:
                dist = ((this_ball.x - pos.x) ** 2 + (this_ball.y - pos.y) ** 2) ** 0.5
                n = (pos.x - this_ball.x), (pos.y - this_ball.y)
                p1 = n[0] * n[1] / (dist ** 2)
                p2 = (n[0] / dist) ** 2
                p3 = (n[1] / dist) ** 2
                d1 = this_ball.vy * p1 + this_ball.vx * p2 - pos.vx * p1 - pos.vy * p2
                d2 = this_ball.vx * p1 + this_ball.vy * p3 - pos.vx * p1 - pos.vy * p3
                this_ball.vx -= d1
                this_ball.vy -= d2
                pos.vx += d1
                pos.vy += d2




# Инициализация pygame и отрисовка первоначального экрана
pygame.init()
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balls")
clock = pygame.time.Clock()

list_of_balls = []
hands_balls = None
# основной цикл программы
while True:
    dt = clock.tick(50) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                flag = True
                for _ in list_of_balls:
                    if ((event.pos[0] - _.x)**2 + (event.pos[1] - _.y)**2 > _.siz**2):
                        flag = True
                    else:
                        hands_balls = _
                        _.col = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
                        flag = False
                        break
                if flag:
                    list_of_balls.append(Balls(event.pos))
    if hands_balls != None:
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            hands_balls.vy += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            hands_balls.vy -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            hands_balls.vx += 1
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            hands_balls.vx -= 1



    window.fill((0, 0, 0))
    for _ in list_of_balls:
        _.update()
        _.collision(_)
        _.render()



    pygame.display.flip()