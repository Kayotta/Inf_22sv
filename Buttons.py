import pygame
import sys

pygame.init()

display = pygame.display.set_mode((800, 600))

# Startbutton
# Startbutton laden
start_img = pygame.image.load('Start.png').convert_alpha()
exit_img = pygame.image.load('exit.png').convert_alpha()
rock_img = pygame.image.load('rock.png').convert_alpha()
paper_img = pygame.image.load('paper.png').convert_alpha()
scissor_img = pygame.image.load('scissor.png').convert_alpha()


# Klasse definieren
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        #self.rect.topleft = (x, y)
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # Mausposition
        pos = pygame.mouse.get_pos()

        # check Mouseover und Klicks
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Button auf Screen zeichnen
        display.blit(self.image, (self.rect.x, self.rect.y))
        return action


# Fälle definieren
start_button = Button(305, 200, start_img, 3)
exit_button = Button(550, 750, exit_img, 0.5)
rock_button = Button(300, 200, rock_img, 0.5)
paper_button = Button(500, 200, paper_img, 0.5)
scissor_button = Button(700, 200, scissor_img, 0.5)

# Game Loop
run = True
while run:
    display.fill((100, 55, 255))

    start_button.draw()
    if start_button.clicked == True:
        print('start')

    # Eventhandler
    for event in pygame.event.get():
        # Exit Game
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

        # pygame.QUIT
    pygame.display.update()
