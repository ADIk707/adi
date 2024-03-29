import pygame
from pygame.draw import *
from pygame.transform import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1200))
# фон типа
rect(screen, (125, 125, 125), (0, 0, 794, 530))
rect(screen, (0, 0, 0), (0, 561, 794, 561))

def house(x, y):
    # крыша
    polygon(screen, (0, 0, 0), [[20 + x, 400 + y], [70 + x, 370 + y], [280 + x, 370 + y], [330 + x, 400 + y]])
    aalines(screen, (0, 0, 0), True, [[20 + x, 400 + y], [70 + x, 370 + y], [280 + x, 370 + y], [330 + x, 400 + y]])
    # трубы
    rect(screen, (26, 26, 26), (100 + x, 310 + y, 20, 80))
    rect(screen, (26, 26, 26), (85 + x, 325 + y, 9, 60))
    rect(screen, (26, 26, 26), (215 + x, 330 + y, 9, 40))
    rect(screen, (26, 26, 26), (260 + x, 330 + y, 9, 60))
    # здание заливка
    rect(screen, (43, 34, 0), (50 + x, 400 + y, 250, 150))
    rect(screen, (40, 34, 11), (50 + x, 550 + y, 250, 180))
    # окна второго этажа
    for i in range(1, 5):
        rect(screen, (72, 62, 55), ((65 * i) + x, 400 + y, 27, 130))
    # балкон??
    rect(screen, (26, 26, 26), (15 + x, 525 + y, 320, 35))
    rect(screen, (26, 26, 26), (35 + x, 485 + y, 280, 15))
    rect(screen, (26, 26, 26), (27 + x, 500 + y, 10, 25))
    for i in range(1, 5):
        rect(screen, (26, 26, 26), ((65 * i) + x, 500 + y, 15, 30))
    rect(screen, (26, 26, 26), (314 + x, 500 + y, 10, 25))
    # окна перового этажа
    for i in range(1, 3):
        rect(screen, (43, 17, 0), ((75 * i) + x, 630 + y, 50, 60))
    rect(screen, (212, 170, 0), (225 + x, 630 + y, 50, 60))

# луна
circle(screen, (200, 230, 230), (460, 300), 50)

def clouds(color, x, y, long):
    ellipse(screen, color, (0 + x, 200 + y, long, 40))

