import pygame
import sys

pygame.init()

'''spielerfigur = "Stein"
RED = (255, 0, 0)
GREY = (150, 150, 150)'''

# Screen erstellen
display = pygame.display.set_mode((800, 600))

# Titel und Icon
pygame.display.set_caption("Rock-Paper-Scissors")
icon = pygame.image.load('rock-paper-scissors.png')
pygame.display.set_icon(icon)
pygame.display.update()

# Game Loop
while True:
    display.fill((100, 55, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.QUIT




     # Stein
    '''if spielerfigur == "Stein":
        pygame.image.load("stein.png")
    spielerfigur = pygame.image.load("stein.png")
    bildgroesse = spielerfigur.get_rect()
    print(bildgroesse)
    print(bildgroesse.center[0])
    print(bildgroesse.center[1])
    print(bildgroesse.width)
    print(bildgroesse.height)
    display.blit(spielerfigur, (200, 205))
    pygame.display.update()'''
