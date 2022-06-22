import time

import pygame

for c in range(10, -1, -1):
    print('\033[1;33m{}\033[m'.format(c))
    time.sleep(1)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('desafio_046.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
print('\033[1;4;31mBOOM\033[m')