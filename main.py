import pygame
import sys
import random
from pygame import mixer
import time

from pygame.font import Font

import Buttons

# Initialisiere Pygame und den Mixer
pygame.init()
pygame.mixer.init()

# Screen erstellen
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Display = 1280 * 720

# Windowcaption und Icon
pygame.display.set_caption("Rock-Paper-Scissors")
icon = pygame.image.load('bilder/rock-paper-scissors.png')
pygame.display.set_icon(icon)

# Musik und Soundeffekte
winning_sound = pygame.mixer.Sound("sound/mixkit-fantasy-game-success-notification-270.wav")
winning_sound.set_volume(0.5)
losing_sound = pygame.mixer.Sound("sound/mixkit-player-losing-or-failing-2042.wav")
losing_sound.set_volume(1.0)
draw_sound = pygame.mixer.Sound("sound/mixkit-bell-notification-933.wav")
draw_sound.set_volume(0.5)

# Textdarstellende Funktion definieren
def draw_text(text, font, text_col, x, y):
    img = font.render(str(text), True, text_col)
    display.blit(img, (x, y))

# Schrift, Schriftfarbe und Schriftgrösse definieren
font = pygame.font.SysFont("arialblack", 40)
font1 = pygame.font.SysFont("Impact", 40)
font2 = pygame.font.SysFont("Impact", 50)
TEXT_COL = (0, 0, 0)

# Figuren initialisieren
figuren = [0, "Stein", "Papier", "Schere"]
play_bilder = [0, pygame.image.load("bilder/Fighting/rock1.png"), pygame.image.load("bilder/Fighting/paper1.png"), pygame.image.load("bilder/Fighting/scissors1.png")]
comp_bilder = [0, pygame.image.load("bilder/Fighting/rock2.png"), pygame.image.load("bilder/Fighting/paper2.png"), pygame.image.load("bilder/Fighting/scissors2.png")]
# play- und comp_bilder sind die Listen, die die bilder für den Game-Status "fighting" beinhalten
# so wird dargestellt, wer welche Figur gewählt hat.

# Spielvariablen initialisieren
game_state = "main_menu"
hintergrundfarbe = "blue"
spielerfigur = figuren[0]
computerfigur = figuren[0]
zufallsgenerator = True
'''sound_play1 = False
sound_play2 = False
sound_play3 = False'''
comp_counter = 0
play_counter = 0
win = 0         # win = 1 bedeutet Spieler hat gewonnen, win = 2 bedeutet Computer hat gewonnen
                # win = 3 bedeutet unentschieden

# Sonstige Bilder laden
# Bild für den Startbildschirm
startbild = pygame.image.load("bilder/rockpaperscissors.png")
# Bilder für den Game-Status "fighting", bzw. Darstellung des Spielausgangs
winning = pygame.image.load("bilder/win.png")
winning_groesse = winning.get_rect()
winning = pygame.transform.scale(winning, (512, 512))
print(winning_groesse)              # drei Schritte, um die Bilder neu zu skalieren
losing = pygame.image.load("bilder/lose.png")
draw = pygame.image.load("bilder/draw.png")


