"""
Программа моделеирования шара в среде. Шар отталкивается от стен и других шаров,
Шары которые добовляются по ажатию на девую клавишу мыши не подвижны.
Шар который двигается, постепенно останавливается под действие силы трения.
Шару можно придать ускорение зажав соответсвующие клетки срелки на клавиатуре
Цвет шара изменяется в зависимости от его скорости
"""
import sys
import pygame

pygame.init()
width = 500
height = 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Balls')
clock = pygame.time.Clock()

x = 21
y = 21
vx = 20
vy = 50
list_of_balls = []


while True:

    dt = clock.tick(50)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                list_of_balls.append(event.pos)
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        vy += 1
    if pygame.key.get_pressed()[pygame.K_UP]:
        vy -= 1
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        vx += 1
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        vx -= 1
    vx += -abs(vx ** 2 * 0.0001) if vx > 0 else abs(vx ** 2 * 0.0001)
    vy += -abs(vy ** 2 * 0.0001) if vy > 0 else abs(vy ** 2 * 0.0001)
    x += vx*dt
    y += vy*dt
    if int(x) + 20 >= width or int(x) - 20 <= 0:
        vx = -vx
    if int(y) + 20 >= height or int(y) - 20 <= 0:
        vy = -vy
    for pos in list_of_balls:
        if ((x - pos[0])**2 + (y - pos[1])**2)**0.5 < 40: # условие пересечения колизий https://en.wikipedia.org/wiki/Elastic_collision
            dist = ((x - pos[0])**2 + (y - pos[1])**2)**0.5
            n = (pos[0] - x), (pos[1] - y)
            p1 = n[0]*n[1]/(dist**2)
            p2 = (n[0]/dist)**2
            p3 = (n[1]/dist)**2
            d1 = vy*p1*2 + vx*p2*2
            d2 = vx*p1*2 + vy*p3*2
            vx -= d1
            vy -= d2
    window.fill((0, 0, 0))
    for pos in list_of_balls:
        pygame.draw.circle(window, (225, 150, 200), pos, 20)
    pygame.draw.circle(window, (abs(vy)+100, 0, abs(vx)+100), (int(x), int(y)), 20)

    pygame.display.flip()
