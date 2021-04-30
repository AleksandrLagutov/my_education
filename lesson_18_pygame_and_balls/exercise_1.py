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



while True:
    dt = clock.tick(50)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
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

    window.fill((0,0,0))
    pygame.draw.circle(window, (abs(vy),0 , abs(vy)), (int(x), int(y)), 20)

    pygame.display.flip()