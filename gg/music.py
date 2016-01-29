# -*- coding: utf-8 -*-

import pygame

_songs = [
    '/Users/shenjialong/Slippin.mp3',
    '/Users/shenjialong/Slippin.mp3'
]

_commands = [
    'restart',
    'start',
    'stop',
    'quit',
    'next',
]


class Music(object):

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_mode([200, 100])
        pygame.time.delay(1000)

    def play(self):
        for song in _songs:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                command = raw_input("Input a command: ")
                if command not in _commands:
                    print "commands ===> `{}` availd!!".format(command)
                    continue
                else:
                    if command == 'start':
                        pygame.mixer.music.unpause()
                        print "Resume Paused Music..."
                    if command == 'stop':
                        pygame.mixer.music.pause()
                        print "Pause Current Music..."
                    if command == 'next':
                        pygame.mixer.music.stop()
                        print "Playing Next..."
                    if command == 'restart':
                        pygame.mixer.music.rewind()
                        print "Restart Current Music..."
                    if command == 'quit':
                        pass