def ghost(x, y, k):
    z = k * 10 #коэфф k меняет размер призрака. !!! k>0 !!!
    circle(screen, (179, 179, 179), (465 + x, 720 + y), 27 * k // 2) #тут при изменении размера надо методом тыка к координатам ещё что-то прибавить или убавить(я про x и y). ума не хватило
    aalines(screen, (179, 179, 179), True,
            [(440 + x, 730 + y), (440 + x - (0.11 * z), (0.53 * z) + 730 + y),
            (440 + x - (z * 0.21), (0.92 * z) + 730 + y), (440 + x - (0.39 * z), (1.31 * z) + 730 + y),
            (440 + x - (0.56 * z), (1.62 * z) + 730 + y), (440 + x - (0.64 * z), (1.80 * z) + 730 + y),
            (440 + x - (0.85 * z), (2.29 * z) + 730 + y), (440 + x - (0.99 * z), (2.58 * z) + 730 + y),
            (440 + x - (1.38 * z), (3.00 * z) + 730 + y), (440 + x - (1.48 * z), (3.35 * z) + 730 + y),
            (440 + x - (1.52 * z), (3.60 * z) + 730 + y), (440 + x - (1.76 * z), (4.09 * z) + 730 + y),
            (440 + x - (2.05 * z), (4.27 * z) + 730 + y), (440 + x - (1.94 * z), (4.48 * z) + 730 + y),
            (440 + x - (1.73 * z), (4.45 * z) + 730 + y), (440 + x - (1.48 * z), (4.41 * z) + 730 + y),
            (440 + x - (1.02 * z), (4.34 * z) + 730 + y), (440 + x - (0.74 * z), (4.30 * z) + 730 + y),
            (440 + x - (0.46 * z), (4.45 * z) + 730 + y), (440 + x - (0.11 * z), (4.59 * z) + 730 + y),
            (440 + x + (0.21 * z), 730 + y + (4.76 * z)), (440 + x + (0.60 * z), 730 + y + (5.33 * z)),
            (440 + x + (0.74 * z), 730 + y + (5.54 * z)), (440 + x + (1.13 * z), 730 + y + (5.61 * z)),
            (440 + x + (1.52 * z), 730 + y + (5.54 * z)), (440 + x + (1.80 * z), 730 + y + (5.36 * z)),
            (440 + x + (2.36 * z), 730 + y + (4.80 * z)), (440 + x + (2.86 * z), 730 + y + (4.62 * z)),
            (440 + x + (3.39 * z), 730 + y + (4.66 * z)), (440 + x + (3.85 * z), 730 + y + (4.62 * z)),
            (440 + x + (4.20 * z), 730 + y + (4.69 * z)), (440 + x + (4.37 * z), 730 + y + (4.41 * z)),
            (440 + x + (4.52 * z), 730 + y + (4.09 * z)), (440 + x + (4.62 * z), 730 + y + (3.67 * z)),
            (440 + x + (4.83 * z), 730 + y + (3.35 * z)), (440 + x + (5.15 * z), 730 + y + (3.21 * z)),
            (440 + x + (5.50 * z), 730 + y + (3.18 * z)), (440 + x + (5.89 * z), 730 + y + (2.75 * z)),
            (440 + x + (5.96 * z), 730 + y + (2.26 * z)), (440 + x + (5.79 * z), 730 + y + (1.83 * z)),
            (440 + x + (5.64 * z), 730 + y + (1.59 * z)), (440 + x + (5.29 * z), 730 + y + (1.34 * z)),
            (440 + x + (4.94 * z), 730 + y + (1.09 * z)), (440 + x + (4.62 * z), 730 + y + (0.85 * z)),
            (440 + x + (4.37 * z), 730 + y + (0.60 * z)), (440 + x + (4.06 * z), 730 + y + (0.25 * z)),
            (440 + x + (3.88 * z), 730 + y + (0.14 * z)), (440 + x + (3.63 * z), 730 + y - (0.14 * z)),
            (440 + x + (3.28 * z), 730 + y - (0.42 * z)), (440 + x + (3.03 * z), 730 + y - (0.56 * z)),
            (440 + x + (2.72 * z), 730 + y - (0.85 * z)), (440 + x + 2.01 * z, 730 + y - 1.06 * z)], 1000)
    polygon(screen, (179, 179, 179),
            [(440 + x, 730 + y), (440 + x - (0.11 * z), (0.53 * z) + 730 + y),
             (440 + x - (z * 0.21), (0.92 * z) + 730 + y), (440 + x - (0.39 * z), (1.31 * z) + 730 + y),
             (440 + x - (0.56 * z), (1.62 * z) + 730 + y), (440 + x - (0.64 * z), (1.80 * z) + 730 + y),
             (440 + x - (0.85 * z), (2.29 * z) + 730 + y), (440 + x - (0.99 * z), (2.58 * z) + 730 + y),
             (440 + x - (1.38 * z), (3.00 * z) + 730 + y), (440 + x - (1.48 * z), (3.35 * z) + 730 + y),
             (440 + x - (1.52 * z), (3.60 * z) + 730 + y), (440 + x - (1.76 * z), (4.09 * z) + 730 + y),
             (440 + x - (2.05 * z), (4.27 * z) + 730 + y), (440 + x - (1.94 * z), (4.48 * z) + 730 + y),
             (440 + x - (1.73 * z), (4.45 * z) + 730 + y), (440 + x - (1.48 * z), (4.41 * z) + 730 + y),
             (440 + x - (1.02 * z), (4.34 * z) + 730 + y), (440 + x - (0.74 * z), (4.30 * z) + 730 + y),
             (440 + x - (0.46 * z), (4.45 * z) + 730 + y), (440 + x - (0.11 * z), (4.59 * z) + 730 + y),
             (440 + x + (0.21 * z), 730 + y + (4.76 * z)), (440 + x + (0.60 * z), 730 + y + (5.33 * z)),
             (440 + x + (0.74 * z), 730 + y + (5.54 * z)), (440 + x + (1.13 * z), 730 + y + (5.61 * z)),
             (440 + x + (1.52 * z), 730 + y + (5.54 * z)), (440 + x + (1.80 * z), 730 + y + (5.36 * z)),
             (440 + x + (2.36 * z), 730 + y + (4.80 * z)), (440 + x + (2.86 * z), 730 + y + (4.62 * z)),
             (440 + x + (3.39 * z), 730 + y + (4.66 * z)), (440 + x + (3.85 * z), 730 + y + (4.62 * z)),
             (440 + x + (4.20 * z), 730 + y + (4.69 * z)), (440 + x + (4.37 * z), 730 + y + (4.41 * z)),
             (440 + x + (4.52 * z), 730 + y + (4.09 * z)), (440 + x + (4.62 * z), 730 + y + (3.67 * z)),
             (440 + x + (4.83 * z), 730 + y + (3.35 * z)), (440 + x + (5.15 * z), 730 + y + (3.21 * z)),
             (440 + x + (5.50 * z), 730 + y + (3.18 * z)), (440 + x + (5.89 * z), 730 + y + (2.75 * z)),
             (440 + x + (5.96 * z), 730 + y + (2.26 * z)), (440 + x + (5.79 * z), 730 + y + (1.83 * z)),
             (440 + x + (5.64 * z), 730 + y + (1.59 * z)), (440 + x + (5.29 * z), 730 + y + (1.34 * z)),
             (440 + x + (4.94 * z), 730 + y + (1.09 * z)), (440 + x + (4.62 * z), 730 + y + (0.85 * z)),
             (440 + x + (4.37 * z), 730 + y + (0.60 * z)), (440 + x + (4.06 * z), 730 + y + (0.25 * z)),
             (440 + x + (3.88 * z), 730 + y + (0.14 * z)), (440 + x + (3.63 * z), 730 + y - (0.14 * z)),
             (440 + x + (3.28 * z), 730 + y - (0.42 * z)), (440 + x + (3.03 * z), 730 + y - (0.56 * z)),
             (440 + x + (2.72 * z), 730 + y - (0.85 * z)), (440 + x + 2.01 * z, 730 + y - 1.06 * z)])
    circle(screen, (135, 205, 222), (453 + x, 720 + y), 9)
    circle(screen, (135, 205, 222), (473 + x, 715 + y), 9)
    circle(screen, (0, 0, 0), (469 + x, 715 + y), 3)
    circle(screen, (0, 0, 0), (449 + x, 720 + y), 3)

    #и сними надо мучиться, чтобы они были тамб где надо. колдуй над координатами
    #поэтому наверное будет лучше это блики рисовать вне функции. то естть вынести эту часть кода (?)
    surf = pygame.Surface((794, 1123), pygame.SRCALPHA) #левый блик
    ellipse(surf, (249, 249, 249), (167 + x, 195 + y, 10, 4))
    surf = rotate(surf, 35)
    screen.blit(surf, (200, 200))

    surf = pygame.Surface((794, 1123), pygame.SRCALPHA) #правый блик
    ellipse(surf, (249, 249, 249), (186 + x, 203 + y, 10, 4))
    surf = rotate(surf, 35)
    screen.blit(surf, (200, 200))

house(0, 0) #меняя координаты по ох и оу, прибавляя их к исхродным координатам, происходит перемещение. методом тыка получится
clouds((77, 77, 77), 0, 0, 300) #возможные цвета, они же color: (51, 51, 51), (77, 77, 77). !!! long>300  !!!
ghost(0, 0, 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
