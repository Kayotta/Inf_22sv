import pygame
import sys
import random   # from random import randint
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

# Textdarstellende Funktion definieren
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    display.blit(img, (x, y))

# Schrift, Schriftfarbe und Schriftgrösse definieren
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (0, 0, 0)

# Figuren initialisieren
figuren = [0, "Schere", "Stein", "Papier"]

# Spielvariablen initialisieren
game_state = "menu"
spielerfigur = figuren[0]
computerfigur = figuren[0]
zufallsgenerator = True
comp_counter = 0
play_counter = 0

RUNNING = True
# Game Loop
while RUNNING:
    display.fill((100, 90, 255))

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
            print("spieler = Stein")
        if Buttons.paper_button.draw(display):
            spielerfigur = figuren[3]
            print("spieler = Papier")
        if Buttons.scissor_button.draw(display):
            spielerfigur = figuren[1]
            print("spieler = Schere")
        if Buttons.exit_button.draw(display):
            sys.exit()

    # Computerfigur auswählen
        while zufallsgenerator == True:
            computerfigur = figuren[random.randint(1, 3)]   # figuren[randint(1, 3)]
            print("computer =", computerfigur)
            zufallsgenerator = False

    # Sieger ermitteln
        if spielerfigur == figuren[1] or spielerfigur == figuren[2] or spielerfigur == figuren[3]:

            if spielerfigur == computerfigur:
                print("Unentschieden")
            else:
                if spielerfigur == "Schere":
                    if computerfigur == "Stein":
                        print("Verloren")
                        comp_counter = comp_counter + 1
                    else:
                        print("Gewonnen")
                        play_counter = play_counter + 1

                if spielerfigur == "Stein":
                    if computerfigur == "Papier":
                        print("Verloren")
                        comp_counter = comp_counter + 1
                    else:
                        print("Gewonnen")
                        play_counter = play_counter + 1

                if spielerfigur == "Papier":
                    if computerfigur == "Schere":
                        print("Verloren")
                        comp_counter = comp_counter + 1
                    else:
                        print("Gewonnen")
                        play_counter = play_counter + 1


            game_state = "restart"

    if game_state == "restart":
        if Buttons.restart_button.draw(display):
            game_state = "game"
            zufallsgenerator = True
            spielerfigur = figuren[0]
            draw_text(play_counter, font, TEXT_COL, 1, 1)
        if Buttons.exit_button.draw(display):
            sys.exit()

    # Eventhandler
    for event in pygame.event.get():
        # Exit Game
        if event.type == pygame.QUIT:
            sys.exit()


        pygame.QUIT
        pygame.display.update()
