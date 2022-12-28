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
icon = pygame.image.load('bilder/rock-paper-scissors.png')
pygame.display.set_icon(icon)
pygame.display.update()

# Text darstellen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    display.blit(img, (x, y))

# Schriftart bestimmen
font = pygame.font.SysFont("arialblack", 40)

# Schriftfarbe bestimmen
TEXT_COL = (0, 0, 0)

# Game Loop
while True:
    display.fill((100, 55, 255))

    draw_text("Hello", font, TEXT_COL, 1, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        pygame.QUIT
        pygame.display.update()




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
