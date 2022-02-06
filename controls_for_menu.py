import pygame
import sys

from window_cotrol import control_window
import music


def event_menu(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                music.draw_pause(screen)
            elif event.key == pygame.K_e:
                music.draw_unpause(screen)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 200 < event.pos[0] < 600 and 250 < event.pos[1] < 400:  # play
                pass
            elif 200 < event.pos[0] < 600 and 420 < event.pos[1] < 620:  # choose skin
                pass
            elif 200 < event.pos[0] < 600 and 590 < event.pos[1] < 790:
                pygame.mixer.music.stop()
                control_window()
                sys.exit()