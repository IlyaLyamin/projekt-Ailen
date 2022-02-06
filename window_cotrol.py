import pygame
import sys

import all_sprit
from controls_for_window_control import event_for_window_control


def control_window():
    # создание окна
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")

    # прорисовка окна
    all_sprit.create_window_control(screen)

    while True:
        event_for_window_control(screen)
        pygame.display.flip()