import pygame
import sys
pygame.init()


display = pygame.display.set_mode((800, 600))

while True:
    display.fill((255, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

    pygame.display.update()