# Game loop
RUNNING = True
while RUNNING:
    display.fill((49, 29, 209))

    # Game-Status "main_menu"
    if game_state == "main_menu":
        # Abfrage der Hintergrundfarbe, da diese im Menu verändert werden kann
        if hintergrundfarbe == "pink":
            display.fill((253, 172, 226))
        if hintergrundfarbe == "yellow":
             display.fill((249, 211, 35))
        if hintergrundfarbe == "blue":
            display.fill((49, 26, 209))

        # Abbilden des Bildes auf dem Startbildschirm
        display.blit(startbild, (384, 104))
        # Abbilden von Start-, Exit- und Menubutton und Abfrage nach deren Status (angeklickt oder nicht)
        # Code dieses Mechanismus' in Buttons zu finden
        if Buttons.menu_button.draw(display):
            game_state = "lower_menu"
        if Buttons.start_button.draw(display):
            game_state = "game"
        if Buttons.exit_button.draw(display):
            sys.exit()

    # Menu wird geöffnet
    if game_state == "lower_menu":
        # Abfrage der Hintergrundfarbe, die hier verändert werden kann
        if game_state == "main_menu":
            if hintergrundfarbe == "pink":
                display.fill((253, 172, 226))
            if hintergrundfarbe == "yellow":
                 display.fill((249, 211, 35))
            if hintergrundfarbe == "blue":
                display.fill((49, 26, 209))

        # Text zur Beschriftung der Buttons
        draw_text("Sound:", font1, TEXT_COL, 20, 200)
        draw_text("Background:", font1, TEXT_COL, 20, 340)
        draw_text("Music:", font1, TEXT_COL, 20, 480)
        # Abbilden der Musicbuttons und Abfragen deren Staten
        if Buttons.music1_button.draw(display):
            print("eins")
        if Buttons.music2_button.draw(display):
            print("zwei")
        if Buttons.music3_button.draw(display):
            print("drei")
        # Abbilden der Colorbuttons
        if Buttons.blue_button.draw(display):
            hintergrundfarbe = "blue"
        if Buttons.pink_button.draw(display):
            hintergrundfarbe = "pink"
        if Buttons.yellow_button.draw(display):
            hintergrundfarbe = "yellow"
        # Abbilden der Mute- und Unmutebuttons
        if Buttons.unmute_button.draw(display):
            winning_sound.set_volume(0.5)
            losing_sound.set_volume(1.0)
            draw_sound.set_volume(0.5)
            Buttons.clicked_sound.set_volume(1.0)
        if Buttons.mute_button.draw(display):
            winning_sound.set_volume(0.0)
            losing_sound.set_volume(0.0)
            draw_sound.set_volume(0.0)
            Buttons.clicked_sound.set_volume(0.0)
        # Abbilden des Returnbuttons
        if Buttons.back_button.draw(display):   # Wait-Funktion, damit nicht ausversehen der Exitbutton gedrückt
            pygame.display.update()             # wird, er befindet sich an denselben Koordinaten wie der Returnbutton
            pygame.time.wait(250)               # durch eine Verzögerung wird der Game-Status noch nicht geändert und der
            game_state = "main_menu"            # Knopf nicht abgebildet, so kann er nicht gedrückt werden.

    # Das Spiel beginnt
    if game_state == "game":

        # Hintergrundfarbe wird abgefragt
        if hintergrundfarbe == "pink":
            display.fill((253, 172, 226))
        if hintergrundfarbe == "yellow":
             display.fill((249, 211, 35))
        if hintergrundfarbe == "blue":
            display.fill((49, 26, 209))
        # Score wird dargestellt
        draw_text("Your Score:", font2, TEXT_COL, 20, 20)
        draw_text(play_counter, font2, TEXT_COL, 290, 20)
        draw_text("Computer Score:", font2, TEXT_COL, 830, 20)
        draw_text(comp_counter, font2, TEXT_COL, 1210, 20)
        # Spielfiguren abgebildet und Status abgefragt
        if Buttons.rock_button.draw(display):
            spielerfigur = figuren[1]
            bild1 = play_bilder[1]
        if Buttons.paper_button.draw(display):
            spielerfigur = figuren[2]
            bild1 = play_bilder[2]
        if Buttons.scissors_button.draw(display):
            spielerfigur = figuren[3]
            bild1 = play_bilder[3]

        # Computerfigur auswählen
        while zufallsgenerator == True:
            computerfigur = figuren[random.randint(1, 3)]
            zufallsgenerator = False        # While-Schleife damit nur eine Figur gewählt wird
        if computerfigur == figuren[1]:
            bild2 = comp_bilder[1]          # Zuweisen der Figur zu einem Bild der Liste
        elif computerfigur == figuren[2]:
            bild2 = comp_bilder[2]
        else:
            bild2 = comp_bilder[3]


        # Bestimmung des Siegers
        if spielerfigur == figuren[1] or spielerfigur == figuren[2] or spielerfigur == figuren[3]:

            if spielerfigur == computerfigur:
                win = 3

                '''if spielerfigur == computerfigur:   # funktioniert nicht ganz
                    def draw_text(text, font1, text_col, x, y):
                        img = font.render(str('Unentschieden'),font1, TEXT_COL)
                        display.blit(img, (200, 400))
                    print("Unentschieden")'''
            else:
                if spielerfigur == "Schere":
                    if computerfigur == "Stein":
                        win = 2
                        comp_counter = comp_counter + 1
                    else:
                        win = 1
                        play_counter = play_counter + 1

                elif spielerfigur == "Stein":
                    if computerfigur == "Papier":
                        win = 2
                        comp_counter = comp_counter + 1
                    else:
                        win = 1
                        play_counter = play_counter + 1

                else:
                    if computerfigur == "Schere":
                        win = 2
                        comp_counter = comp_counter + 1
                    else:
                        win = 1
                        play_counter = play_counter + 1

            game_state = "fighting"

    if game_state == "fighting":
        # Hintergrundfarbe
        if hintergrundfarbe == "pink":
            display.fill((253, 172, 226))
        if hintergrundfarbe == "yellow":
             display.fill((249, 211, 35))
        if hintergrundfarbe == "blue":
            display.fill((49, 26, 209))
        # Spieler hat gewonnen
        if win == 1:
            sound_play = True
            while sound_play ==True:
                display.blit(bild1, (20, 300))
                display.blit(bild2, (700, 300))
                display.blit(winning, (384, 50))
                winning_sound.play()
                pygame.display.update()
                pygame.time.wait(2800)      # Bildschirm wird durch die Verzögerung 2.8 Sekunden lang
                sound_play = False          # dargestellt, sonst wären es bloss Millisekunden
                game_state = "restart"
        # Spieler hat verloren
        if win == 2:
            sound_play = True
            while sound_play == True:
                display.blit(bild1, (20, 300))
                display.blit(bild2, (700, 300))
                display.blit(losing, (384, 50))
                losing_sound.play()
                pygame.display.update()
                pygame.time.wait(2800)
                sound_play = False
                game_state = "restart"
        # Unentschieden
        if win == 3:
            sound_play = True
            while sound_play == True:
                display.blit(bild1, (20, 300))
                display.blit(bild2, (700, 300))
                display.blit(draw, (384, 50))
                draw_sound.play()
                pygame.display.update()
                pygame.time.wait(2800)
                sound_play = False
                game_state = "restart"

    if game_state == "restart":
        # Hintergrundfarbe
        if hintergrundfarbe == "pink":
            display.fill((253, 172, 226))
        if hintergrundfarbe == "yellow":
             display.fill((249, 211, 35))
        if hintergrundfarbe == "blue":
            display.fill((49, 26, 209))
        # Darstellung von Spielstand
        draw_text("Your Score:", font2, TEXT_COL, 20, 20)
        draw_text(play_counter, font2, TEXT_COL, 290, 20)
        draw_text("Computer Score:", font2, TEXT_COL, 830, 20)
        draw_text(comp_counter, font2, TEXT_COL, 1210, 20)
        # Abbilden und Abfragen der Buttons, Variablen werden in den Startzustand versetzt
        if Buttons.continue_button.draw(display):
            pygame.time.wait(250)
            game_state = "game"
            zufallsgenerator = True
            spielerfigur = figuren[0]
            computerfigur = figuren[0]
        if Buttons.reset_button.draw(display):
            game_state = "main_menu"
            play_counter = 0
            comp_counter = 0
            zufallsgenerator = True
            spielerfigur = figuren[0]
            computerfigur = figuren[0]
        if Buttons.exit1_button.draw(display):
            sys.exit()

    # Eventhandler
    for event in pygame.event.get():
        # Exit Game
        if event.type == pygame.QUIT:
            sys.exit()


        pygame.QUIT
        pygame.display.update()
