import time
import random

# Variablen
import pygame

figuren = ('Schere', 'Stein', 'Papier')
spielen = True

while spielen:

    # Spielfigur auswählen
    spielerauswahl = 0
    while spielerauswahl not in (1, 2, 3):
        spielerauswahl = int(input("[1]Schere [2]Stein [3]Papier\n"))
    spielerfigur = figuren[spielerauswahl - 1]

    # Computerfigur auswählen
    computerfigur = figuren[random.randint(0, 2)]

    # Steinbild einfügen
    if spielerfigur == "Stein":
        pygame.image.load("stein.png")

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

    # Restart
    time.sleep(1)
    entscheidung = ""
    while entscheidung not in ("y", "n"):
        entscheidung = input("\nNochmal spielen? [y]Ja [n]Nein")

    if entscheidung == "n":
        spielen = False
