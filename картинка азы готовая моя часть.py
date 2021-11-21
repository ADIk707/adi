import pygame
from pygame.draw import *
from math import sin, cos, pi

pygame.init()

FPS = 30
screen = pygame.display.set_mode ((1100, 900))
rect(screen, (158, 234, 245), (0, 0, 1100, 450))
rect(screen, (14, 147, 37), (0, 450, 1100, 450))

def house(x, y, z):
    rect(screen, (147, 107, 14), (200 * z + x, 400 * z + y, 200 * z, 120 * z))
    rect(screen, 0, (200 * z + x, 400 * z + y, 200 * z, 120 * z), 2)
    #крыша
    polygon(screen, (235, 47, 68), [(200 * z + x, 400 * z + y), (400 * z + x, 400 * z + y), (300 * z + x, 320 * z + y)])
    polygon(screen, 0, [(200 * z + x, 400 * z + y), (400 * z + x, 400 * z + y), (300 * z + x, 320 * z + y)], 2)
    #окно
    rect(screen, (14, 147, 145), (275 * z + x, 425 * z + y, 50 * z, 50 * z))
    rect(screen, (212, 92, 32), (275 * z + x, 425 * z + y, 50 * z, 50 * z), 2)

def leaves(x, y, z):
    circle(screen, (15, 83, 14), (625 * z + x, 280 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (625 * z + x, 280 * z + y), 40 * z, 1)
    circle(screen, (15, 83, 14), (665 * z + x, 320 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (665 * z + x, 320 * z + y), 40 * z, 1)
    circle(screen, (15, 83, 14), (585 * z + x, 320 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (585 * z + x, 320 * z + y), 40 * z, 1)
    circle(screen, (15, 83, 14), (628 * z + x, 350 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (628 * z + x, 350 * z + y), 40 * z, 1)
    circle(screen, (15, 83, 14), (660 * z + x, 380 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (660 * z + x, 380 * z + y), 40 * z, 1)
    circle(screen, (15, 83, 14), (590 * z + x, 380 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (590 * z + x, 380 * z + y), 40 * z, 1)

def tree(x, y, z):
    #дерево
    rect(screen, (0, 0, 0), (610 * z + x, 400 * z + y, 30 * z, 130 * z))
    leaves(x, y, z)

def cloud(x, y, z):
    circle(screen, (255, 255, 255), (300 * z + x, 190 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (300 * z + x, 190 * z + y), 40 * z, 1)
    circle(screen, (255, 255, 255), (340 * z + x, 190 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (340 * z + x, 190 * z + y), 40 * z, 1)
    circle(screen, (255, 255, 255), (380 * z + x, 190 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (380 * z + x, 190 * z +y), 40 * z, 1)
    circle(screen, (255, 255, 255), (430 * z + x, 190 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (430 * z + x, 190 * z + y), 40 * z, 1)
    circle(screen, (255, 255, 255), (390 * z + x, 150 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (390 * z + x, 150 * z + y), 40 * z, 1)
    circle(screen, (255, 255, 255), (340 * z + x, 150 * z + y), 40 * z)
    circle(screen, (0, 0, 0), (340 * z + x, 150 * z + y), 40 * z, 1)

def sun(x, y, r, n, color):
    for i in range(n):
        line(screen, color, (x, y), (cos(2 * pi * i / n) * (r * 1) + x, sin(2 * pi * i / n) * (r * 1) + y), 3)
        circle(screen, color , (cos(2 * pi * i / n) * (r * 1) + x, sin(2 * pi * i / n) * (r * 1) + y), r * 0.3)
        circle(screen, 0, (cos(2 * pi * i / n) * (r * 1) + x, sin(2 * pi * i / n) * (r * 1) + y), r * 0.3, 1)
    circle(screen, color, (x, y), r * 1.238)

house(-200, -130, 1.5)
house(450, 100, 0.9)
tree(-140, 100, 1)
tree(500, 230, 0.6)
cloud(-80, 0, 1)
cloud(350, 120, 0.7)
cloud(550, 50, 1)

sun(100, 100, 50, 20, (249, 194, 194))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
