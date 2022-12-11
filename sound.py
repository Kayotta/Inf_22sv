import pygame
from pygame import mixer
# Soundintegration
pygame.mixer.init()  # initialisierre den Soundmixer

'''sound_rooster = pygame.mixer.Sound("Mein Song 7.m4a")  # rooster.wav
    sound_rooster.set_volume(1.0)  # setze die Lautstärke'''

# song = "C:\Users\sophi\Music\Songs\Mein Song 7.m4a"
# mixer.init()
mixer.music.load("C:\Users\sophi\OneDrive\Desktop\2b\Informatik\Inf_22sv\Mein Song 7.m4a")
mixer.music.set_volume(1.0)
mixer.music.play(-1)
mixer.music.stop()
