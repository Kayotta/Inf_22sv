import pygame
import sys
from pygame import mixer
import time

pygame.init()

display = pygame.display.set_mode((800, 600))

# Startbutton
# Startbutton laden
start_img = pygame.image.load('bilder/start.png').convert_alpha()
exit_img = pygame.image.load('bilder/exit.png').convert_alpha()
continue_img = pygame.image.load('bilder/continue.png').convert_alpha()
reset_img = pygame.image.load('bilder/reset.png').convert_alpha()
rock_img = pygame.image.load('bilder/rock.png').convert_alpha()
paper_img = pygame.image.load('bilder/paper.png').convert_alpha()
scissors_img = pygame.image.load('bilder/scissors.png').convert_alpha()

# Soundeffekte
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



# Fälle definieren
start_button = Buttons(20, 0, start_img, 0.5)  # (305, 200, start_img, 3)
exit_button = Buttons(600, 450, exit_img, 0.3)
continue_button = Buttons(305, 200, continue_img, 0.3)
reset_button = Buttons(20, 430, reset_img, 0.3)
rock_button = Buttons(90, 200, rock_img, 0.4)
paper_button = Buttons(230, 150, paper_img, 0.6)
scissors_button = Buttons(490, 180, scissors_img, 0.5)

# Game Loop
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
