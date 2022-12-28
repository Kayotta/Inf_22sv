import pygame
import sys
import random
import time
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
figuren = [0, "Schere", "Stein", "Papier"]

# Spielvariablen initialisieren
game_state = "menu"
spielerfigur = False

RUNNING = True
# Game Loop
while RUNNING:
    display.fill((100, 55, 255))

    # Startbildschirm und Startknopf kreieren
    if game_state == "menu":
        if Buttons.exit_button.draw(display):
            sys.exit()
        if Buttons.start_button.draw(display):
            # Spiel beginnt
            game_state = "game"

    # Spielerfigur auswählen
    if game_state == "game":
        if Buttons.rock_button.draw(display):
            spielerfigur = figuren[2]
        if Buttons.paper_button.draw(display):
            spielerfigur = figuren[3]
        if Buttons.scissor_button.draw(display):
            spielerfigur = figuren[1]
        if Buttons.exit_button.draw(display):
            sys.exit()


    # Computerfigur auswählen
        computerfigur = figuren[random.randint(1, 3)]

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
