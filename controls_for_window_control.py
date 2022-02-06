import pygame
import sys

import all_sprit


def event_for_window_control(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 250 < event.pos[0] < 550 and 650 < event.pos[1] < 750:
                from free_play import run
                run()
                sys.exit()
            elif 750 < event.pos[0] < 790 and 10 < event.pos[1] < 50:
                from menu import first_window
                first_window()
                sys.exit()