import pygame
import all_sprit

import music
from controls_for_menu import event_menu


def first_window():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Ailen")

    # загружаем музыку
    music.start_music(0)
    music.draw_unpause(screen)

    # рисуем окно меню
    all_sprit.create_menu(screen)

    while True:
        event_menu(screen)

        pygame.display.flip()


first_window()