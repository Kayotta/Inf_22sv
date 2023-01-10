import pygame
import sys
from pygame import mixer
import time

pygame.init()

display = pygame.display.set_mode((800, 600))

# Bilder laden
# Gamesteuerungsbilder
start_img = pygame.image.load('bilder/start.png').convert_alpha()
exit_img = pygame.image.load('bilder/exit.png').convert_alpha()
exit1_img = pygame.image.load('bilder/exit1.png').convert_alpha()
continue_img = pygame.image.load('bilder/continue.png').convert_alpha()
reset_img = pygame.image.load('bilder/reset.png').convert_alpha()
# Figurenbilder
rock_img = pygame.image.load('bilder/rock.png').convert_alpha()
paper_img = pygame.image.load('bilder/paper.png').convert_alpha()
scissors_img = pygame.image.load('bilder/scissors.png').convert_alpha()
# Menubilder
menu_img = pygame.image.load('bilder/menu.png').convert_alpha()
back_img = pygame.image.load('bilder/back.png').convert_alpha()
mute_img = pygame.image.load('bilder/mute.png').convert_alpha()
unmute_img = pygame.image.load('bilder/sound-on.png').convert_alpha()
# Colorbuttons
blue_img = pygame.image.load('bilder/blue.png').convert_alpha()
pink_img = pygame.image.load('bilder/pink.png').convert_alpha()
yellow_img = pygame.image.load('bilder/yellow.png').convert_alpha()
# Musicbuttons
music1_img = pygame.image.load('bilder/live.png').convert_alpha()
music2_img = pygame.image.load('bilder/music.png').convert_alpha()
music3_img = pygame.image.load('bilder/note.png').convert_alpha()

# Clicksound initialisieren
clicked_sound = pygame.mixer.Sound("sound/mixkit-game-ball-tap-2073.wav")
clicked_sound.set_volume(1.0)


# Klasse definieren
class Buttons():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        # self.rect.topleft = (x, y)
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    # Abbildungsfunktion definieren
    def draw(self, surface):
        action = False

        # Mausposition
        pos = pygame.mouse.get_pos()

        # check Mouseover und Klicks
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                clicked_sound.play()
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        # Button auf Screen zeichnen
        display.blit(self.image, (self.rect.x, self.rect.y))
        return action


# Fälle definieren/ Parameter hinzufügen
# Gamesteuerung
start_button = Buttons(953, 463, start_img, 0.6)
exit_button = Buttons(20, -10, exit_img, 0.45)
exit1_button = Buttons(1003, 483, exit1_img, 0.45)
continue_button = Buttons(563, 283, continue_img, 0.3)
reset_button = Buttons(20, 546, reset_img, 0.3)
# Figuren
rock_button = Buttons(200, 238, rock_img, 0.6)
paper_button = Buttons(486, 200, paper_img, 0.6)
scissors_button = Buttons(772, 200, scissors_img, 0.6)
# Menu
menu_button = Buttons(1106, 20, menu_img, 0.3)
back_button = Buttons(10, 20, back_img, 0.3)
mute_button = Buttons(250, 170, mute_img, 0.2)
unmute_button = Buttons(450, 170, unmute_img, 0.2)
# Colorbuttons
blue_button = Buttons(250, 320, blue_img, 0.2)
pink_button = Buttons(450, 320, pink_img, 0.2)
yellow_button = Buttons(650, 315, yellow_img, 0.22)
# Musicbuttons
music1_button = Buttons(250, 460, music1_img, 0.2)
music2_button = Buttons(450, 460, music2_img, 0.2)
music3_button = Buttons(650, 460, music3_img, 0.2)

# Game Loop zum Ausprobieren
'''run = True
while run:
    display.fill((100, 55, 255))

    start_button.draw(display)

    pygame.display.update()

    # Eventhandler
    for event in pygame.event.get():
        # Exit Game
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

        # pygame.QUIT
    pygame.display.update()'''
