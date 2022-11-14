import pygame
import sys
pygame.init()

spielerfigur = "Stein"
W, H = 800, 600
RED = (255, 0, 0)
GREY = (150, 150, 150)
display = pygame.display.set_mode((800, 600))
fenster = pygame.display.set_mode((W, H))


while True:
    display.fill((100, 55, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
    # Soundintegration
    #pygame.mixer.init()  # initialisiere den Soundmixer
    #sound_rooster = pygame.mixer.Sound("Filename mit Musik")  # rooster.wav
    #sound_rooster.set_volume(1.0)  # setze die Lautstärke

    #Stein
    if spielerfigur == "Stein":
        pygame.image.load("stein.png")
    spielerfigur = pygame.image.load("stein.png")
    bildgroesse = spielerfigur.get_rect()
    print(bildgroesse)
    print(bildgroesse.center[0])
    print(bildgroesse.center[1])
    print(bildgroesse.width)
    print(bildgroesse.height)
    fenster.blit(spielerfigur, (200,205))
    pygame.display.update()

