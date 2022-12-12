import pygame
import sys
import random
import time
#from Buttons import Button
import Buttons

pygame.init()

# Screen erstellen
display = pygame.display.set_mode((800, 600))

# Titel und Icon
pygame.display.set_caption("Rock-Paper-Scissors")
icon = pygame.image.load('bilder/rock-paper-scissors.png')
pygame.display.set_icon(icon)
pygame.display.update()

# Figuren initialisieren
figuren = ["Schere", "Stein", "Papier"]

# Game Loop
while True:
    display.fill((100, 55, 255))


    # Startbildschirm und Startknopf kreieren
    Buttons.start_button.draw()
    if Buttons.start_button.clicked == True:
        Buttons.start_button = Buttons.Button(305, 200, Buttons.start_img, 0)

        Buttons.rock_button.draw()
        Buttons.paper_button.draw()
        Buttons.scissor_button.draw()

     # Spielerfigur auswählen
    if Buttons.scissor_button.clicked == True:
        spielerfigur = figuren[0]
    elif Buttons.rock_button.clicked == True:
        spielerfigur = figuren[1]
    else:
        spielerfigur = figuren[2]


    # Computerfigur auswählen
    computerfigur = figuren[random.randint(0, 2)]

    # Sieger ermitteln
    if spielerfigur == computerfigur:
        print("Unentschieden")
    else:
        if spielerfigur == "Schere":
            if computerfigur == "Stein":
                print("Verloren")
            else:
                print("Gewonnen")

        if spielerfigur == "Stein":
            if computerfigur == "Papier":
                print("Verloren")
            else:
                print("Gewonnen")

        if spielerfigur == "Papier":
            if computerfigur == "Schere":
                print("Verloren")
            else:
                print("Gewonnen")

    # Eventhandler
    for event in pygame.event.get():
        # Exit Game
        if event.type == pygame.QUIT:
            sys.exit()


        pygame.QUIT
        pygame.display.update()
