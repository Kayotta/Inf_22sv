import pygame
import sys
pygame.init()

#Display erstellen
display = pygame.display.set_mode((800, 600))

#Icon und Titel ändern
pygame.display.set_caption("Rock-Paper-Scissors")
pygame.image.load('rock-paper-scissors.png')
icon = pygame.image.load('rock-paper-scissors.png')
pygame.display.set_icon(icon)

#Spielloop erstellen
while True:
    display.fill((236, 154, 245))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

    pygame.display.update()
