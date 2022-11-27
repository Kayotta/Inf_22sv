import pygame
import os
import sys
pygame.init()


#Display erstellen
display = pygame.display.set_mode((800, 600))

#Titel und Icon des Displays
pygame.display.set_caption("Rock-Paper-Scissors")
'''icon = pygame.image.load('rock-paper-scissors.png')
pygame.display.set_icon(icon)'''

#Game loop erstellen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT


    display.fill((0,155,0))
    pygame.display.update()
