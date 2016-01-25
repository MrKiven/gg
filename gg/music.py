# -*- coding: utf-8 -*-

import pygame
import sys


def play_music():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_mode([100, 100])
    pygame.time.delay(1000)
    pygame.mixer.music.load("/Users/shenjialong/Slippin.mp3")  # your music path
    pygame.mixer.music.play()
    while 1:
        try:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
        except KeyboardInterrupt:
            sys.exit(1)
