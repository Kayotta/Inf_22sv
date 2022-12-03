import pygame
import sys

pygame.init()

display = pygame.display.set_mode((800, 600))

# Startbutton
# Startbutton laden
start_img = pygame.image.load('Start.png').convert_alpha()

# Klasse definieren
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect
        #self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # Mausposition
        pos = pygame.mouse.get_pos()
        print(pos)

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
start_button = Button(100, 200, start_img, 1)

# Game Loop
run = True
while run == True:
    display.fill((100, 55, 255))

    if start_button.draw():
        print('START')




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.QUIT



