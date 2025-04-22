from operator import truediv

import pygame
import scipy
import numpy
from scipy.stats import false_discovery_control

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

aPressed = False
dPressed = False

location = 0

while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_a):
                aPressed = True
            elif (event.key == pygame.K_d):
                dPressed = True
        elif (event.type == pygame.KEYUP):
            if (event.key == pygame.K_a):
                aPressed = False
            elif (event.key == pygame.K_d):
                dPressed = False

    if (aPressed):
        if (location >= -250):
            location -= 1
    if (dPressed):
        if (location <= 250):
            location += 1

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (80, 80, 255), [100, 300 + location, 400, 100], 8)

    pygame.display.flip()

pygame.quit()
