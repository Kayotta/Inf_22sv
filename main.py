import pygame
import sys
import random   # from random import randint
from pygame import mixer
import time

from pygame.font import Font

import Buttons

pygame.init()
pygame.mixer.init()

# Screen erstellen
display = pygame.display.set_mode((900, 600))

# Titel und Icon
pygame.display.set_caption("Rock-Paper-Scissors")
icon = pygame.image.load('bilder/rock-paper-scissors.png')
pygame.display.set_icon(icon)

# Musik und Soundeffekte



# Textdarstellende Funktion definieren
def draw_text(text, font, text_col, x, y):
    img = font.render(str(text), True, text_col)
    display.blit(img, (x, y))

# Schrift, Schriftfarbe und Schriftgrösse definieren
font = pygame.font.SysFont("arialblack", 40)
font1 = pygame.font.SysFont("Impact", 40)
TEXT_COL = (0, 0, 0)

# Figuren initialisieren
figuren = [0, "Stein", "Papier", "Schere"]
play_bilder = [0, pygame.image.load("bilder/Fighting/rock1.png"), pygame.image.load("bilder/Fighting/paper1.png"), pygame.image.load("bilder/Fighting/scissors1.png")]
comp_bilder = [0, pygame.image.load("bilder/Fighting/rock2.png"), pygame.image.load("bilder/Fighting/paper2.png"), pygame.image.load("bilder/Fighting/scissors2.png")]

# Spielvariablen initialisieren
game_state = "menu"
spielerfigur = figuren[0]
computerfigur = figuren[0]
zufallsgenerator = True
comp_counter = 0
play_counter = 0
win = 0         # win = 1 bedeutet Spieler hat gewonnen, win = 2 bedeutet Computer hat gewonnen

# Sonstige Bilder laden
winning = pygame.image.load("bilder/win.png")
losing = pygame.image.load("bilder/lose.png")
draw = pygame.image.load("bilder/draw.png")

RUNNING = True
# Game Loop
while RUNNING:
    display.fill((29, 46, 209))

    if game_state == "menu":
        # Startbildschirm kreieren
        startbild = pygame.image.load("bilder/rockpaperscissors.png").convert_alpha()
        display.blit(startbild, (200, 100))
        if Buttons.exit_button.draw(display): # 0.3):
            sys.exit()
        if Buttons.start_button.draw(display):  # 0.5):
            # Spiel beginnt
            game_state = "game"

    # Spielerfigur auswählen
    if game_state == "game":
        if Buttons.rock_button.draw(display): # 0.4):
            spielerfigur = figuren[1]
            bild1 = play_bilder[1]
            print("spieler = Stein")
        if Buttons.paper_button.draw(display): # 0.6):
            spielerfigur = figuren[2]
            bild1 = play_bilder[2]
            print("spieler = Papier")
        if Buttons.scissors_button.draw(display): # 0.5):
            spielerfigur = figuren[3]
            bild1 = play_bilder[3]
            print("spieler = Schere")
        if Buttons.exit_button.draw(display): # 0.3):
            sys.exit()

    # Computerfigur auswählen
        while zufallsgenerator == True:
            computerfigur = figuren[random.randint(1, 3)]   # figuren[randint(1, 3)]
            print("computer =", computerfigur)
            zufallsgenerator = False
        if computerfigur == figuren[1]:
            bild2 = comp_bilder[1]
        if computerfigur == figuren[2]:
            bild2 = comp_bilder[2]
        if computerfigur == figuren[3]:
            bild2 = comp_bilder[3]



    # Sieger ermitteln
        if spielerfigur == figuren[1] or spielerfigur == figuren[2] or spielerfigur == figuren[3]:

            if spielerfigur == computerfigur:
                print("Unentschieden")
                win = 3

                '''if spielerfigur == computerfigur:   # funktioniert nicht ganz
                    def draw_text(text, font1, text_col, x, y):
                        img = font.render(str('Unentschieden'),font1, TEXT_COL)
                        display.blit(img, (200, 400))
                    print("Unentschieden")'''
            else:
                if spielerfigur == "Schere":
                    if computerfigur == "Stein":
                        print("Verloren")
                        win = 2
                        comp_counter = comp_counter + 1
                    else:
                        print("Gewonnen")
                        win = 1
                        play_counter = play_counter + 1

                if spielerfigur == "Stein":
                    if computerfigur == "Papier":
                        print("Verloren")
                        win = 2
                        comp_counter = comp_counter + 1
                    else:
                        print("Gewonnen")
                        win = 1
                        play_counter = play_counter + 1

                if spielerfigur == "Papier":
                    if computerfigur == "Schere":
                        print("Verloren")
                        win = 2
                        comp_counter = comp_counter + 1
                    else:
                        print("Gewonnen")
                        win = 1
                        play_counter = play_counter + 1

            game_state = "fighting"

    if game_state == "fighting":
        x = -40
        y = 80
        display.blit(bild1, (x, y))         # -20, 100
        for i in range(20):
            x = x + 1
            y = y + 1
        display.blit(bild2, (400,100))
        if win == 1:
            display.blit(winning, (200, 100))
        if win == 2:
            display.blit(losing, (200, 100))
        if win == 3:
            display.blit(draw, (200, 100))
        if Buttons.exit_button.draw(display): # 0.3):
            sys.exit()

        # game_state = "restart"      # Achtung: für game_state = "restart" ist noch keine Bedingung gesetzt.
                                      # Deshalb wird game_state = "fighting" nur für Milisekunden dargestellt
    if game_state == "restart":
        draw_text("Your Score:", font1, TEXT_COL, 1, 1)
        draw_text(play_counter, font1, TEXT_COL, 230, 1)
        draw_text("Computer Score:", font1, TEXT_COL, 450, 1)
        draw_text(comp_counter, font1, TEXT_COL, 750, 1)

        if Buttons.continue_button.draw(display): # 0.3):
            game_state = "game"
            zufallsgenerator = True
            spielerfigur = figuren[0]
            computerfigur = figuren[0]
        if Buttons.reset_button.draw(display): # 0.3):
            game_state = "menu"
            play_counter = 0
            comp_counter = 0
            zufallsgenerator = True
            spielerfigur = figuren[0]
            computerfigur = figuren[0]
        if Buttons.exit_button.draw(display): # 0.3):
            sys.exit()
    # Eventhandler
    for event in pygame.event.get():
        # Exit Game
        if event.type == pygame.QUIT:
            sys.exit()


        pygame.QUIT
        pygame.display.update()
