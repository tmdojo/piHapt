#!/usr/bin/python3

"""
https://learn.adafruit.com/raspberry-pi-pygame-ui-basics/overview
"""
import os

import pygame

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((320, 240))
movie = pygame.movie.Movie("asset/sl.mpg")

lcd.fill((255,0,0))
pygame.display.update()
pygame.mouse.set_visible(False)
while True:
    pass
